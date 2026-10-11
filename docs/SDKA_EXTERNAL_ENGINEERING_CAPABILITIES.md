# SDKA — Capacidades externas de engenharia (proposta experimental)

**Status:** proposta para revisão; não é decisão aprovada nem integração operacional.  
**Issue:** #25  
**Data:** 2026-10-09

## Objetivo

Investigar a adoção seletiva de padrões de [API Anything](https://github.com/goodnight000/api-anything) e [Replica Skill](https://github.com/Jakeschincariol/replica-skill) na SDKA, sem duplicar domínios existentes ou tornar agentes dependentes de um fornecedor.

## Inventário mínimo verificado

- `AGENTS.md` exige leitura de `docs/SOURCE_OF_TRUTH.md`, Skill apropriada, Technical Decision Gate, issue, ADR, PR e análise de impacto cruzado.
- `docs/SDKA.md` descreve Knowledge Registry, Skills, Functional Bridge e agentes.
- `docs/SKILL_ARCHITECTURE.md` define a convenção de `SKILL.md`, dependências e workflows.
- `skills/` contém `sertaodigital-core`, `legislagd` e `observatorio-mandacaru`.
- `knowledge.yaml` cataloga os três domínios.
- Esta avaliação não confirma instalação, execução, segurança ou compatibilidade runtime dos projetos de referência.

## Matriz de oportunidades

| Capacidade desejada | Referência de estudo | SDKA atual | Proposta | Prioridade |
| --- | --- | --- | --- | --- |
| Descoberta observacional de interações HTTP | API Anything | Não identificada como Skill independente | Adaptador opcional, limitado a fontes autorizadas | P2 |
| Contrato de conectores e proveniência | API Anything | Manifestos de fontes e regras de autoridade existentes | Contrato complementar sem substituir `sources.yaml` | P1 |
| Monitoramento de alteração de endpoints | API Anything | Não verificado | Health check read-only com alerta e revisão humana | P3 |
| Reconhecimento e inventário funcional | Replica Skill | Skills de contexto de domínio | Workflow técnico reutilizável | P1 |
| Comparação de lacunas entre sistemas | Replica Skill | Governança e decisões existentes | Relatório com evidências, confiança e pendências | P1 |
| Revisão de arquitetura | Replica Skill | Technical Decision Gate existente | Complementar gate; jamais substituí-lo | P1 |
| Testes funcionais orientados a evidências | Replica Skill | Política geral de validação | Critérios explícitos de verificação em ambiente controlado | P2 |
| Estratégia de produto e concorrência | Replica Skill | Autoridade comercial/funcional no Drive | Handoff funcional, sem declarar fato não verificado | P3 |

## Contrato conceitual de operação

O contrato abaixo é **exemplo proposto**, não manifesto implementado:

```yaml
id: public-catalog-read
source_id: source-registered-in-sources-yaml
purpose: "Verificar catálogo público documentado"
owner: responsible-team
scope:
  allowed_hosts: ["example.org"]
  allowed_paths: ["/api/catalog"]
  methods: ["GET"]
authorization:
  basis: publicly_documented_and_permitted
  approved_by: null
  reviewed_at: null
execution:
  mode: dry_run
  read_only: true
  timeout_seconds: 10
  max_requests: 10
evidence:
  source_url: "https://example.org/api-docs"
  captured_at: null
  redaction_required: true
verification:
  required: true
  expected_status: 200
  last_checked_at: null
provenance:
  master_domain: technical
  registry_reference: sources.yaml
```

Nenhuma operação deve ser executada enquanto `approved_by` não estiver autorizado quando exigido; `dry_run` é o padrão, e os limites não são autorização implícita. Proibir tokens em payloads de evidência, bypass de autenticação, coleta de dados pessoais desnecessários, replay autenticado sem autorização e métodos mutáveis por padrão.

## Arquitetura proposta

1. **Contexto**: `sertaodigital-core` e Skill do produto continuam definindo escopo e precedência.
2. **Planejamento**: `sdka-engineering-intelligence` descreve reconhecimento, análise de diferenças, testes e gate de decisão.
3. **Adaptadores opcionais**: componentes futuros podem oferecer descoberta/execução de operações HTTP; isolados do Functional Bridge e sem compartilhar segredos.
4. **Evidências**: saídas descrevem origem, data de coleta, escopo, limitações e grau de confiança.
5. **Governança**: alteração arquitetural exige issue + ADR + PR + revisão; alterações com efeito funcional usam Cross-Layer Impact Check.

## Critérios de aceite da fase experimental

- [ ] Ausência de dependência exclusiva de Claude, Codex ou Copilot.
- [ ] Nenhum código de terceiros copiado sem inventário de licença e notices.
- [ ] Nenhuma alteração no `sources.yaml` ou `knowledge.yaml` antes de aprovar escopo e validar schema.
- [ ] Reconhecimento e comparação funcionam a partir de artefatos públicos/localmente fornecidos sem acessar sistemas não autorizados.
- [ ] Relatórios separam **observado**, **inferido** e **não verificado**.
- [ ] Automação externa começa em dry-run/read-only; escrita é explicitamente autorizada e revisada.
- [ ] Todo impacto funcional é avaliado contra o MASTER do Drive e, quando necessário, convertido em handoff.
- [ ] Testes automatizados e documentação adicional serão definidos antes de qualquer código runtime.

## Próximas issues após avaliação

1. Especificar schema de `connector-operation`, sem duplicar `sources.yaml`.
2. Criar fixture de testes com API pública simulada e contrato de aprovação.
3. Testar workflow `recon → gap → validation` em um produto com evidências já autorizadas.
4. Medir custo, manutenção, fragilidade de endpoints e riscos de segurança por adaptador.
