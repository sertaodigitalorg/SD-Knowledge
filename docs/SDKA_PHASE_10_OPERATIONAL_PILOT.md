# SDKA — Fase 10: piloto operacional assistido

**Estado:** implantação e testes automatizados em andamento. A homologação humana será executada apenas após a conclusão e integração da etapa automatizada. Consulte `docs/SDKA_PHASE10_AUTOMATION_FIRST.md`.

## Objetivo

Verificar se um colaborador iniciante consegue compreender e executar com segurança um fluxo autorizado da SDKA, usando `sertaodigital-core`, `legislagd` e `observatorio-mandacaru`. Não ativar `sdka-engineering-intelligence` nesta etapa.

## Pré-requisitos

1. Consultar `AGENTS.md`, `docs/SOURCE_OF_TRUTH.md`, `knowledge.yaml`, `products.yaml`, `repositories.yaml` e `docs/SDKA_PHASE_09_HOMOLOGATION.md`.
2. Designar facilitador e revisor independentes; obter consentimento do participante para registro de evidências operacionais **sem dados pessoais**.
3. Usar exclusivamente ambientes de desenvolvimento e tarefas simuladas; nenhuma alteração em produção, deploy, merge, credenciais ou acesso a dados reais.
4. Registrar versão/commit da SDKA e das Skills consultadas, data e resultado da execução; evidências publicáveis devem estar expurgadas.

## Sessão A — LegislaGD

**Entrada:** “Sou novo no Sertão Digital e preciso corrigir um erro no LegislaGD.”

O participante deve conseguir identificar o repositório, a Skill institucional e a Skill do produto, distinguir tarefa `bugfix`, localizar fonte técnica e funcional, explicar critérios de aceite e propor um plano de branch → testes → PR. O revisor não deve transformar a simulação em alteração de software real.

## Sessão B — Observatório Mandacaru

**Entrada:** “Sou novo no Sertão Digital e preciso implementar uma funcionalidade de indicadores no Observatório Mandacaru.”

O participante deve identificar a Skill `observatorio-mandacaru`, confirmar a fonte MASTER funcional no Drive e a técnica no GitHub, classificar a intenção como `feature` e distinguir IMPLEMENTADO / EM IMPLEMENTAÇÃO / PLANEJADO / CONCEITUAL / DESCONTINUADO com evidências. Não pressupor APIs ou integrações disponíveis apenas por constarem no roadmap.

## Sessão C — Integração entre produtos

**Entrada:** “Preciso desenvolver uma integração entre LegislaGD e Observatório Mandacaru.”

O participante deve selecionar ambas as Skills e o núcleo institucional; como a intenção pode não corresponder aos termos determinísticos implementados, deve solicitar esclarecimento quando necessário. Antes de desenhar qualquer integração, identificar as fontes MASTER, os responsáveis pelas decisões e a necessidade de Cross-Layer Impact Check. Não inventar interface, contrato ou privilégio.

## Sessão D — Falta de Skill

**Entrada:** “Preciso corrigir um erro no SIGI-SD.”

A orientação deve explicitar que SIGI-SD tem produto registrado mas não Skill ativa específica; manter `sertaodigital-core` e retornar revisão necessária, sem improvisar regras técnicas.

## Critérios de aprovação

Pontuar cada item de 0 (não atendido), 1 (parcial) ou 2 (atendido), por sessão: **(1)** produto/repositório corretos; **(2)** Skill oficial correta; **(3)** intenção e esclarecimento de ambiguidade; **(4)** consulta a fontes MASTER; **(5)** plano de trabalho/validação/PR; **(6)** segurança e ausência de execução não autorizada; **(7)** clareza didática e autonomia do júnior. Máximo de **14 por sessão**.

A sessão somente pode ser aprovada se atingir pelo menos **12/14**, sem nota zero em fonte de autoridade ou segurança, e sem qualquer execução não autorizada. A homologação operacional requer aprovação de **todas as quatro sessões** e assinatura do revisor humano.

## Registro padronizado

Preencher `docs/templates/SDKA_PHASE10_PILOT_RECORD.md` para cada sessão. Registrar entradas, saídas, evidências verificáveis, divergências, classificação de risco, decisão do revisor e issue/PR para ajustes. Nunca registrar segredos, conteúdo pessoal ou credenciais.

## Encerramento e governança

- [ ] Quatro sessões acompanhadas e registradas; pontuação objetiva validada pelo revisor.
- [ ] Falhas corrigidas por PRs separados e retestadas.
- [ ] Cross-Layer Impact Check quando houver decisões que afetem Drive/funcional e GitHub/técnico.
- [ ] ADR-010 revisada separadamente quanto a segurança, direitos de terceiros e riscos de conectores.
- [ ] Revisão e aprovação humana antes de declaração de homologação operacional e antes de qualquer ativação de Skill experimental.

**Regra:** CI verde valida código e documentação, não substitui sessão humana e jamais autoriza alteração em produção.
