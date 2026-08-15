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

**Exemplo:**

```
Drive diz: "LegislaGD vai usar Keycloak compartilhado com Executivo"
GitHub SKILL legislagd.md diz: "Keycloak separado, federação futura"

Resolução:
- Ambas são funcionais/arquiteturais
- Drive é mais recente (2026-08-15)
- Drive é document oficial
- GitHub deve ser atualizado para refletir Drive
- Abrir PR para sync
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

## Mantendo a Hierarquia

Para manter SOURCE_OF_TRUTH:

- ✅ Revise PRs para garantir referências corretas
- ✅ Quando Drive muda: atualize GitHub correspondente
- ✅ Quando GitHub muda: valide contra Drive
- ✅ Procure por conflitos em CI/CD
- ✅ Documente mudanças de precedência

---

**Versão:** 1.0.0  
**Última atualização:** 2026-08-15
