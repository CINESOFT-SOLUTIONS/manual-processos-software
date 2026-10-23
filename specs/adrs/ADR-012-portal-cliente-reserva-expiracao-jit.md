# ADR-012 - Portal do Cliente, Autenticação de Espectador, Expiração Just-in-Time e Notificação Transacional

## Status
Aprovada

## Data
2026-10-23

## Contexto
O CineDoom foi originalmente concebido como um MVP focado nos módulos do Atendente (bilheteria física) e do Gerente (backoffice). A incorporação do **Portal do Cliente** permite que o espectador final consulte a programação, crie uma conta com login/senha, selecione assentos no mapa interativo e solicite uma **reserva de ingressos para pagamento presencial** na bilheteria física até 1 hora antes do início da sessão.

Para viabilizar essa funcionalidade no prazo de 21 dias sem comprometer a estabilidade do sistema, quatro desafios arquiteturais foram endereçados:
1. **Concorrência e bloqueio de assentos:** Uma reserva não pode permitir que outro cliente ou atendente compre ou reserve o mesmo assento.
2. **Expiração de reservas pendentes:** Se o cliente não comparecer até 60 minutos antes da sessão, os assentos devem ser liberados automaticamente sem sobrecarregar a arquitetura serverless na Vercel com servidores de fila dedicados (como Redis/BullMQ).
3. **Autenticação e LGPD do cliente final:** O cliente precisa acessar seu histórico pessoal de compras/reservas e ter a faculdade de cancelar sua reserva voluntariamente antes do prazo limite.
4. **Comprovante de reserva:** O cliente necessita de instruções claras e inequívocas de comparecimento e pagamento presencial, recebidas em tela e por e-mail transacional.

## Decisão
1. **Trava ACID com Status `RESERVED`:**
   - Adição do status `RESERVED` na tabela `session_seats`.
   - A criação de uma reserva executa transação no PostgreSQL com `SELECT FOR UPDATE` na linha do assento, preenchendo `reservation_id` e `reservation_expires_at = starts_at - INTERVAL '1 hour'`.
   - Se o horário atual for superior a `starts_at - 1h`, novas reservas são rejeitadas (`HTTP 422 Unprocessable Entity`), permitindo apenas vendas diretas no balcão.

2. **Expiração sob Demanda (*Just-in-Time / Lazy Expiration*):**
   - Em vez de orquestrar workers ou cron jobs externos a cada segundo, a expiração é avaliada diretamente no PostgreSQL:
     ```sql
     -- Assento considerado ocupado se vendido OU se reservado e ainda dentro do prazo de validade
     WHERE status = 'SOLD'
        OR (status = 'RESERVED' AND reservation_expires_at > NOW())
     ```
   - Nas consultas do mapa de assentos (`GET /api/sessoes/[id]/assentos`) e em tentativas de venda presencial de balcão, assentos com `status = 'RESERVED' AND reservation_expires_at <= NOW()` são atualizados sob demanda para `AVAILABLE` com `reservation_id = NULL`, liberando os assentos imediatamente sem custos adicionais de infraestrutura.

3. **Autenticação Unificada com Perfil `CLIENTE` (NextAuth.js):**
   - Extensão do modelo `users` para suportar `role = 'CLIENTE'` associado ao tenant.
   - O cadastro exige nome, e-mail, senha com hash bcrypt/argon2 e CPF protegido pela arquitetura de duas camadas do `CryptoService` (HMAC-SHA256 para indexação e AES-256-GCM para armazenamento), além de consentimento LGPD explícito com timestamp.
   - O cliente autenticado acessa o dashboard "Minhas Reservas", onde pode visualizar comprovantes e disparar cancelamento voluntário de reservas `PENDING`.

4. **Cancelamento Voluntário pelo Cliente via Web:**
   - Rota `POST /api/portal/reservas/[id]/cancelar` restrita ao dono da reserva.
   - Valida se `status == 'PENDING'` e `NOW() < reservation_expires_at`.
   - Atualiza `reservations.status = 'CANCELLED'`, preenche `cancelled_at = NOW()` e limpa os assentos vinculados em `session_seats` para `AVAILABLE` de forma atômica.

5. **Notificação Transacional de Reserva:**
   - Módulo `NotificationService` desacoplado que envia o voucher por e-mail transacional (adaptador Resend/Nodemailer em produção e log formatado em console no ambiente de desenvolvimento).
   - O voucher contém o código identificador (ex.: `CD-8942`), dados da sessão, assentos, valor total e alerta explícito de expiração 1 hora antes do início do filme.

6. **Baixa Presencial Integrada na Bilheteria:**
   - O Atendente pesquisa a reserva por código (`CD-XXXX`) ou CPF do cliente.
   - O sistema valida a vigência. Ao confirmar o recebimento em dinheiro, débito ou crédito físico, converte a reserva para `CONFIRMED`, gera o `Ticket` fiscal e atualiza `session_seats.status = 'SOLD'`.

## Consequências
### Positivas
- **Viabilidade Estrita:** Não necessita de gateway de pagamento online, antifraude ou liquidação financeira externa.
- **Eficiência e Custo Zero:** Zero dependência de Redis ou workers assíncronos para gerenciamento de expiração.
- **Rastreabilidade e Segurança:** Histórico completo de reservas por cliente com rigorosa conformidade LGPD.
- **Consistência Matemática:** A trava pessimista `SELECT FOR UPDATE` elimina qualquer possibilidade de conflito entre reservas web e vendas físicas no balcão.

### Negativas / Mitigações
- **Assentos Ociosos:** Se o cliente reservar e não comparecer, o assento fica bloqueado até 1 hora antes da sessão. *Mitigação:* A margem de 1 hora assegura que o cinema tenha tempo hábil para vender o assento liberado para clientes na fila presencial.
