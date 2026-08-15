# Skill: legislagd

---

## Metadados

| Campo | Valor |
|---|---|
| **Name** | legislagd |
| **Description** | Contexto funcional, arquitetural e de integração para desenvolvimento e manutenção da plataforma pública livre LegislaGD. |
| **Version** | 1.0.0 |
| **Status** | active |
| **Author** | Sertão Digital |
| **Type** | product-context |

---

## Propósito

Esta Skill fornece contexto específico sobre:

- **LegislaGD** — plataforma legislativa livre
- **Arquitetura de integração** — componentes legislativos
- **Identidade centralizada** — Keycloak do Legislativo
- **Relacionamentos** com produtos complementares
- **Workflows** de desenvolvimento e deployment
- **Princípios de compatibilidade** com upstream

LegislaGD é uma plataforma **DO PODER LEGISLATIVO**, não Executivo.

---

## Escopo

### LegislaGD - Core

Plataforma legislativa integrada baseada em:

- SAPL-SD — Sistema de Acompanhamento de Processo Legislativo
- PortalModelo-SD — Portal institucional
- Keycloak Legislativo — Identidade e SSO
- Integrações com sistemas complementares

### Componentes Relacionados

```
LegislaGD
  ├── SAPL-SD (processo legislativo)
  ├── PortalModelo-SD (portal institucional)
  ├── e-Cidade-SD (funções administrativas)
  ├── SIGI-SD (atendimento ao cidadão)
  └── Keycloak Legislativo (identidade/SSO)
```

### Não Incluído em legislagd

- ❌ Sistemas do Poder Executivo (escopo separado, futuro)
- ❌ Integração Executivo-Legislativo (será elaborada depois)
- ❌ Sistemas verticais específicos (cada um com sua Skill)

---

## Quando Usar

✅ **Use legislagd quando:**

- Trabalhar em LegislaGD (plataforma core)
- Integrar SAPL-SD, PortalModelo-SD, e-Cidade-SD, ou SIGI-SD
- Lidar com autenticação/autorização do Legislativo
- Discussões sobre arquitetura legislativa
- Processo legislativo (sessões, proposições, parlamentares)
- Atendimento ao cidadão relacionado ao Legislativo
- Gestão administrativa do Legislativo

❌ **Não use quando:**

- Trabalhar em sistemas do Executivo (Skill separada)
- Questões puramente institucionais (use sertaodigital-core)
- Detalhes matemáticos ou algorítmicos puros

---

## Arquitetura Conceitual

```
┌─────────────────────────────────────────────────────┐
│                   LegislaGD                         │
│            (Plataforma Legislativa)                 │
└────────┬────────────────────────────┬───────────────┘
         │                            │
    ┌────v─────┐          ┌──────────v─────┐
    │  SAPL-SD  │          │ PortalModelo-SD│
    │ (Process) │          │   (Portal)     │
    └────┬──────┘          └────┬───────────┘
         │                      │
         └──────┬───────────────┘
                │
         ┌──────v─────────────┐
         │ Keycloak Legislativo│
         │  (Identity/SSO)    │
         └──────┬─────────────┘
                │
    ┌───────────┴──────────────┐
    │                          │
┌───v─────┐            ┌──────v────┐
│e-Cidade │            │ SIGI-SD    │
│  (RH)   │            │(Atendimento)
└─────────┘            └────────────┘
```

### SAPL-SD

**Sistema de Acompanhamento de Processo Legislativo**

- Proposições (projetos, emendas)
- Sessões e plenário
- Parlamentares e gabinetes
- Votações
- Compatibilidade com upstream SAPL

**Repositório:** Será registrado em `repositories.yaml`

**Compatibilidade:** Mantém interface com projeto upstream sempre que possível

### PortalModelo-SD

**Portal Institucional**

- Publicação de conteúdo legislativo
- Acesso público a informações
- Interface com cidadão

**Repositório:** Será registrado em `repositories.yaml`

### e-Cidade-SD

**ERP Municipal/Legislativo**

Funções administrativas:
- RH e folha de pagamento
- Gestão administrativa
- Contabilidade
- Patrimônio

Pode ser compartilhado entre Legislativo e Executivo (futuro), mas inicialmente escopoado para Legislativo.

### SIGI-SD

**Sistema de Gestão de Políticas Internas**

Atendimento ao cidadão:
- Protocolo de atendimento
- Chatwoot (omnichannel)
- IA de atendimento
- Protocolo integrado

### Keycloak Legislativo

**Identidade Centralizada**

- Autenticação única (SSO)
- RBAC (Role-Based Access Control)
- Federação de identidades
- Integração SAML/OIDC

**Importante:** Legislativo terá seu próprio Keycloak. Executivo terá Keycloak separado (futuro).

**Não assuma compartilhamento automático de identidade entre Poderes.**

---

## Arquitetura de Identidade

### Poder Legislativo (LegislaGD)

```
Usuários do Legislativo
        ↓
Keycloak Legislativo (Centralizado)
        ↓
   SAPL-SD, PortalModelo-SD, e-Cidade-SD, SIGI-SD
```

**Princípio:** Uma identidade central para todos os sistemas do Legislativo.

### Poder Executivo (Futuro)

Terá arquitetura de identidade **independente** (Keycloak separado).

### Interoperabilidade Futura

Quando necessário integrar Poderes:
- Federação de identidade
- Protocolo SAML/OIDC entre Keycloaks
- **Não assume compartilhamento de usuários**
- Consentimento e autorização explícita

---

## Dependências

### Requerida

```yaml
dependencies:
  required:
    - sertaodigital-core  # Contexto institucional
```

### Condicional

```yaml
dependencies:
  conditional:
    sapl-sd:
      when:
        - processo legislativo
        - sessões e plenário
        - parlamentares
        - proposições
        - votações
        
    sigi-sd:
      when:
        - atendimento ao cidadão
        - protocolo
        - Chatwoot
        - omnichannel
        - IA de atendimento
        
    ecidade-sd:
      when:
        - RH
        - folha de pagamento
        - gestão administrativa
        - contabilidade
        - patrimônio
        
    keycloak:
      when:
        - login
        - autenticação
        - autorização
        - SSO
        - RBAC
```

---

## Regras de Arquitetura

### 1. Identidade

- ✅ Keycloak Legislativo é centralizado
- ✅ Todos os sistemas usam mesma identidade
- ❌ Não assuma Keycloak compartilhado com Executivo
- ❌ Não compartilhe usuários sem consentimento

### 2. Compatibilidade Upstream

- ✅ SAPL-SD mantém compatibilidade com SAPL sempre que possível
- ✅ PortalModelo-SD segue padrões de portal aberto
- ❌ Não force mudanças que quebrem upstream sem razão forte

### 3. Acoplamento

- ✅ Componentes devem ser o mais independentes possível
- ✅ Use APIs bem definidas
- ❌ Evite acoplamento desnecessário
- ❌ Cada componente deve ser deployável independentemente

### 4. Legislativo vs Executivo

- ✅ LegislaGD é **exclusivamente** Legislativo
- ✅ Executivo terá solução separada (futuro)
- ❌ Não misture conceitos de Legislativo com Executivo
- ❌ Não presuma estrutura Executiva em LegislaGD

### 5. Integração Futura

- ✅ Planeje para interoperabilidade entre Poderes
- ✅ Use protocolos padrão (SAML, OIDC)
- ✅ Documente pontos de integração
- ❌ Não force integração prematura
- ❌ Consentimento explícito para compartilhamento de dados

---

## Fluxos de Desenvolvimento

### Novo Feature em Produto Legislativo

```
Issue → Branch → Feature → PR → Review → Merge

1. Abra issue descrevendo feature
2. Crie branch (feature/descricao)
3. Implemente com testes
4. PR com:
   - Objetivo
   - Impacto legislativo
   - Compatibilidade upstream
   - Segurança
5. Review pela equipe
6. Merge em main
```

### Bug Fix

```
Issue → Branch → Fix → Tests → PR → Merge

Similar a novo feature, mas com prioridade.
```

### Integração/Mudança Arquitetural

```
Discussão → Proposal → Prototipo → Revisão → Decision → Implementation

1. Discussão em issue
2. Proposta documentada
3. Prototipo se necessário
4. Revisão arquitetural
5. Decisão final (com sertaodigital-core se global)
6. Implementação e documentação
```

### Atualização de Documentação

```
Issue → Branch → Update → Validação → PR → Merge

Revise referências cruzadas.
```

---

## Produtos e Repositórios

Veja `manifests/repositories.yaml` para lista completa de repositórios legislativos.

Principais:
- LegislaGD (core, será registrado)
- SAPL-SD (será registrado)
- PortalModelo-SD (será registrado)
- e-Cidade-SD (será registrado)
- SIGI-SD (será registrado)

---

## Segurança

### Acesso Parlamentar

- Dados públicos de proposições, sessões
- Dados privados de gabinete/parlamentar (controle de acesso)
- Histórico legislativo (auditável)

### Dados de Cidadão

- LGPD compliance
- Consentimento para atendimento
- Direito ao esquecimento

### Secrets

- Não expor em repositório público
- Use variáveis de ambiente
- Credenciais em Deploy apenas
- Veja SECURITY.md

### Auditoria

- Log de ações de usuário
- Histórico de proposições
- Rastreamento de sessões
- Dados completos e inalterados

---

## Integração com IA e Agentes

Quando um agente trabalha em legislagd:

1. Carregue `sertaodigital-core/SKILL.md` (base)
2. Carregue `legislagd/SKILL.md` (este arquivo)
3. Consulte arquitetura em `references/`
4. Valide contra hierarquia de fontes
5. Respeite regras de arquitetura
6. Use manifestos para referências de repositório

---

## Versionamento

Seguir Semantic Versioning:

- **MAJOR:** Quebra de compatibilidade, mudança arquitetural
- **MINOR:** Nova funcionalidade compatível
- **PATCH:** Correção de bug

Documentar mudanças em CHANGELOG.md.

---

## Referências

- `docs/SDKA.md` — Especificação da SDKA
- `docs/SOURCE_OF_TRUTH.md` — Hierarquia de fontes
- `skills/sertaodigital-core/SKILL.md` — Contexto institucional
- `repositories.yaml` — Lista de repositórios
- `products.yaml` — Registro de produtos

---

## Contato

Para questões sobre legislagd:

- Consulte `references/` para tópicos específicos
- Abra issue no GitHub
- Utilize canais institucionais oficiais do Sertão Digital

---

**Versão:** 1.0.0  
**Última atualização:** 2026-08-15  
**Status:** Active
