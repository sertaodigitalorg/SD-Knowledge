# SDKA — Fase 9: consolidação e homologação do roteamento

Status: **em homologação**, sem autorização para ativar a Skill experimental.

## Diagnóstico pós-merge do PR #26

A branch `main` contém `AGENTS.md`, `sertaodigital-core`, roteador de Skills, descoberta por nome canônico e orientação por intenção. Os manifestos de autoridade permanecem `knowledge.yaml`, `products.yaml`, `repositories.yaml` e `sources.yaml`.

**Inconsistência a eliminar:** `scripts/sdka_registry_gate.py` mantém o dicionário fixo `allowed_skill_by_product`, enquanto `scripts/sdka_skill_router.py` resolve a Skill por convenção sobre o domínio registrado. É necessário unificar essa regra sem criar catálogo paralelo. Nenhuma modificação desse código é pressuposta neste documento.

## Piloto 1 — Colaborador júnior / LegislaGD

**Entrada:** `Sou novo e preciso corrigir um erro no LegislaGD`.

**Aceite:** reconhecer `legislagd`, Skill central e Skill do produto; intenção `bugfix`; oferecer roteiro de reprodução, fonte oficial, branch, testes e PR; não executar código nem autorizar alterações por inferência.

## Piloto 2 — Requisito novo / LegislaGD

**Entrada:** `Implementar uma nova funcionalidade no LegislaGD`.

**Aceite:** classificar como `feature`; indicar necessidade de requisito funcional aprovado e critérios de aceite; exigir revisão antes de produção.

## Piloto 3 — Integração LegislaGD / SIGI-SD

**Entrada:** `Corrigir integração LegislaGD com SIGI-SD`.

**Aceite:** reconhecer dois produtos; encaminhar LegislaGD para Skill ativa; sinalizar `review_required` para SIGI-SD enquanto não tiver Skill específica ativa; não inventar arquitetura do SIGI-SD.

## Piloto 4 — Pedido genérico

**Entrada:** `Preciso corrigir atendimento ao cidadão`.

**Aceite:** solicitar esclarecimento de produto; nenhuma associação implícita autorizada.

## Piloto 5 — Solicitação ambígua

**Entrada:** `Preciso corrigir e documentar o LegislaGD`.

**Aceite:** reconhecer múltiplas intenções e solicitar prioridade ou dividir etapas antes de executar.

## Comandos offline de verificação

```bash
python scripts/sdka_task_guidance.py 'Sou novo e preciso corrigir um erro no LegislaGD' --experience junior
python scripts/sdka_task_guidance.py 'Corrigir integração LegislaGD com SIGI-SD' --experience junior
python -m unittest discover -s scripts -p 'test_*.py' -v
```

## Critérios de encerramento

- [ ] Testes completos executados no estado final da branch.
- [ ] Validador e roteador usam associação produto–Skill única e verificável.
- [ ] Oito pilotos confirmados em execução offline, sem dados pessoais.
- [ ] Teste com profissional iniciante real ou simulação humana revisada.
- [ ] ADR-010, licenças e aspectos de segurança revisados separadamente antes de ativação.
- [ ] Aprovação humana, histórico de revisão e guard de ações destrutivas preservados.

**Observação:** roteiro gerado por software não significa que houve execução de uma correção ou aprovação funcional. Google Drive continua MASTER institucional/funcional; GitHub, MASTER técnico.

## Piloto 6 — Colaborador júnior / Observatório Mandacaru

**Entrada:** `Sou novo e preciso corrigir um erro no Observatório Mandacaru`.

**Aceite:** selecionar `sertaodigital-core` + `observatorio-mandacaru`; identificar `bugfix`; orientar leitura da Skill, reprodução, testes e PR. Antes de dizer que algo está implementado, confirmar no código e aplicar os estados IMPLEMENTADO, EM IMPLEMENTAÇÃO, PLANEJADO, CONCEITUAL ou DESCONTINUADO.

## Piloto 7 — Indicadores e governança de dados / Observatório Mandacaru

**Entrada:** `Implementar uma nova funcionalidade de indicadores no Observatório Mandacaru`.

**Aceite:** selecionar a Skill do Observatório e classificar `feature`; consultar especificação funcional MASTER no Drive e código MASTER técnico no repositório; preservar rastreabilidade, autorização e classificação de dados. Não confundir expansão planejada com implementação existente.

## Piloto 8 — Integração Observatório Mandacaru / LegislaGD

**Entrada:** `Implementar uma nova funcionalidade de integração entre Observatório Mandacaru e LegislaGD`.

**Aceite:** reconhecer os dois produtos, selecionar ambas as Skills de produto e a institucional; exigir escopo, APIs autorizadas, evidências e revisão cross-layer antes de qualquer alteração. Não presumir integração existente somente porque os produtos são cadastrados.

## Verificação adicional do Observatório

```bash
python scripts/sdka_task_guidance.py 'Sou novo e preciso corrigir um erro no Observatório Mandacaru' --experience junior
python scripts/sdka_task_guidance.py 'Implementar uma nova funcionalidade de indicadores no Observatório Mandacaru' --experience junior
python scripts/sdka_task_guidance.py 'Implementar uma nova funcionalidade de integração entre Observatório Mandacaru e LegislaGD' --experience junior
```

Os pilotos 6–8 são critérios de aceite propostos, **não** resultados de execução já homologados. A Skill do Observatório permanece ativa no catálogo institucional; a Skill experimental de Engineering Intelligence continua inativa.
