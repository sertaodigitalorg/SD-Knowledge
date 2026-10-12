# SDKA Core 1.0 — plano de consolidação e critérios de aceite

**Estado:** checklist de preparação; **não** declara a versão 1.0 lançada, integrada ou homologada.

## Linha de base

A `main` contém a estrutura de conhecimento, manifestos oficiais, bootstrap institucional, Skills ativas de núcleo/LegislaGD/Observatório, roteamento, descoberta e testes das fases anteriores. Os itens abaixo são entregas independentes ainda em PRs abertos.

## Fila de integração

| Ordem sugerida | PR | Entrega | Situação no levantamento |
| --- | --- | --- | --- |
| 1 | #32 | Proveniência e registro de evidências | Aberto; revisão/merge pendentes |
| 2 | #33 | Integridade automática de manifestos | Aberto; revisão/merge pendentes |
| 3 | #34 | Relatório institucional de governança | Aberto; revisão/merge pendentes |
| 4 | #35 | Planejamento consultivo de impacto entre produtos | Aberto; revisão/merge pendentes |

A ordem facilita testes incrementais, mas os PRs partiram da `main` e não devem depender de cherry-pick informal. **Após cada merge**, atualizar branches remanescentes pela interface GitHub, resolver conflitos e exigir novos checks no HEAD. Revisões podem ficar obsoletas e precisar ser refeitas. Nunca ignorar a regra do revisor ou o Destructive Action Guard.

## Critérios verificáveis para declarar SDKA Core 1.0

1. Os quatro PRs incorporados à `main` por revisão e merge autorizados.
2. `main` possui todos os workflows de conhecimento, lint, engenharia e proteção aprovados sobre os commits finais.
3. `knowledge.yaml`, `products.yaml`, `repositories.yaml` e `sources.yaml` seguem como manifestos canônicos sem catálogos concorrentes.
4. Inventário cobre os dez produtos atualmente registrados sem declarar status funcional não comprovado.
5. Auditoria de integridade e testes negativos passam; falhas de referência continuam gerando bloqueios.
6. Evidências têm referência rastreável e nível de verificação explícito; consulta estática não se apresenta como teste executado.
7. Relatório de governança e planejamento de impacto permanecem **consultivos, offline e sem autoridade para escrita**.
8. SIGI-SD e VEREDAS seguem com Skills preparatórias inativas; `sdka-engineering-intelligence` permanece experimental/inativa.
9. ADR-010, integrações externas, execução de testes operacionais e avaliação com colaboradores não são declaradas concluídas.
10. Registrar commit da versão consolidada, data e responsável **somente após** confirmação da `main` e dos checks finais.

## Entregas para depois do Core

- Revisão técnica produto a produto: Observatório Mandacaru, LegislaGD, SIGI-SD, VEREDAS e demais componentes/cadastros.
- Integrações externas, auditoria semântica e criação de issues automatizada exigem autorização e propostas próprias.
- Homologação prática de colaboradores ocorrerá depois de concluída a implantação automatizada, conforme a estratégia Automation First.

## Processo de encerramento

1. Conferir PRs, proteção da branch e lista de revisores.
2. Aprovar/mesclar cada PR conforme política institucional; conferir CI a cada alteração.
3. Executar conjunto final de validações da SDKA na `main`.
4. Abrir registro documental específico de release com SHA consolidado e pendências remanescentes.
5. Declarar Core 1.0 implantado apenas após os passos anteriores.

**Nenhum passo acima autoriza merge automático ou dispensa validação humana de código.**
