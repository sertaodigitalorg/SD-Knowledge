# Arquitetura LegislaGD

## Visão Geral

```
┌─────────────────────────────────────────┐
│         Interface Pública (Portal)      │
│       (PortalModelo-SD)                 │
└──────────────────┬──────────────────────┘
                   │
        ┌──────────v──────────┐
        │   API Gateway       │
        │  (Autenticação)     │
        └──────────┬──────────┘
                   │
    ┌──────────────┼──────────────┐
    │              │              │
┌───v─────┐  ┌────v────┐  ┌──────v────┐
│  SAPL   │  │e-Cidade │  │  SIGI     │
│Backend  │  │Backend  │  │Backend    │
└───┬─────┘  └────┬────┘  └──────┬────┘
    │             │              │
    └─────────────┼──────────────┘
                  │
         ┌────────v────────┐
         │  Keycloak       │
         │  Legislativo    │
         └─────────────────┘
```

## Componentes

### Frontend (PortalModelo-SD)

- Interface web responsiva
- Consulta pública de proposições
- Autenticação integrada
- Acesso a sessões públicas

### SAPL-SD Backend

- Gerenciamento de proposições
- Controle de sessões
- Registro de parlamentares
- Histórico legislativo
- API para integrações

### e-Cidade-SD Backend

- Gestão administrativo-financeira
- RH e folha
- Patrimônio
- Contabilidade

### SIGI-SD Backend

- Atendimento ao cidadão
- Protocolo
- Omnichannel (web, chat, email)
- IA de classificação/roteamento

### Keycloak

- Autenticação centralizada
- Autorização (RBAC)
- Sessão única (SSO)
- Federação de identidades

---

## Fluxo de Autenticação

```
Usuário
    ↓
Login (Keycloak)
    ↓
Token (JWT)
    ↓
API Gateway valida
    ↓
Acesso ao Backend apropriado
    ↓
Recursos conforme RBAC
```

---

## Integração Entre Componentes

### SAPL → SIGI

- Cidadão pode criar protocolo sobre proposição
- Link entre protocolo e proposição
- Notificações de atualizações

### SAPL → e-Cidade

- Dados de parlamentares
- RH integrado
- Folha de pagamento

### e-Cidade → Keycloak

- Sincronização de usuários
- Atualização de RBAC

---

## Padrões Técnicos

### API

- REST com JSON
- Autenticação JWT
- Documentação OpenAPI
- Rate limiting
- CORS apropriado

### Banco de Dados

- PostgreSQL preferencial
- Migrações versionadas
- Backup e recuperação
- Replicação para HA

### Containerização

- Docker para cada componente
- docker-compose para desenvolvimento
- Kubernetes para produção

### CI/CD

- GitHub Actions para testes
- Validação automática
- Deploy automatizado
- Rollback rápido

---

## Escalabilidade

Preparado para:

- Múltiplas câmaras
- Múltiplos poderes legislativos
- Crescimento de dados
- Picos de carga

Uso de cache (Redis) quando necessário.

---

## Relacionamento com Upstream

SAPL-SD é fork mantida de SAPL.

Princípios:

- Acompanhar releases upstream quando possível
- Contribuições de volta para upstream
- Documentar diferenças
- Merge de correções (cherry-pick)
- Compatibilidade de dados
