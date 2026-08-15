# Skill: sertaodigital-core

---

## Metadados

| Campo | Valor |
|---|---|
| **Name** | sertaodigital-core |
| **Description** | Contexto institucional, documental e arquitetural do ecossistema Sertão Digital. |
| **Version** | 1.0.0 |
| **Status** | active |
| **Author** | Sertão Digital |
| **Type** | organizational-context |

---

## Propósito

Esta Skill fornece contexto fundamental sobre:

- **Missão e visão** do Sertão Digital
- **Governança documental** — como conhecimento é organizado e autorizado
- **Arquitetura técnica** — princípios e padrões
- **Princípios de software livre** e soberania tecnológica
- **Fontes de autoridade** — Google Drive, GitHub, documentos públicos
- **Segurança e privacidade**
- **Documentação compartilhada** vs. documentação técnica versionada

Quando trabalhar em qualquer contexto do Sertão Digital, carregue esta Skill.

---

## Escopo

Esta Skill abrange:

### Contexto Institucional
- Estrutura organizacional
- Governança
- Documentação oficial
- Decisões estratégicas

### Contexto Arquitetural
- Princípios técnicos
- Padrões de desenvolvimento
- Infraestrutura padrão
- Ferramentas preferidas

### Contexto Documental
- Estrutura de Drive
- Versionamento
- Relacionamento entre fontes
- Como evitar duplicação

### Contexto de Segurança
- Proteção de dados
- Política de secrets
- Privacidade
- Conformidade

---

## Quando Usar

✅ **Use esta Skill quando:**

- Trabalhar em qualquer produto ou componente do Sertão Digital
- Precisar entender decisões arquiteturais
- Lidar com questões de governança ou documentação
- Integrar múltiplos repositórios
- Discutir estratégia de software livre
- Trabalhar com infraestrutura
- Proteger segredos ou dados sensíveis
- Validar conformidade com padrões

❌ **Não é necessária quando:**

- Trabalhar em detalhes específicos de produtos (use Skills de produto)
- Implementar algoritmo matemático puro
- Tarefa é trivial e autodescritiva

---

## Fontes de Autoridade

### 1. Google Drive (Primary)

**Local:** `SERTÃO DIGITAL - ACERVO INSTITUCIONAL / 33_BASE_DE_CONHECIMENTO_E_SKILLS`

**Conteúdo:**
- Documentação funcional oficial
- Decisões estratégicas
- Documentação administrativa
- Documentos jurídicos

**Status:** MASTER para institucional/funcional

### 2. GitHub (This Repo + Específicos)

**Local:** `sertaodigitalorg/SD-Knowledge` (este repo)

**Conteúdo:**
- Arquitetura técnica (docs/)
- Skills (skills/)
- Schemas (schemas/)
- Workflows e automação

**Status:** MASTER para técnico

### 3. Documentos Públicos

- Políticas públicas
- Legislação aplicável
- Padrões abertos (POSIX, RFCs, etc)

**Status:** Autoridade de referência

### 4. Conhecimento Derivado

- Markdown exportado de Drive para GitHub
- Knowledge Index (este repo)
- Context derivado

**Status:** NÃO-AUTORATIVO (referência apenas)

---

## Hierarquia de Autoridade

Ao resolver conflitos, use esta ordem:

1. **Documento oficial vigente** — decisão formal, assinada
2. **Documentação funcional oficial** — Google Drive
3. **Documentação técnica** — GitHub deste repo
4. **Manifestos SDKA** — knowledge.yaml, products.yaml, etc
5. **Knowledge Base derivada** — Markdown exportado, contexto
6. **Inferência do agente** — nunca substitua (1-5)

**Regra:** Nunca invente informação que já existe em fonte oficial.

---

## Governança Documental

### Princípio Central: Duas Fontes de Verdade

| Domínio | Master | Derivado |
|---|---|---|
| **Institucional** | Google Drive | Markdown (ref) |
| **Funcional** | Google Drive | Markdown (ref) |
| **Estratégico** | Google Drive | Markdown (ref) |
| **Jurídico** | Google Drive | Referência |
| **Técnico** | GitHub | — |
| **Arquitetura** | GitHub | — |
| **Code** | GitHub | — |
| **Skills** | GitHub | — |

### Estrutura de Google Drive

```
SERTÃO DIGITAL - ACERVO INSTITUCIONAL
└── 33_BASE_DE_CONHECIMENTO_E_SKILLS
    ├── 00_GOVERNANCA
    ├── 01_BASE_DE_CONHECIMENTO_INSTITUCIONAL
    ├── 02_ARQUITETURA_DE_CONHECIMENTO
    ├── 03_MAPA_DE_FONTES
    ├── 04_DOCUMENTACAO_DE_PRODUTOS
    ├── 05_EXPORTACOES_MD
    └── 99_HISTORICO
```

**Nota:** A numeração `33` é intencional e identitária. Representa a convergência de conhecimento institucional, técnico e operacional.

### Exportações de Markdown

Markdown exportado do Drive para GitHub é **DERIVADO**:
- Use como referência apenas
- Nunca edite como fonte oficial
- Sincronize com Drive como master

---

## Software Livre e Soberania Tecnológica

### Princípios

- ✅ Preferência por software open source
- ✅ Evitar lock-in proprietário
- ✅ Código fonte versionado e auditável
- ✅ Comunidade pública quando possível
- ✅ Padrões abertos e interoperabilidade
- ✅ Reprodutibilidade e transparência

### Infraestrutura

- **Padrão preferencial:** Docker (contêinerização reproduzível)
- **Repositórios:** GitHub (público, auditável)
- **CI/CD:** GitHub Actions (nativo, open source)
- **Infraestrutura:** Kubernetes, OpenStack, ou cloud aberta
- **Bancos de dados:** PostgreSQL, MongoDB, etc
- **Linguagens:** Python, Node.js, Go, Rust (quando apropriado)

### Evitar

- ❌ Vendor lock-in desnecessário
- ❌ Sistemas proprietários sem razão forte
- ❌ Dependências não-auditáveis
- ❌ Infraestrutura opaca

---

## Documentação

### Padrão Técnico

- Documentação técnica vive junto ao código (inline, README, docs/)
- Versionada com o código
- Atualizada em PRs
- Auditável por histórico git

### Padrão Funcional

- Documentação funcional vive em Google Drive
- Disponível para usuários não-técnicos
- Assinada e versionada institucionalmente
- Pode ser exportada como Markdown para referência

### Integração

- GitHub README aponta para Drive para contexto funcional
- Drive aponta para GitHub para especificações técnicas
- Markdown exportado une ambas (sem ser fonte)
- Não há duplicação de verdade

---

## Segurança e Privacidade

### Proteção de Dados

- Nenhum dado pessoal (PII) em repositórios públicos
- Nenhuma credential, token, ou secret exposto
- .gitignore protege arquivos sensíveis
- Validação automática detecta padrões de segredos

### Privacidade

- Conform com LGPD (Lei Geral de Proteção de Dados)
- Consentimento informado para dados de cidadão
- Pseudonimização quando possível
- Direito ao esquecimento respeitado

### Vulnerabilidades

- Reporte via canais oficiais do Sertão Digital
- Não abra issues públicas para vulnerabilidades
- Política de disclosure responsável
- Veja SECURITY.md para detalhes

---

## Dependências

### Requerida

Nenhuma — esta é a Skill raiz.

### Condicional

Outras Skills podem depender desta:
- `legislagd` depende de `sertaodigital-core` para contexto institucional
- Skills de produto dependem de contexto arquitetural

---

## Como Usar Esta Skill

### Para Agentes de IA

1. Carregue este arquivo no contexto
2. Consulte as seções relevantes (instituições, arquitetura, governança)
3. Valide decisões contra "Hierarquia de Autoridade"
4. Não invente informações que já existem em Drive
5. Respeite "Duas Fontes de Verdade"

### Para Desenvolvedores

1. Leia sobre padrões de infraestrutura (Docker, GitHub, etc)
2. Conheça a estrutura de Drive para referências futuras
3. Proteja secrets conforme SECURITY.md
4. Mantenha compatibilidade com projetos existentes

### Para Documentadores

1. Saiba distinguir conteúdo funcional (Drive) vs técnico (GitHub)
2. Não duplique informação entre fontes
3. Exporte Markdown quando apropriadoUnca edite exportações como fonte

---

## Sincronização Bidirecional Entre Camadas

A SDKA implementa dois masters complementares com sincronização obrigatória:

### Camadas

**Camada Funcional/Institucional:** Google Drive (MASTER)
- Decisões estratégicas
- Documentação funcional
- Requisitos de negócio
- Procedimentos operacionais

**Camada Técnica:** GitHub (MASTER)
- Arquitetura técnica
- Código e APIs
- Skills e manifestos
- Decisões arquiteturais (ADRs)

### Regra de Sincronização

Quando uma mudança em uma camada impacta a outra:

1. **COM acesso à camada impactada:**
   - Atualizar diretamente na mesma atividade
   - Respeitar governança e fontes de verdade

2. **SEM acesso à camada impactada:**
   - Gerar **Prompt Handoff** obrigatoriamente
   - Registrar em **PENDING_SYNC**
   - Ausência de acesso NÃO elimina responsabilidade

### Fluxos Principais

**Funcional → Técnico (quando mudança em Drive afeta GitHub):**
- Requisito novo → novo componente técnico
- Mudança de fluxo → alteração de API
- Nova política → atualização de permissões

**Técnico → Funcional (quando mudança em GitHub afeta Drive):**
- Nova funcionalidade → documentação de uso
- Mudança de API → manual operacional
- Depreciação → avisos em Drive

### Responsabilidades

Quem executa uma mudança é responsável por:
1. Identificar impacto na outra camada
2. Atualizar a outra camada (se houver acesso)
3. Gerar Prompt Handoff (se não houver acesso)
4. Nunca deixar divergência consciente entre camadas

**Referência completa:** `docs/PROMPT_HANDOFF_STANDARD.md` e `docs/TECHNICAL_DECISION_GOVERNANCE.md`

---

## Referências Importantes

- `docs/SDKA.md` — Especificação formal
- `docs/SOURCE_OF_TRUTH.md` — Hierarquia de fontes
- `docs/DOCUMENTATION_ARCHITECTURE.md` — Padrão de documentação
- `docs/DRIVE_INTEGRATION.md` — Integração com Google Drive
- `SECURITY.md` — Política de segurança
- Google Drive `33_BASE_DE_CONHECIMENTO_E_SKILLS`

---

## Relacionamento com Outras Skills

- **legislagd** — Contexto legislativo específico, depende de sertaodigital-core para contexto institucional
- *Futuras Skills* — Contexto de produtos, dependerão de sertaodigital-core como base

---

## Versionamento

Quando atualizar esta Skill:

- Documente mudança em CHANGELOG.md
- Mantenha retrocompatibilidade quando possível
- Use Semantic Versioning (MAJOR.MINOR.PATCH)
- Comunique breaking changes claramente

---

## Contato / Suporte

Para questões sobre esta Skill:

- Consulte `docs/SDKA.md` para contexto arquitetural
- Verifique `skills/sertaodigital-core/references/` para tópicos específicos
- Abra issue no GitHub
- Utilize canais institucionais oficiais do Sertão Digital

---

**Versão:** 1.0.0  
**Última atualização:** 2026-08-15  
**Status:** Active
