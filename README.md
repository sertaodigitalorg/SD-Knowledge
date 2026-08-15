# SD-Knowledge

**Arquitetura de Conhecimento, Skills e Agents do Sertão Digital**

---

## O que é a SDKA?

A **SDKA** (Sertão Digital Knowledge Architecture) é a camada técnica canônica para conhecimento, skills, agentes de IA e documentação arquitetural do Centro de Inovação e Tecnologia Sertão Digital.

A SDKA estabelece:

- **Skills** — camada de interpretação, regras de contexto e conhecimento de domínio
- **Agents** — orquestração de IA baseada em Skills
- **Manifestos** — registro centralizado de produtos, repositórios e fontes
- **Source of Truth** — hierarquia clara entre Google Drive (institucional) e GitHub (técnico)
- **Schemas** — validação e versionamento de conhecimento
- **Workflows** — automação para integração e sincronização

## Princípio Central: Duas Fontes de Verdade

```
┌─────────────────────────────────────────────────────┐
│           SERTÃO DIGITAL - ACERVO                   │
│     BASE_DE_CONHECIMENTO_E_SKILLS (Drive)           │
│                                                     │
│  - Documentação funcional                           │
│  - Documentação estratégica                         │
│  - Documentação administrativa                      │
│  - Decisões institucional/jurídicas                 │
│  - Materiais para usuários não-técnicos             │
└──────────────────┬──────────────────────────────────┘
                   │ Master Funcional
                   │
                   v
        ┌──────────────────────┐
        │   Knowledge Index    │
        │  (GitHub / SDKA)     │
        │  - Schema validation │
        │  - Skills registry   │
        │  - Product manifest  │
        └──────────┬───────────┘
                   │
        ┌──────────┴──────────┐
        │                     │
        v                     v
    ┌────────────┐      ┌────────────────┐
    │   Docs     │      │   Skills       │
    │ (Technical)│      │(Implementation)│
    │            │      │                │
    │- Architecture      │- Interpretation│
    │- APIs      │      │- Context Rules │
    │- Deploy    │      │- Dependencies  │
    │- ADRs      │      │- Workflows     │
    └─────┬──────┘      └────────┬───────┘
          │                      │
          └──────────┬───────────┘
                     │
                     v
            ┌─────────────────┐
            │     Agents      │
            │  (Orchestration)│
            │                 │
            │- AI workflows   │
            │- Tool integration
            │- Reasoning      │
            └────────┬────────┘
                     │
                     v
         ┌─────────────────────────────┐
         │   Desenvolvimento / IA       │
         │  Consumidores de Contexto    │
         └─────────────────────────────┘
```

## Structure

```
SD-Knowledge/
├── README.md                          # Você está aqui
├── AGENTS.md                          # Bootstrap central de Agents
├── VERSION                            # Versionamento semântico
├── CHANGELOG.md                       # Histórico de mudanças
├── LICENSE                            # Licença (em definição)
├── CONTRIBUTING.md                    # Guia de contribuição
├── SECURITY.md                        # Política de segurança
├── CODE_OF_CONDUCT.md                 # Código de conduta
├── .gitignore
│
├── knowledge.yaml                     # Índice de conhecimento
├── sources.yaml                       # Registro de fontes
├── products.yaml                      # Catálogo de produtos
├── repositories.yaml                  # Catálogo de repositórios
├── governance.yaml                    # Políticas de governança
│
├── docs/                              # Documentação técnica
│   ├── README.md
│   ├── SDKA.md                        # Especificação formal
│   ├── SOURCE_OF_TRUTH.md             # Hierarquia de fontes
│   ├── KNOWLEDGE_GOVERNANCE.md
│   ├── DOCUMENTATION_ARCHITECTURE.md
│   ├── SKILL_ARCHITECTURE.md
│   ├── AGENT_ARCHITECTURE.md
│   ├── DRIVE_INTEGRATION.md
│   ├── PRODUCT_KNOWLEDGE_STANDARD.md
│   ├── CONTEXT_EXPORT_STANDARD.md
│   ├── SECURITY_AND_PRIVACY.md
│   ├── LICENSE_DECISION.md
│   └── NEXT_STEPS.md
│
├── skills/                            # Skills de conhecimento
│   ├── README.md
│   ├── sertaodigital-core/
│   │   ├── SKILL.md                   # Especificação da Skill
│   │   ├── references/
│   │   │   ├── organization.md
│   │   │   ├── governance.md
│   │   │   ├── documentation.md
│   │   │   ├── architecture.md
│   │   │   ├── products.md
│   │   │   └── security.md
│   │   ├── manifests/
│   │   │   └── sources.yaml
│   │   └── workflows/
│   │       ├── documentation-review.md
│   │       └── source-validation.md
│   │
│   └── legislagd/
│       ├── SKILL.md
│       ├── references/
│       │   ├── domain.md
│       │   ├── architecture.md
│       │   ├── integrations.md
│       │   ├── identity.md
│       │   ├── sapl.md
│       │   ├── portalmodelo.md
│       │   ├── ecidade.md
│       │   └── sigi.md
│       ├── manifests/
│       │   ├── product.yaml
│       │   ├── repositories.yaml
│       │   └── sources.yaml
│       └── workflows/
│           ├── new-feature.md
│           ├── bug-fix.md
│           ├── integration-change.md
│           ├── architecture-change.md
│           └── documentation-update.md
│
├── schemas/                           # Validação JSON Schema
│   ├── knowledge.schema.json
│   ├── sources.schema.json
│   ├── products.schema.json
│   ├── repositories.schema.json
│   └── skill.schema.json
│
├── tools/
│   ├── README.md
│   ├── validate/
│   └── export-context/
│
├── examples/
│   ├── AGENTS.example.md
│   ├── knowledge.example.yaml
│   └── product.example.yaml
│
└── .github/
    ├── workflows/
    │   ├── validate.yml
    │   └── markdown.yml
    ├── ISSUE_TEMPLATE/
    │   ├── documentation.yml
    │   ├── skill.yml
    │   └── source.yml
    └── pull_request_template.md
```

## Conceitos Fundamentais

### Skills

Uma **Skill** é uma camada de interpretação que encapsula:

- **Contexto de domínio** — conhecimento específico de um produto ou área
- **Regras de interpretação** — como agentes devem entender referências
- **Dependências** — outras Skills ou fontes necessárias
- **Workflows** — processos padrão para mudanças

Exemplo: `sertaodigital-core` é a Skill de contexto institucional.

**Quando usar:** Ao trabalhar com produtos, arquitetura, ou integrações específicas.

**Como consumir:** Veja o AGENTS.md para instruir agentes a carregar uma Skill.

### Agents

Um **Agent** é um processo de IA que:

1. Carrega o AGENTS.md
2. Consulta Skills relevantes
3. Valida decisões contra SOURCE_OF_TRUTH.md
4. Nunca inventa informações funcional/arquitetural
5. Registra mudanças quando necessário

### Source of Truth

Hierarquia de autoridade:

| Tipo | Master | Derivado |
|------|--------|----------|
| **Institucional** | Google Drive | Markdown (referência) |
| **Funcional** | Google Drive | Markdown (referência) |
| **Arquitetura Técnica** | GitHub | — |
| **APIs** | GitHub | — |
| **Skills** | GitHub | — |
| **Código** | GitHub | — |
| **Knowledge Index** | SDKA | — |

**Nunca edite uma cópia derivada como se fosse a fonte original.**

## Como Começar

### Para Desenvolvedores

1. **Entender a arquitetura:**
   ```bash
   cat docs/SDKA.md
   cat docs/SOURCE_OF_TRUTH.md
   ```

2. **Identificar a Skill necessária:**
   ```bash
   ls skills/
   cat skills/[skill-name]/SKILL.md
   ```

3. **Consultar manifestos:**
   ```bash
   cat knowledge.yaml
   cat products.yaml
   ```

### Para Contribuidores

1. Leia [CONTRIBUTING.md](CONTRIBUTING.md)
2. Abra uma issue descrevendo sua mudança
3. Crie uma branch `feature/descricao`
4. Faça suas mudanças
5. Abra um Pull Request

### Para Agentes de IA

1. Carregue o [AGENTS.md](AGENTS.md)
2. Consulte a Skill apropriada em `skills/[name]/SKILL.md`
3. Valide decisões contra [docs/SOURCE_OF_TRUTH.md](docs/SOURCE_OF_TRUTH.md)
4. Nunca invente informações funcionais
5. Use este repositório como source técnica, não substitua Google Drive

## Adicionar um Novo Produto

1. **Criar issue** com detalhes do produto
2. **Registrar em** `products.yaml`
3. **Criar um repositório** se necessário
4. **Registrar repositório** em `repositories.yaml`
5. **Criar Skill** em `skills/[product-name]/SKILL.md`
6. **Documentar arquitetura** em `skills/[product-name]/references/`

## Adicionar uma Nova Skill

1. **Criar diretório:** `skills/[skill-name]/`
2. **Criar SKILL.md** com metadados e documentação
3. **Criar estrutura:**
   ```
   skills/[skill-name]/
   ├── SKILL.md
   ├── references/
   ├── manifests/
   └── workflows/
   ```
3. **Registrar em** `knowledge.yaml`
4. **Abrir Pull Request**

## Consumir uma Skill

Ao trabalhar em um contexto específico, instrua o agente:

```yaml
# No prompt ou arquivo de contexto:
skills:
  - sertaodigital-core  # Contexto institucional
  - legislagd           # Contexto legislativo (se aplicável)
```

Agents carregarão automaticamente as Skills necessárias.

## Segurança

- ✅ Nunca commit: tokens, senhas, credentials, secrets
- ✅ Use `.gitignore` para proteger `.env` local
- ✅ Validação automática detecta padrões comuns
- ✅ Reporte vulnerabilidades nos canais institucionais oficiais

Veja [SECURITY.md](SECURITY.md).

## Licença

Licença em definição. Veja [docs/LICENSE_DECISION.md](docs/LICENSE_DECISION.md).

Enquanto isso:
- Você pode ler e estudar o conteúdo
- Contribuições seguem [CONTRIBUTING.md](CONTRIBUTING.md)
- Nenhuma secret deve ser exposta

## Informações de Contato

Para questões sobre SDKA, arquitetura ou Skills:

Utilize os canais institucionais oficiais do Sertão Digital.

---

**Última atualização:** 2026-08-15  
**Versão:** 1.0.0  
**Status:** Foundational Release
