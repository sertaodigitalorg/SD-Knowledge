---
name: sdka-engineering-intelligence
description: Workflow experimental de reconhecimento funcional, análise de lacunas e validação técnica baseada em evidências.
version: 0.1.0
status: inactive
type: technical-context
---

# SDKA Engineering Intelligence (experimental)

## Propósito

Orientar agentes e desenvolvedores na produção de um diagnóstico **não invasivo**, reproduzível e auditável de funcionalidades, arquitetura observável e lacunas de implementação.

**Status:** `inactive`. Esta Skill é uma proposta de revisão da issue #25; não está registrada como ativa em `knowledge.yaml`.

## Escopo

- Inventário de funcionalidades observáveis, APIs publicamente documentadas e artefatos que o usuário autorizou examinar.
- Mapeamento de requisitos, contratos conhecidos, evidências e diferenças entre capacidades desejadas e implementadas.
- Geração de hipóteses, critérios de aceitação, testes propostos e issue de trabalho.
- NÃO executa discovery HTTP, exploração autenticada, engenharia de evasão, scraping invasivo, deploy, modificação de produção ou cópia de código de terceiros.

## Quando usar

Use no planejamento de auditorias técnicas, comparação de capacidades e preparação de testes em sistemas próprios ou autorizados. Não use para contornar autenticação, reconstruir ativos protegidos nem acessar dados pessoais fora de base legítima.

## Fontes de autoridade

1. [Source of Truth](../../docs/SOURCE_OF_TRUTH.md): MASTER por domínio.
2. [SDKA](../../docs/SDKA.md): arquitetura técnica vigente.
3. [Technical Decision Governance](../../docs/TECHNICAL_DECISION_GOVERNANCE.md): gate para alterações.
4. [Estudo de integração](../../docs/SDKA_EXTERNAL_ENGINEERING_CAPABILITIES.md): referência experimental, **não normativa**.
5. Referências externas: [API Anything](https://github.com/goodnight000/api-anything) e [Replica Skill](https://github.com/Jakeschincariol/replica-skill) — materiais de estudo, não fontes de autoridade SDKA.

## Hierarquia de autoridade

Documentação funcional e políticas institucionais no Google Drive; arquitetura e código no GitHub; manifestos na SDKA. Observações externas são evidências auxiliares. Inferências devem ser identificadas como inferências.

## Dependências

- `sertaodigital-core` (obrigatória).
- Skill específica do produto avaliado, se existente.
- Autorização explícita para examinar sistemas que não sejam públicos e autorizados.

## Como usar (workflow)

1. **Delimitar** sistema, objetivo, proprietário, autorização, escopo e ambiente.
2. **Carregar** `AGENTS.md`, Source of Truth, Core Skill, Skill do produto e ADRs pertinentes.
3. **Coletar evidências permitidas**, priorizando documentação e fixtures locais; nunca tentar superar controles de acesso.
4. **Inventariar** funcionalidades com identificadores e estado: observado, inferido ou não verificado.
5. **Comparar** com requisitos oficiais; registrar diferenças sem declarar ausência apenas por falha de descoberta.
6. **Propor validação**: casos de teste, riscos, limitações, prioridade e critérios de aceite.
7. **Encaminhar** para issue, ADR e PR após revisão humana; aplicar Cross-Layer Impact Check.

## Saída mínima

```yaml
assessment:
  product: example
  scope: approved-artifacts-only
  evidence:
    - id: E1
      source: local-approved-document
      observed_at: "2026-10-09"
      finding: "Endpoint documentado"
      confidence: observed
  gaps:
    - id: G1
      requirement: "Requisito formal identificado na fonte MASTER"
      current_state: not_verified
      evidence_refs: [E1]
      recommendation: "Validar com equipe responsável"
  security:
    external_mutations: false
    credential_capture: false
  decision: review_required
```

## Segurança e privacidade

Não registrar cookies, tokens, PII, capturas de sessão ou respostas sensíveis. Acesso público não é permissão irrestrita. Todo conector futuro deverá aplicar escopo, rate-limit, allowlist, redaction, autorização e auditoria.

## Critério de ativação

Ativar e registrar em `knowledge.yaml` somente após review do ADR, testes, validação do schema de Skills e aprovação por mantenedor.
