# Integração com Google Drive

Como SDKA conecta com o Acervo Institucional do Sertão Digital.

---

## Estrutura de Drive

### Localização Oficial

```
SERTÃO DIGITAL - ACERVO INSTITUCIONAL
└── 33_BASE_DE_CONHECIMENTO_E_SKILLS
    ├── 00_GOVERNANCA
    │   ├── Decisões estratégicas
    │   ├── Políticas organizacionais
    │   └── Aprovações
    │
    ├── 01_BASE_DE_CONHECIMENTO_INSTITUCIONAL
    │   ├── Organização
    │   ├── Produtos e linhas
    │   ├── Estrutura operacional
    │   └── Histórico
    │
    ├── 02_ARQUITETURA_DE_CONHECIMENTO
    │   ├── Análise arquitetural
    │   ├── Integração de sistemas
    │   ├── Roadmap técnico
    │   └── Estudos de viabilidade
    │
    ├── 03_MAPA_DE_FONTES
    │   ├── Registro de autoridades
    │   ├── Relacionamento entre fontes
    │   ├── Matriz de responsabilidades
    │   └── Índices de conteúdo
    │
    ├── 04_DOCUMENTACAO_DE_PRODUTOS
    │   ├── [Produto 1]/
    │   ├── [Produto 2]/
    │   └── [...]
    │
    ├── 05_EXPORTACOES_MD
    │   ├── Contexto para IA
    │   ├── Markdown derivado
    │   └── Snapshots de conhecimento
    │
    └── 99_HISTORICO
        ├── Versões antigas
        ├── Discussões resolvidas
        └── Rascunhos
```

**Nota:** A numeração `33` é intencional e identitária, representando convergência de conhecimento.

---

## Sincronização Drive → GitHub

### Fluxo

```
Drive (Master)
    ↓
    | (Export)
Markdown / YAML
    ↓
GitHub Repository
(Referência, nunca edit)
    ↓
SDKA Manifestos
(knowledge.yaml, etc)
```

### Quando Exportar

- [ ] Após aprovação de decisão em Drive
- [ ] Após atualização de documentação funcional
- [ ] Após mudança de política
- [ ] Periodicamente (quinzenal/mensal)

### Como Exportar

**Manual:**
1. Selecionar conteúdo no Drive
2. Exportar como Markdown ou PDF
3. Converter para Markdown se necessário
4. Criar branch `docs/export-YYYY-MM-DD`
5. Adicionar em `docs/` ou `skills/*/references/`
6. Criar PR documentando origem
7. Merge

**Automático (Futuro):**
- Webhook de Drive → GitHub
- Conversão automática
- Branch e PR automáticos
- Notificação de conflitos

### Estrutura de Referência

```
# Documento Exportado

> **Origem:** Google Drive — 33_BASE_DE_CONHECIMENTO_E_SKILLS / [Pasta]
> **Data:** YYYY-MM-DD
> **Status:** Referência (master em Drive)
> **Último update Drive:** YYYY-MM-DD

[Conteúdo do documento]

---

**Aviso:** Este é um documento derivado. Sempre consulte a versão original em Drive.
```

---

## Sincronização GitHub → Drive

### Quando Sincronizar

- Skills documentadas em GitHub
- Decisões técnicas (ADRs)
- Contexto arquitetural importante
- Mudanças de grande impacto

### Como Sincronizar

**Manual:**
1. Preparar resumo de GitHub
2. Criar documento em Drive
3. Linkar de volta ao GitHub
4. Registrar em `sources.yaml`

**Automático (Futuro):**
- Export context ferramenta
- Geração de Markdown para Drive
- Link tracking automático

---

## Evitar Duplicação

### Regra: Uma Fonte, Uma Verdade

```
❌ ERRADO: Editar Markdown em GitHub e tratá-lo como master
❌ ERRADO: Ter mesma info em Drive E GitHub com versões diferentes
❌ ERRADO: Perder histórico de qual é original

✅ CERTO: Drive = Master, GitHub = Referência
✅ CERTO: Editar sempre no master
✅ CERTO: Atualizar referência quando master muda
```

### Como Validar

- [ ] Documentação técnica → Está em GitHub?
- [ ] Documentação funcional → Está em Drive?
- [ ] Há duplicatas com versões diferentes? → Alinhar com Drive
- [ ] Referência em GitHub aponta para Drive? → Adicionar link
- [ ] Markdown é derivado? → Marcar como "Reference only"

---

## Campos de Manifesto para Referência Drive

No `knowledge.yaml`, `products.yaml`, etc:

```yaml
product:
  name: LegislaGD
  drive_reference: "SERTÃO DIGITAL - ACERVO / 33... / 04_DOCUMENTACAO_DE_PRODUTOS / LegislaGD"
  drive_sync_date: "2026-08-15"
  status: "synced"
  
repository:
  github: "sertaodigitalorg/LegislaGD"
  drive_reference: null (ou link se houver doc no Drive)
```

---

## Rastreamento de Sincronização

### Checklist de Sincronização

Quando exportar/sincronizar:

- [ ] Identificar fonte original (Drive ou GitHub)
- [ ] Identificar conteúdo (qual informação)
- [ ] Validar data e versão
- [ ] Criar branch com nome descritivo
- [ ] Adicionar em local apropriado (docs/ ou skills/)
- [ ] Incluir header com origem
- [ ] Criar PR com descrição
- [ ] Revisar para conflitos
- [ ] Merge e atualizar manifesto
- [ ] Registrar em `sources.yaml` se novo

---

## Perguntas Frequentes

### P: Posso editar Markdown em GitHub?

**R:** Apenas se for documento novo. Se é cópia do Drive, nunca edite no GitHub — edite no Drive e resync.

### P: Como reportar conflito entre Drive e GitHub?

**R:** Abra issue em GitHub descrevendo conflito. Tag `documentation`. Resolva sempre em favor de source of truth hierarquia.

### P: Como citar Drive em PR?

**R:**
```
Relacionado a Drive: SERTÃO DIGITAL - ACERVO / 33... / [Pasta]
Data: YYYY-MM-DD
Tipo: Funcional / Estratégico / Arquiteural
```

### P: Com que frequência sincronizar?

**R:** Quinzenalmente (2 semanas) ou quando há mudança significativa em Drive. Futuro: webhook contínuo.

---

## Ferramentas de Suporte (Futuro)

Planejado para Fase 2:

- [ ] Google Drive → Markdown exporter automático
- [ ] Comparador Drive/GitHub (detecção de conflitos)
- [ ] Webhook Drive → GitHub
- [ ] Validador de referências cruzadas
- [ ] Gerador de contexto para IA

---

**Versão:** 1.0.0  
**Última atualização:** 2026-08-15
