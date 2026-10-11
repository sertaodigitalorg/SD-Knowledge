# SDKA — Fase 11: inteligência institucional baseada em evidências

**Estado:** implementação experimental **offline**, independente da Skill inativa `sdka-engineering-intelligence`.

## Objetivo e escopo

Consolidar um relatório técnico de lacunas **declaradas** no contrato `schemas/engineering-assessment.schema.json`. O utilitário verifica consistência do JSON, referências entre requisitos e evidências e correspondência entre repositório e Skill ativa nos manifestos institucionais, sem coletar informações de repositórios de produto.

## Executar

```bash
python scripts/sdka_evidence_assessment.py examples/engineering-assessment.example.json
python -m unittest discover -s scripts -p 'test_evidence_assessment.py' -v
```

Requer as dependências de validação do CI, `jsonschema==4.23.0` e `PyYAML==6.0.2`. A saída não atesta que o conteúdo das evidências seja verdadeiro ou que alguma funcionalidade esteja implementada: `verified_against_source: false`, `status: review_required` e `authorization_granted: false`.

## Produtos prioritários

- **LegislaGD:** contexto `sertaodigitalorg/LegislaGD`, Skill `legislagd`; requisitos e evidências devem vir de suas fontes MASTER.
- **Observatório Mandacaru:** contexto `sertaodigitalorg/ObservatorioMandacaru`, Skill `observatorio-mandacaru`; manter distinção entre IMPLEMENTADO, EM IMPLEMENTAÇÃO, PLANEJADO, CONCEITUAL e DESCONTINUADO.

## Salvaguardas

1. Rejeitar produto sem Skill ativa, referências ausentes, IDs duplicados e decisões que tentem aprovar automaticamente.
2. Uma lacuna marcada `met` requer evidências declaradas com confiança `observed`, mas essa classificação **não comprova** a inspeção externa.
3. Não executar requisições HTTP, ferramentas de coleta, importação de dados pessoais, alterações em sistemas, deploy ou merge.
4. Fontes funcionais/institucionais permanecem no Drive; arquitetura/código, no GitHub; a plataforma Observatório é MASTER dos dados estruturados do ecossistema.
5. Auditorias reais e conectores externos exigem ADR, escopo autorizado, decisão de segurança e trilha de revisão.

## Próximos gates

- [ ] CI validado no último commit e revisão técnica do PR.
- [ ] Definir contrato de captura segura de evidências **somente** de fontes já autorizadas, sem runtime HTTP ativado.
- [ ] Avaliar ADR-010 e governança de proveniência.
- [ ] Implantação completa automatizada antes de avaliações práticas, conforme a decisão da Fase 10.

Este documento não homologa implantação em LegislaGD ou Observatório; trata exclusivamente a nova capacidade offline do SD-Knowledge.
