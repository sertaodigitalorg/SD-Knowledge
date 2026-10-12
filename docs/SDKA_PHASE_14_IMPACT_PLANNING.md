# SDKA — Fase 14: planejamento de impactos entre produtos

**Status:** automatização consultiva, offline, sem autorização de implementação.

## Objetivo

Usar exclusivamente os catálogos canônicos da SDKA para elaborar um roteiro inicial de revisão de impactos cruzados. Não presume conexões funcionais entre produtos com base apenas no catálogo.

## Execução

```bash
python scripts/sdka_impact_plan.py legislagd sapl_sd
python scripts/sdka_impact_plan.py sigi_sd veredas
python -m unittest discover -s scripts -p 'test_impact_plan.py' -v
```

## Contrato e limites

A saída contém o produto, família de componentes declarados, repositório registrado, Skill ativa se houver, fontes consultadas e exigência de revisão. Os vínculos do catálogo **não** equivalem a comprovação de impacto no código. Portanto `status=review_required`, `authorization_granted=false` e `cross_layer_impact_check_required=true` em todos os casos.

A ferramenta falha se algum produto informado não estiver em `products.yaml`; não cria issues, não executa requests, não modifica o Drive ou GitHub, não ativa Skills e não autoriza merge.

## Evolução posterior

Após a consolidação central, futuros módulos poderão anexar evidências técnicas autorizadas, gerar rascunhos de issues ou ADRs e inspecionar o impacto funcional. Essas capacidades exigirão contratos, aprovação e PRs específicos, sem enfraquecer os gates existentes.

**Independência:** Fase 14 desenvolvida a partir da `main`, sem incorporar os PRs #32 e #33 ainda pendentes.
