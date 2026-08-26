# Prompt Handoff Standard

Padrão formal para transferência de responsabilidade entre camadas quando não há acesso direto.

---

## Definição

Um **Prompt Handoff** é um documento estruturado que encapsula contexto completo e instruções para que outro agente ou responsável execute uma mudança necessária em uma camada diferente da SDKA.

**Cenário típico:**
- Agente A identificou mudança necessária na camada técnica
- Agente A não tem acesso ao GitHub
- Agente A gera Prompt Handoff
- Agente B (com acesso ao GitHub) recebe e executa

**Princípio:** Ausência de acesso não elimina responsabilidade de sincronização. Apenas muda o mecanismo de entrega.

---

## Duas Categorias

### 1. TECHNICAL HANDOFF

**Origem:** Camada Funcional/Institucional (Google Drive)  
**Destino:** Camada Técnica (GitHub)  
**Quando:** Mudança funcional exige atualização técnica

**Exemplos:**
- Novo requisito funcional → novo componente técnico
- Mudança de regra de negócio → alteração de arquitetura
- Novo fluxo percebido pelo usuário → alteração de API
- Mudança de integração de negócio → novo endpoint

### 2. FUNCTIONAL HANDOFF

**Origem:** Camada Técnica (GitHub)  
**Destino:** Camada Funcional/Institucional (Google Drive)  
**Quando:** Mudança técnica afeta funcionamento percebido

**Exemplos:**
- Alteração de API → documentação de uso
- Mudança de permissões técnicas → manual de usuário
- Depreciação de funcionalidade → aviso em Drive
- Nova capacidade técnica → documentação operacional
- Mudança de implantação → guia de operação

## Leitura Por Camada Destino

Handoffs devem ser pesquisaveis e legiveis pela camada que precisa executa-los:

- agente tecnico le TECHNICAL HANDOFFs gerados pela camada funcional;
- agente funcional le FUNCTIONAL HANDOFFs gerados pela camada tecnica.

A interface conceitual comum e:

```text
handoff.search
handoff.read
```

Filtros minimos:

```yaml
type: TECHNICAL | FUNCTIONAL | null
origin_layer: functional | technical | null
target_layer: functional | technical | null
product: string | null
status: PENDING | IN_PROGRESS | COMPLETED | CANCELLED | null
```

O nome historico `functional.handoff.*` nao deve limitar a leitura apenas a
handoffs funcionais.

---

## Estrutura Padrão

### Seção de Metadados

```yaml
handoff_id: [YYYY-MM-DD]-[tipo]-[numero]
            # Exemplo: 2026-08-15-TECHNICAL-001

origin_layer: functional | technical
target_layer: technical | functional

product: [nome-do-produto]
         # Exemplo: legislagd

date: [ISO 8601]
      # Exemplo: 2026-08-15

origin_source: 
  type: drive | github | [autre]
  location: [caminho ou URL]
  reference: [ID de documento ou issue]
  date_accessed: [ISO 8601]

reason: [motivo-sucinto]
        # Exemplo: Novo requisito de autenticação multifator

access_state: NOT_FOUND | READ_DENIED | WRITE_DENIED | ACCESS_UNKNOWN | SOURCE_UNAVAILABLE | NOT_APPLICABLE

security_classification: [classificação aplicável]
```

### Seção de Contexto

```
## Origem

[Onde a mudança foi identificada]

Exemplo:
- Decisão formal no Drive
- Issue aberta no GitHub
- Feedback de usuário
- Reunião de stakeholders
- Arquitetura em evolução

## Contexto Funcional/Técnico

[Descrever o contexto completo]

Máximo: claro e conciso, evitar repetição
Incluir: situação atual, razão da mudança, impacto esperado
```

### Seção de Mudança

```
## Mudança Necessária

Descrição clara do que deve ser alterado:

[Descrever tecnicamente o que fazer]

Exemplo TECHNICAL:
- Adicionar campo "mfa_enabled" na tabela de usuários
- Atualizar API de login para validar MFA
- Atualizar documentação de API
- Adicionar testes de integração MFA

Exemplo FUNCTIONAL:
- Criar guia de ativação de MFA no manual
- Atualizar procedimento de onboarding
- Criar FAQ sobre MFA
- Atualizar RH sobre nova política de autenticação
```

### Seção de Impacto

```
## Impacto Cruzado

Componentes / Documentos / Módulos potencialmente afetados:

[Listar]

Exemplo TECHNICAL:
- Tabela: usuarios
- Tabela: sessoes
- Módulo: auth
- API: POST /login
- API: POST /mfa/verify
- Docs: API Reference
- Docs: Authentication Guide

Exemplo FUNCTIONAL:
- Procedimento: Onboarding de Usuários
- Manual: Operações Diárias
- Manual: Gerenciamento de Acesso
- Doc: FAQ Sistema
```

### Seção de Validação

```
## Resultado Esperado

[Descrever o estado final verificável que o agente receptor deve produzir]

## Critérios de Validação

Como confirmar que a mudança foi implementada corretamente:

[Listar critérios específicos]

Exemplo TECHNICAL:
- [ ] Campo MFA criado e migrações executadas
- [ ] API aceita headers de MFA
- [ ] Endpoints validam token MFA
- [ ] Testes de integração passam
- [ ] Documentação atualizada
- [ ] Sem quebra de compatibilidade

Exemplo FUNCTIONAL:
- [ ] Documentação criada/atualizada
- [ ] Guia de uso é claro
- [ ] Procedimentos são step-by-step
- [ ] FAQ responde perguntas comuns
- [ ] Versão do documento atualizada
```

### Seção de Segurança

```
## Segurança e Privacidade

Considerações de segurança e classificação de dados:

[Descrever]

Exemplo:
- Classificação: Dado de acesso (Classe B)
- LGPD: Não contém dados pessoais sensíveis
- Secrets: Não inclua tokens/senhas
- Conformidade: Validar contra SECURITY.md
- Impacto de auditoria: Registrar mudanças em log
```

### Seção de Instruções para Agente

```
## Instruções para Agente Receptor

Passo a passo para executar a mudança:

[Para TECHNICAL HANDOFF]

1. Carregue AGENTS.md
2. Carregue Skills necessárias (identifique quais)
3. Execute Technical Decision Gate:
   a. Consulte código atual
   b. Analise arquitetura
   c. Revise ADRs (Architecture Decision Records)
   d. Valide compatibilidade upstream
   e. Considere impacto de integração
   e. Aprove decisão técnica
4. Criar branch feature/[nome]
5. Executar mudança (código/docs)
6. Atualizar Skills/manifests se aplicável
7. Criar PR com referência a este handoff
8. Aguardar revisão

[Para FUNCTIONAL HANDOFF]

1. Carregue Skills necessárias
2. Consulte SOURCE_OF_TRUTH.md
3. Identifique documento Master no Drive
4. Carregue autoridades relevantes
5. Atualizar documentação no Drive
6. Garantir versionamento
7. Registrar data de mudança
8. Notificar responsáveis conforme procedimento
9. Sincronizar Markdown para GitHub (se aplicável)
```

### Seção de Referências

```
## Fontes Consultadas

Documentação, issues, decisions que fundamentam este handoff:

[Listar URLs, referências, capítulos]

Exemplo:
- docs/SDKA.md (Princípios)
- skills/legislagd/SKILL.md (Contexto)
- GitHub issue #42 (Requisito original)
- docs/SOURCE_OF_TRUTH.md (Hierarquia)
- GitHub PR #15 (Contexto técnico anterior)
```

### Seção de Pendências

```
## Decisões Pendentes

Se houver decisões que não podem ser tomadas automaticamente:

[Listar decisões e critérios]

Exemplo:
- [ ] Qual framework usar para MFA? (Recomendação: Time-based OTP)
- [ ] Armazenar secrets em HSM ou Vault? (Recomendação: Vault)
- [ ] Período de migração? (Sugestão: 30 dias com aviso)
```

---

## Template Markdown Completo

```markdown
# Prompt Handoff

**ID:** [handoff_id]  
**Tipo:** TECHNICAL | FUNCTIONAL  
**Data:** [ISO 8601]  
**Produto:** [nome]  
**Status:** PENDING | IN_PROGRESS | COMPLETED | CANCELLED

---

## Origem

[Quem iniciou, onde, como]

---

## Contexto

[Situação atual, problema, por que mudar]

---

## Mudança Necessária

[O que fazer, passo a passo técnico/funcional]

---

## Resultado Esperado

[Estado final verificável]

---

## Impacto Cruzado

Componentes/Documentos afetados:
- [Item 1]
- [Item 2]
- ...

---

## Critérios de Validação

- [ ] Critério 1
- [ ] Critério 2
- [ ] Critério 3

---

## Segurança

[Classificação, LGPD, secrets, conformidade e estado de acesso]

---

## Instruções para Agente

1. ...
2. ...
3. ...

---

## Fontes Consultadas

- [Fonte 1](URL)
- [Fonte 2](URL)

---

## Decisões Pendentes

- [ ] Decisão 1 (recomendação: X)
- [ ] Decisão 2 (recomendação: Y)

---

## Observações

[Contexto adicional]

```

---

## Exemplo: TECHNICAL HANDOFF

> **EXEMPLO FICTÍCIO / NÃO NORMATIVO.** Os nomes, endpoints, tabelas, classificações, políticas e decisões abaixo são apenas ilustrativos e não representam implementação real ou decisão oficial do Sertão Digital ou de seus produtos.

```markdown
# Prompt Handoff - Novo Fluxo de Aprovação de Proposições

**ID:** 2026-08-15-TECHNICAL-001  
**Tipo:** TECHNICAL  
**Data:** 2026-08-15  
**Produto:** legislagd  
**Status:** PENDING

---

## Origem

Requisito identificado em Drive (doc assinado):
`SERTÃO DIGITAL/.../04_DOCUMENTACAO_DE_PRODUTOS/legislagd_novo_fluxo_aprovacao_v2.docx`

Decisão formal: Novo fluxo de aprovação em 3 estágios (pré-análise, análise, votação).

---

## Contexto

Atualmente LegislaGD não distingue pré-análise de análise.  
Novo fluxo exige:
- Criar estágio de pré-análise
- Registrar responsável por análise
- Validar permissões antes de votação

---

## Mudança Necessária

1. **Banco de Dados:**
   - Adicionar coluna `approval_stage` em proposicoes
   - Adicionar tabela `approval_stages` (enum)
   - Migração para proposições existentes: status `em_analise` → `pre_analise`

2. **API:**
   - Novo endpoint: PATCH /proposicoes/{id}/approve-step-1
   - Validar RBAC: apenas gestores podem avançar estágio
   - Adicionar validação: não pular estágios

3. **Documentação:**
   - Atualizar API Reference
   - Atualizar fluxo em docs/

4. **Testes:**
   - Testes de integração para cada transição de estágio

---

## Impacto Cruzado

- Tabelas: proposicoes, approval_stages
- APIs: /proposicoes/* endpoints
- Docs: API Reference, fluxo legislativo
- Skills: legislagd (references/domain.md, references/integrations.md)
- Manifestos: legislagd/manifests/product.yaml (versão, features)

---

## Critérios de Validação

- [ ] Banco de dados migrado
- [ ] APIs testadas (unit + integração)
- [ ] Sem quebra de compatibilidade com PortalModelo
- [ ] Documentação API atualizada
- [ ] Skill legislagd atualizada
- [ ] PR revisado conforme governance

---

## Segurança

- Classificação: Dados legislativos (Classe B - restrito)
- LGPD: Proposições são públicas por padrão, mas dados de análise podem incluir revisores
- Validação: Respeitar política de permissões existente
- Auditoria: Registrar quem avançou cada estágio

---

## Instruções para Agente

1. Carregue AGENTS.md
2. Carregue Skills: sertaodigital-core, legislagd
3. Consulte GitHub code: SAPL-SD repository
4. Execute Technical Decision Gate:
   - Analisar arquitetura atual de proposições
   - Revisar ADRs sobre RBAC
   - Validar compatibilidade com e-Cidade (RH)
   - Considerar impacto em relatórios/exportação
5. Criar branch: feature/proposicoes-3-stage-approval
6. Implementar mudanças (DB + API + tests + docs)
7. Atualizar legislagd Skill
8. Abrir PR com descrição completa
9. Solicitar revisão de gestor legislativo

---

## Fontes Consultadas

- docs/SDKA.md
- skills/legislagd/SKILL.md
- skills/legislagd/references/domain.md
- skills/legislagd/references/integrations.md
- docs/TECHNICAL_DECISION_GOVERNANCE.md
- GitHub: sertaodigitalorg/SAPL-SD (upstream)

---

## Decisões Pendentes

- [ ] Qual será o SLA para transição entre estágios? (Sugestão: sem limite, mas auditado)
- [ ] Reverter estágio (voltar de votação para análise) será permitido? (Sugestão: não, histórico apenas)

```

---

## Exemplo: FUNCTIONAL HANDOFF

> **EXEMPLO FICTÍCIO / NÃO NORMATIVO.** Os nomes, endpoints, tabelas, classificações, políticas e decisões abaixo são apenas ilustrativos e não representam implementação real ou decisão oficial do Sertão Digital ou de seus produtos.

```markdown
# Prompt Handoff - Documentação de Autenticação por Biometria

**ID:** 2026-08-15-FUNCTIONAL-001  
**Tipo:** FUNCTIONAL  
**Data:** 2026-08-15  
**Produto:** legislagd  
**Status:** PENDING

---

## Origem

Decisão técnica implementada em GitHub (PR #89):
- Novo backend de autenticação com suporte a biometria
- Integração com APIs nativas de dispositivos

---

## Contexto

A camada técnica implementou suporte a autenticação biométrica.
A camada funcional precisa documentar:
- Como ativar no navegador
- Compatibilidade de dispositivos
- Procedimento de configuração
- Troubleshooting comum

---

## Mudança Necessária

1. **Manual de Operação:**
   - Novo capítulo: "Autenticação Biométrica"
   - Pré-requisitos: navegador moderno, dispositivo com sensor

2. **Manual de RH:**
   - Atualizar política de autenticação
   - Informar que MFA pode ser agora biométrico OU senha

3. **FAQ:**
   - "Qual navegador suporta biometria?" → compatibilidade
   - "Posso usar biometria e senha?" → sim, os dois funcionam

4. **Treinamento:**
   - Criar guia visual passo-a-passo
   - Vídeo de demonstração (se aplicável)

---

## Impacto Cruzado

- Drive: manuais de operação
- Drive: política de segurança e RH
- Drive: FAQ sistema
- GitHub: Markdown derivado (se houver)
- Comunicação: avisar usuários finais

---

## Critérios de Validação

- [ ] Manual atualizado no Drive
- [ ] Versão incrementada
- [ ] FAQ inclui perguntas sobre biometria
- [ ] RH notificado de mudança de política
- [ ] Guia é acessível para usuários finais

---

## Segurança

- Classificação: Procedimento operacional (Classe A - público)
- LGPD: Biometria é dado biométrico (Classe C) — respeitar consentimento
- Referência: docs/SECURITY_AND_PRIVACY.md
- Notação: Documentar que biometria é opcional, nunca obrigatória

---

## Instruções para Agente

1. Carregue Skills: sertaodigital-core
2. Consulte SOURCE_OF_TRUTH.md
3. Acesse Google Drive (requer acesso):
   - SERTÃO DIGITAL/.../04_DOCUMENTACAO_DE_PRODUTOS/legislagd_manuals
4. Identificar documento master
5. Adicionar seção de autenticação biométrica
6. Atualizar índice/sumário
7. Incrementar versão do documento
8. Adicionar data de revisão
9. Notificar RH e gestores conforme procedimento

---

## Fontes Consultadas

- GitHub PR #89 (implementação técnica)
- docs/SDKA.md (princípios)
- docs/SECURITY_AND_PRIVACY.md (LGPD)
- skills/legislagd/SKILL.md

---

## Decisões Pendentes

- [ ] Texto para consentimento de biometria — sugerir padrão LGPD?

```

---

## Ciclo de Vida de um Handoff

```
PENDING
    ↓
    | (agente recebe e começa)
    v
IN_PROGRESS
    ↓
    | (mudança implementada)
    v
COMPLETED
    ↓
    | (ou cancelado se necessário)
    v
[CANCELLED]
```

---

## Registro de Handoffs

Handoffs podem ser:

1. **Documentados em issue do GitHub** (com tag `handoff`)
2. **Documentados em comentário de PR**
3. **Armazenados em docs/handoffs/** (se volume alto)
4. **Referenciados em PENDING_SYNC (ver abaixo)**

---

## PENDING_SYNC Registry

Quando um Prompt Handoff é criado mas ainda não executado, registre em:

**Status:** PENDING_SYNC

```yaml
pending_syncs:
  - handoff_id: 2026-08-15-TECHNICAL-001
    origin_layer: functional
    target_layer: technical
    product: legislagd
    date_created: 2026-08-15
    status: PENDING
    assigned_to: [agente, team, null]
    expected_completion: 2026-08-22
    criticality: HIGH | MEDIUM | LOW
    blocking: true | false
```

Esta será documentada em:
- GitHub: em issue com tag `pending-sync`
- Ou em SDKA manifesto (futuro)

---

## Validação de Handoff

Checklist para revisor:

- ✅ handoff_id único e datado
- ✅ origin_layer e target_layer claros
- ✅ Mudança é específica e acionável
- ✅ Impacto cruzado identificado
- ✅ Critérios de validação são verificáveis
- ✅ Segurança/LGPD considerado
- ✅ Sem secrets expostos
- ✅ Instruções são claras
- ✅ Fonte consultada é autoritative
- ✅ Formato segue template

Se tudo OK: ✅ Pronto para execução

Se há problemas: 🔄 Revise antes de entregar ao agente executor

---

## Notas de Implementação

### Para Agentes GitHub (com acesso ao repo)

Se você identificar mudança necessária em Drive:
- Gere TECHNICAL HANDOFF
- Abra issue com tag `handoff:technical`
- Ou crie PR com referência ao handoff

### Para Agentes Drive (sem acesso a GitHub)

Se você identificar mudança necessária em GitHub:
- Gere FUNCTIONAL HANDOFF (ou TECHNICAL se souber técnico)
- Documente em comentário de Drive ou issue pública
- Referencie em issue de GitHub se possível

### Status

Tracking de handoff:

- **PENDING** — Criado, aguardando executor
- **IN_PROGRESS** — Executor começou
- **COMPLETED** — Mudança foi executada e validada
- **CANCELLED** — Necessidade deixou de existir ou foi rejeitada

---

**Versão:** 1.0.0  
**Última atualização:** 2026-08-15
