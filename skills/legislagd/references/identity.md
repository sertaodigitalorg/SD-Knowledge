# Identidade e Keycloak

## Keycloak Legislativo

Sistema centralizado de identidade para LegislaGD.

## Usuários

### Tipos

1. **Parlamentar**
   - Login + 2FA
   - Acesso a SAPL, e-Cidade
   - Dados de gabinete
   - Sessões legislativas

2. **Servidor Público (Staff)**
   - Login + 2FA
   - Acesso limitado por setor
   - e-Cidade (administrativo)
   - SIGI (protocolo/atendimento)

3. **Cidadão**
   - Registro em SIGI
   - Acesso a PortalModelo-SD (leitura pública)
   - Criar protocolos
   - Autenticação social (Google, Microsoft, Autenticação .GOV.BR)

4. **Admin/Gestor**
   - Full access
   - Gerenciamento de usuários
   - Configuração de políticas
   - Auditoria

---

## Papéis (RBAC)

Hierarquia de papéis:

- `admin` — Administrador de sistema
- `gestor_sapl` — Gestor de SAPL
- `gestor_ecidade` — Gestor de e-Cidade
- `gestor_sigi` — Gestor de SIGI
- `parlamentar` — Parlamentar
- `staff_legislativo` — Staff legislativo
- `staff_administrativo` — Staff administrativo
- `atendente` — Atendente de protocolo
- `cidadao` — Cidadão
- `usuario_portal` — Apenas consulta pública

---

## Autenticação

### Fluxo Login Parlamentar

```
Parlamentar → Tela Login
           ↓
    Insere Credencial
           ↓
    Keycloak valida
           ↓
    2FA (SMS/Email/TOTP)
           ↓
    Token JWT emitido
           ↓
    Acesso a recursos
```

### Fluxo Login Cidadão

```
Cidadão → Tela Portal
       ↓
Opções:
├─ Criar conta
├─ Login Google
├─ Login Microsoft
└─ Login Gov.BR (futuro)
       ↓
Keycloak processa
       ↓
Redireção e token
       ↓
Acesso limitado (portal + SIGI)
```

---

## Autorização (RBAC)

Cada recurso tem requerimento de papel:

```
GET /api/sapl/proposicoes
  → Público (sem autenticação)

GET /api/sapl/proposicoes/1234/historico
  → Requer: autenticado

POST /api/sapl/proposicoes
  → Requer: admin ou gestor_sapl

DELETE /api/parlamentar/1
  → Requer: admin
```

---

## Sessão

- Token JWT com expiry
- Refresh token para renovação
- SSO entre SAPL, SIGI, e-Cidade
- Logout revoga tokens
- Suporta múltiplos dispositivos

---

## Federação (Futuro)

Quando integrar Executivo:

- Keycloak separado no Executivo
- Federação SAML/OIDC
- **Sem sincronização automática de usuários**
- Consentimento necessário para compartilhamento

---

## Segurança

- Senhas com hash PBKDF2/bcrypt
- HTTPS obrigatório
- Rate limiting em login
- Detecção de tentativas brute-force
- 2FA para parlamentar/admin
- Auditoria de login
- Sessão com timeout
- Protecção CORS

---

## Sincronização de Dados

Keycloak como source de truth:

- e-Cidade sincroniza usuários
- SAPL consulta Keycloak
- SIGI consulta Keycloak

Fluxo:
```
Novo usuário criado em Keycloak
           ↓
Webhook para e-Cidade
           ↓
e-Cidade cria usuário RH
           ↓
Token JWT contém informação
           ↓
Outros serviços consultam Keycloak
```

---

## LDAP/Active Directory

Pode-se conectar para:
- Importação inicial de usuários
- Sincronização periódica
- Validação contra AD corporativo

(Futuro: esclarecer requisitos institucionais)
