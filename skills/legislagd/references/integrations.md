# Integrações

## Entre Componentes LegislaGD

### SAPL-SD ↔ PortalModelo-SD

- SAPL fornece dados legislativos
- Portal consome e exibe publicamente
- Cache de dados públicos
- Atualizações em tempo real (WebSocket opcional)

### SAPL-SD ↔ SIGI-SD

- Cidadão cria protocolo sobre proposição
- SIGI consulta SAPL para contexto
- Link bidirecional (protocolo ↔ proposição)
- Notificações de mudanças

### SAPL-SD ↔ e-Cidade-SD

- Dados de parlamentares sincronizados
- RH/folha referencia parlamentares
- Histórico de mandatos
- Afastamentos e licenças

### Todos ↔ Keycloak

- Autenticação centralizada
- Sincronização de usuários
- Atualização de papéis (RBAC)
- Sessão única

---

## Pontos de Integração

### APIs Públicas (SAPL)

- Consulta de proposições
- Busca de sessões
- Histórico legislativo
- Dados de parlamentares

**Documentação:** OpenAPI em repositório SAPL-SD

### APIs Internas

- Sincronização de usuários (Keycloak)
- Protocolo ↔ Proposição (SAPL/SIGI)
- Dados administrativos (e-Cidade)

**Segurança:** Apenas intra-cluster, JWT validado

---

## Futuras Integrações

### Executivo (Futuro)

Não assume integração no momento.

Quando acontecer:
- Keycloak separado
- Federação de identidade
- APIs bem definidas
- Consentimento explícito

### Câmaras Municipais Externas

Arquitetura permite:
- Multi-tenancy
- Instâncias separadas
- Sincronização opcional
- Federação de dados

---

## Tipos de Dados Compartilhados

### Públicos

- Proposições
- Sessões (atas)
- Votações
- Parlamentares (dados públicos)

Sem restrição de acesso.

### Restritos

- E-mail de parlamentar
- Endereço pessoal
- Dados de gabinete
- RH (salários, afastamentos)

Acesso apenas com RBAC apropriado.

### Pessoais (LGPD)

- Cidadão criando protocolo
- Dados de atendimento
- Histórico de comunicação

Protegidos conforme LGPD.
- Consentimento necessário
- Direitos dos titulares e hipóteses de eliminação, retenção e tratamento conforme LGPD e obrigações legais aplicáveis
- Minimização de dados

---

## Tratamento de Erros

Integrações devem:

- Ter retry logic
- Falhar gracefully
- Logar erros
- Alertar quando crítico
- Permitir operação degradada

### Exemplo

Se SIGI não responde:
- SAPL continua funcionando
- Portal continua funcionando
- Usuário vê mensagem (protocolado depois)
