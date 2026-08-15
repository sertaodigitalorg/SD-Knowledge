# SDKA - Especificação Formal

## Definição

**SDKA** (Sertão Digital Knowledge Architecture) é a camada técnica centralizada para:

- Conhecimento institucional e arquitetural
- Skills (camada de interpretação de domínios)
- Agentes de IA (orquestração)
- Manifestos (catálogo de produtos, repositórios, fontes)
- Validação e governança

---

## Princípios Fundamentais

### 1. Duas Fontes de Verdade

```
Google Drive (Master Institucional/Funcional)
    ↓
    └→ Markdown Exportado (Referência)
    
GitHub (Master Técnico)
    ↓
    └→ Skills, Código, Arquitetura
    
Convergência através de Manifestos (SDKA)
```

**Regra:** Nunca edite uma cópia derivada como se fosse master.

### 2. Hierarquia de Autoridade

Quando resolver conflitos:

1. Documento oficial vigente (Drive, assinado)
2. Documentação funcional oficial (Drive)
3. Documentação técnica (GitHub)
4. Manifestos SDKA (knowledge.yaml, etc)
5. Knowledge Base derivada (Markdown exportado)
6. Inferência de agente (nunca substitua 1-5)

**Implicação:** Agentes nunca inventam informação funcional/arquitetural.

### 3. Skills como Interpretação

Uma Skill encapsula:

- Contexto de domínio (conceitos, vocabulário)
- Regras de interpretação (como agentes devem entender)
- Dependências (outras Skills necessárias)
- Workflows (processos padrão)

Exemplo: `sertaodigital-core` Skill fornece contexto institucional.

### 4. Manifestos como Catalogo

Manifestos (YAML) registram:

- Produtos e componentes
- Repositórios e URLs
- Fontes e autoridades
- Conhecimento e versões

Manifestos são **máquina-legível** e versionados.

### 5. Agentes como Orquestradores

Agentes de IA:

- Carregam AGENTS.md (bootstrap)
- Consultam Skills relevantes
- Validam contra SOURCE_OF_TRUTH.md
- Executam tarefas respeitando hierarquia
- Registram mudanças de arquitetura

**Nunca quebram compatibilidade sem discussão.**

### 6. Sincronização Bidirecional

A SDKA não é unidirecional Drive → GitHub.

**Mudanças em uma camada devem sincronizar na outra:**

**Camada Funcional (Drive) ↔ Camada Técnica (GitHub)**

- Quando mudança funcional impacta técnico: atualizar GitHub (ou Prompt Handoff)
- Quando mudança técnica impacta funcional: atualizar Drive (ou Prompt Handoff)

**Regra:** Quem executa a mudança é responsável por sincronizar.

- ✅ Com acesso: atualizar direto
- ✅ Sem acesso: gerar Prompt Handoff

**Nenhuma mudança deixará conscientemente as camadas divergentes.**

Veja `docs/PROMPT_HANDOFF_STANDARD.md` e `docs/TECHNICAL_DECISION_GOVERNANCE.md`.

---


```
┌─────────────────────────────────────┐
│      Fonte Institucional            │
│     Google Drive (Master)           │
│                                     │
│  - Estratégia                       │
│  - Decisões assinadas               │
│  - Documentação funcional           │
│  - Administrativo e jurídico        │
└─────────────────┬───────────────────┘
                  │
                  │ (referência)
                  v
        ┌─────────────────────┐
        │  Markdown Exportado  │
        │   (Derivado - Ref)   │
        └─────────────────────┘
                  │
                  │ (sincroniza)
                  v
    ┌─────────────────────────────┐
    │   SDKA (GitHub)             │
    │   - manifestos (YAML)       │
    │   - schemas (JSON)          │
    │   - Skills (Markdown)       │
    │   - Documentação técnica    │
    │   - Código                  │
    └──────────┬──────────────────┘
               │
    ┌──────────┴───────────┐
    │                      │
    v                      v
┌──────────────┐   ┌──────────────────┐
│  Skills      │   │  Documentação    │
│              │   │  Técnica         │
│- Core        │   │                  │
│- Produtos    │   │- APIs            │
│- Domínios    │   │- Arquitetura     │
│- Workflows   │   │- ADRs            │
└──────────────┘   └──────────────────┘
       │                    │
       └────────┬───────────┘
                v
          ┌──────────────┐
          │   Agents     │
          │   (Orquestração
          │   de IA)     │
          └──────────────┘
                 │
                 v
     ┌──────────────────────┐
     │  Desenvolvimento     │
     │  Cidadão / IA        │
     └──────────────────────┘
```

---

## Componentes

### Knowledge Registry (Este Repo)

Índice centralizado com:

- `knowledge.yaml` — Catálogo de Skills e conhecimento
- `sources.yaml` — Registro de autoridades
- `products.yaml` — Catálogo de produtos
- `repositories.yaml` — Catálogo de repositórios
- `governance.yaml` — Políticas

### Skills

Interpretação de domínios:

```
skills/
├── sertaodigital-core/
│   ├── SKILL.md (Especificação)
│   ├── references/ (Conteúdo de domínio)
│   ├── manifests/ (Registros)
│   └── workflows/ (Processos)
├── legislagd/
│   ├── SKILL.md
│   ├── references/
│   ├── manifests/
│   └── workflows/
└── [others]/
```

### Schemas

Validação estruturada:

```
schemas/
├── knowledge.schema.json
├── sources.schema.json
├── products.schema.json
├── repositories.schema.json
└── skill.schema.json
```

### Documentação Técnica

Especificações e guias:

```
docs/
├── SDKA.md (Este arquivo)
├── SOURCE_OF_TRUTH.md
├── DOCUMENTATION_ARCHITECTURE.md
├── SKILL_ARCHITECTURE.md
├── AGENT_ARCHITECTURE.md
├── DRIVE_INTEGRATION.md
├── PRODUCT_KNOWLEDGE_STANDARD.md
├── CONTEXT_EXPORT_STANDARD.md
├── SECURITY_AND_PRIVACY.md
└── NEXT_STEPS.md
```

### Agentes

Bootstrap de contexto:

```
AGENTS.md — Instruções centrais para agentes de IA
```

---

## Fluxos

### Fluxo de Novo Conhecimento

```
Necessidade → Issue → Proposta → Skill/Manifesto → PR → Review → Merge
```

### Fluxo de Sincronização Drive-GitHub

```
Drive (Master) → Export Markdown → GitHub (Referência)
```

**Nota:** Exportação é derivada. Nunca edit Markdown e trate como master.

### Fluxo de Decisão Arquitetural

```
Issue → Discussão → Proposta + ADR → Review → Decisão → Implementação
```

### Fluxo de Agente

```
Tarefa → Carrega AGENTS.md → Consulta Skills → Valida contra SOURCE_OF_TRUTH → Executa → Registra
```

---

## Versionamento

Toda SDKA segue Semantic Versioning:

- **MAJOR:** Quebra de compatibilidade, mudança estrutural
- **MINOR:** Novas Skills, novos produtos (compatível)
- **PATCH:** Correções, atualizações menores

Versão atual: `1.0.0`

Mudanças documentadas em `CHANGELOG.md`.

---

## Segurança

**Nunca expor em repositório público:**

- Tokens, senhas, secrets
- Chaves privadas
- Credenciais de API
- Dados pessoais (PII)
- Informações sensíveis

Use `.gitignore` e validação automática.

Veja `SECURITY.md`.

---

## Conformidade

- **LGPD** (Lei Geral de Proteção de Dados)
- **Transparência** — histórico auditável
- **Abertura** — código público quando possível
- **Soberania** — preferência por software livre

---

## Próximos Passos

Veja `docs/NEXT_STEPS.md` para roadmap.

Fases:

1. **Fase 1 (Atual)** — Estrutura SDKA + Skills core
2. **Fase 2** — Integração Drive, Skills adicionais, Exportação
3. **Fase 3** — Registry global, IA avançada, Análise de impacto

---

**Versão:** 1.0.0  
**Última atualização:** 2026-08-15
