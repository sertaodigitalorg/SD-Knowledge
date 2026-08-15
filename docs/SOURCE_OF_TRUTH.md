# Source of Truth

Hierarquia de autoridade para resolver conflitos de informação.

---

## Princípio Central

Quando múltiplas fontes reportam informações diferentes:

**Use esta ordem de precedência:**

1. **Documento oficial vigente** — Decisão formal, assinada, em Drive
2. **Documentação funcional oficial** — Google Drive, decisões estabelecidas
3. **Documentação técnica** — GitHub, este repo, código comentado
4. **Manifestos SDKA** — knowledge.yaml, products.yaml, repositories.yaml
5. **Knowledge Base derivada** — Markdown exportado, contexto compilado
6. **Inferência do agente** — NUNCA, a menos que nenhuma das acima aplique

---

## Tabela de Source of Truth por Tipo

| Informação | Master | Derivado | Notas |
|---|---|---|---|
| **Decisão estratégica** | Drive (doc oficial) | Markdown (ref) | Sempre assinada no Drive |
| **Documentação funcional** | Drive | Markdown (ref) | Drive é autoridade |
| **Processo de negócio** | Drive | GitHub docs (ref) | Validar no Drive |
| **Política organizacional** | Drive | GitHub docs (ref) | Decisão formal em Drive |
| **Arquitetura técnica** | GitHub | Drive (opcional) | GitHub é master técnico |
| **Código** | GitHub | — | Histórico git é autoridade |
| **API Specification** | GitHub | — | Versionado com código |
| **Deploy e CI/CD** | GitHub | — | Workflows são código |
| **ADR (Decision Records)** | GitHub | — | Com histórico git |
| **Skills** | GitHub (repo) | — | Versionado e auditável |
| **Manifesto de Produtos** | GitHub/SDKA | Drive (opcional) | YAML é source |
| **Catálogo de Repositórios** | GitHub/SDKA | — | repositories.yaml é source |
| **Index de Conhecimento** | SDKA/GitHub | Drive (opcional) | knowledge.yaml é source |

---

## Detalhes por Domínio

### Institucional/Estratégico

**Master:** Google Drive `SERTÃO DIGITAL - ACERVO INSTITUCIONAL / 33_BASE_DE_CONHECIMENTO_E_SKILLS`

Inclui:
- Decisões estratégicas
- Planos de ação
- Objetivos institucionais
- Estrutura organizacional
- Políticas oficiais

**Derivado:** Markdown exportado para GitHub (referência)

**Regra:** Nunca edite Markdown exportado como se fosse master. Volte sempre ao Drive.

### Funcional/Administrativo

**Master:** Google Drive

Inclui:
- Procedimentos operacionais
- Documentação de produtos (funcional)
- Requisitos de negócio
- Guias de uso
- Dados administrativos

**Derivado:** Markdown, resumos em GitHub

**Regra:** Validar sempre contra Drive. Markdown é referência.

### Técnico/Arquitetural

**Master:** GitHub (`sertaodigitalorg/SD-Knowledge`)

Inclui:
- Arquitetura técnica (docs/)
- Skills (skills/)
- Schemas (schemas/)
- APIs
- Padrões técnicos
- Workflows de CI/CD

**Derivado:** — (GitHub é primary)

**Nota:** Pode referenciar Drive para contexto funcional.

### Conhecimento Derivado

**Status:** NÃO-AUTORATIVO

Inclui:
- Markdown exportado
- Contexto compilado para IA
- Resumos e índices
- Contexto portátil

**Regra:** Use como referência apenas. Sempre volte à fonte (1-4 acima).

---

## Quando Há Conflito

**Cenário:** Você encontra informações contraditórias.

**Processo:**

1. Identifique as duas fontes
2. Aplique a hierarquia acima
3. A source de precedência mais alta é a verdade
4. Se Drive vs GitHub: confira qual é "funcional" vs "técnico"
5. Se ambas são do mesmo tipo: procure por data/versão
6. Se ainda houver dúvida: abra issue para clarificação

**Regra central:** Exemplos documentais não possuem autoridade normativa. Eles servem apenas para ilustrar fluxo e nunca substituem a decisão oficial.

**Exemplo ilustrativo — não autoritativo:**

```
Drive diz: "Sistema X pode usar identidade centralizada"
GitHub SKILL de produto diz: "Sistema X usa modelo Y"

Resolução:
- O exemplo acima é ilustrativo
- A decisão oficial deve residir em documentação formal ou ADRs do repositório
- GitHub deve refletir a fonte autorizada e não uma inferência
- Se for conflito real, abrir issue para validação
```

---

## Responsabilidades por Fonte

### Drive

- ✅ Decisões estratégicas
- ✅ Aprovações formais
- ✅ Documentação de funcionalidades
- ✅ Requisitos de negócio
- ✅ Histórico institucional

### GitHub

- ✅ Arquitetura técnica
- ✅ Código e APIs
- ✅ Padrões de desenvolvimento
- ✅ Skills (interpretação)
- ✅ Historico de decisões técnicas (ADRs)

### Compartilhado (Sync)

- 📋 Markdown exportado (ambas as direções)
- 📋 Contexto de conexão (ambas referem)
- 📋 Produtos e repositórios (YAML sync)

---

## Ciclo de Sincronização

```
Drive (Master)
    ↓
    v (Export)
Markdown em GitHub
    ↓
    | (Referência)
GitHub Docs (Técnico)
    ↓
    | (Incorpora)
SDKA Manifestos
```

**Regra:** Nunca edite Markdown como fonte. Sempre volte ao Drive original.

---

## Para Agentes de IA

Quando receber uma tarefa:

1. **Identificar tipo de informação**
   - Estratégico? → Buscar em Drive
   - Funcional? → Buscar em Drive
   - Técnico? → Buscar em GitHub
   - Derivado? → Use como referência, valide contra master

2. **Consultar fonte apropriada**
   - Se Drive: busque em Skills de contexto ou Drive diretamente
   - Se GitHub: consulte docs/, skills/, código

3. **Validar contra hierarquia**
   - Há conflitos? Aplique ordem (1-6 acima)
   - Conflitos não resolvidos? Abra issue, não invente

4. **Registrar fonte**
   - Sempre cite a source
   - Indique nível de autoridade
   - Atualize Skills se necessário

5. **Nunca inventar**
   - Se informação não existe: abra issue
   - Se precisa de novo conhecimento: propose no GitHub
   - Agente = orquestrador, não criador de verdade

---

## Exemplo: Decisão sobre LegislaGD

```
Questão: "LegislaGD vai usar Keycloak compartilhado?"

Processo:

1. Tipo: Decisão arquitetural (técnica + estratégica)

2. Buscar em:
   a. Drive → 00_GOVERNANCA ou 02_ARQUITETURA
   b. GitHub → skills/legislagd/SKILL.md

3. Encontrado em Drive:
   "Decisão: Keycloak separado por Poder. Legislativo tem seu Keycloak.
    Executivo terá separado (futuro). Federação quando necessário."
   
4. GitHub SKILL diz:
   "Keycloak Legislativo — identidade central para LegislaGD.
    Legislativo terá seu próprio Keycloak. Executivo — separado (futuro)."

5. Validação:
   - Drive é document oficial (precedência 1)
   - GitHub SKILL reflete Drive (correto, alinhado)
   - Não há conflito

6. Decisão:
   "Keycloak separado, conforme documento Drive de 2026-08-15"
```

---

## Sincronização Bidirecional

Quando uma mudança em uma camada impacta a outra:

### Regra Fundamental

**Quem executa uma mudança é responsável por avaliar impacto na outra camada.**

Quando houver impacto cruzado:

1. **COM acesso à camada impactada:**
   - ✅ Atualizar diretamente na mesma atividade
   - Respeitar governança, fonte de verdade, classificação
   - Sincronizar versão e data

2. **SEM acesso à camada impactada:**
   - ✅ Gerar **Prompt Handoff** obrigatoriamente
   - Documentar em issue com tag `handoff`
   - Registrar em **PENDING_SYNC**
   - Ausência de acesso NÃO elimina responsabilidade

**Nenhuma mudança deverá deixar conscientemente as duas camadas em estado divergente.**

### Fluxo Funcional → Técnico

**Origem:** Google Drive (decisão, requisito, mudança de negócio)  
**Detecção:** Agente identifica impacto técnico  
**Ação com acesso:** Atualizar código, documentação técnica, Skills  
**Ação sem acesso:** TECHNICAL HANDOFF para agente GitHub  

**Exemplos:**
- Novo requisito → novo componente técnico
- Mudança de fluxo operacional → alteração de API
- Nova política de segurança → atualização de autenticação

### Fluxo Técnico → Funcional

**Origem:** GitHub (código, API, arquitetura)  
**Detecção:** Agente identifica impacto em funcionamento percebido  
**Ação com acesso:** Atualizar documentação no Drive, manuais, guias  
**Ação sem acesso:** FUNCTIONAL HANDOFF para agente Drive  

**Exemplos:**
- Novo endpoint de API → documentação de uso
- Mudança de autenticação → manual operacional
- Depreciação de funcionalidade → avisos em Drive

### Access-Aware Handoff

```
if cross_layer_impact == false:
    finish()

if target_layer_access == true:
    update_target_layer()
    validate_cross_layer_consistency()
else:
    generate_prompt_handoff()
    register_pending_sync()
```

**Princípio:** Acesso determina mecanismo, não necessidade.

### PENDING_SYNC Status

Quando não for possível atualizar imediatamente a outra camada:

Registre:
- Camada de origem e destino
- Produto afetado
- Motivo e contexto
- Data de criação
- Responsável (quando conhecido)
- Prompt Handoff completo
- Fontes afetadas
- Criticidade (HIGH / MEDIUM / LOW)
- Status (PENDING / IN_PROGRESS / COMPLETED / CANCELLED)

**Exemplo:**

```yaml
pending_sync:
  - handoff_id: 2026-08-15-TECHNICAL-001
    origin_layer: functional
    target_layer: technical
    product: legislagd
    date_created: 2026-08-15
    status: PENDING
    criticality: HIGH
    blocking_merge: false
```

**Referência:** `docs/PROMPT_HANDOFF_STANDARD.md`

---

## Mantendo a Hierarquia com Sincronização

Para manter SOURCE_OF_TRUTH mesmo com mudanças bidirecional:

- ✅ Sempre identifique qual camada é MASTER para aquela informação
- ✅ Mantenha referência cruzada entre camadas
- ✅ Quando Drive muda: GitHub deve refletir (se impacto técnico)
- ✅ Quando GitHub muda: Drive deve refletir (se impacto funcional)
- ✅ Sempre cite a fonte original
- ✅ Evite duplicação de decisões (sempre aponte ao master)
- ✅ Use manifests (YAML) para registros estruturados de sincronização

**Não é conflito quando:**
- Drive e GitHub referem a mesma verdade de forma diferente
- Markdown derivado está atualizado
- Ambas as camadas foram sincronizadas consciosamente

**É conflito quando:**
- Informação é diferente entre camadas
- Uma camada tem versão mais nova
- Não há razão explicável para divergência

**Resolução:**
- Aplicar hierarquia de SOURCE_OF_TRUTH (Drive antes para funcional, GitHub antes para técnico)
- Se ambas são do mesmo tipo: usar mais recente (por data/versão)
- Sincronizar para estado consistente

---

**Versão:** 1.0.0  
**Última atualização:** 2026-08-15
