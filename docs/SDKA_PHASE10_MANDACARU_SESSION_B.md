# Sessão B — Piloto assistido do Observatório Mandacaru

**Estado:** roteiro preparado; avaliação humana pendente. **Não preencher notas antecipadamente.**

## Participantes e condições

- Participante: desenvolvedor iniciante convidado, sem necessidade de acesso a dados pessoais.
- Facilitador: apresenta o exercício, esclarece o objetivo sem responder pelo participante.
- Revisor: verifica evidências e pontua conforme `docs/templates/SDKA_PHASE10_PILOT_RECORD.md`.
- Ambiente: leitura de documentação e simulação; **sem** deploy, merge, gravação em repositórios de produto ou uso de credenciais.

## Enunciado a apresentar sem explicação adicional

> Sou novo no Sertão Digital e preciso implementar uma funcionalidade de indicadores no Observatório Mandacaru. Como começo sem comprometer os dados existentes?

## Sequência observável

1. O participante localiza `AGENTS.md`, `skills/sertaodigital-core/SKILL.md` e `skills/observatorio-mandacaru/SKILL.md`.
2. Identifica `observatorio_mandacaru` em `products.yaml` e o repositório `sertaodigitalorg/ObservatorioMandacaru` via catálogo.
3. Classifica a tarefa como `feature` e descreve o que precisaria confirmar no requisito de indicadores antes de programar.
4. Distingue a especificação funcional no Drive, a evidência técnica no GitHub e o Observatório como MASTER de dados estruturados do ecossistema.
5. Explica quais evidências do repositório permitiriam classificar um recurso como IMPLEMENTADO, EM IMPLEMENTAÇÃO, PLANEJADO, CONCEITUAL ou DESCONTINUADO, **sem afirmar que verificou código que não abriu**.
6. Propõe procedimento seguro: esclarecer requisito → identificar fontes, dados e autorização → verificar código/testes → definir critérios de aceite → branch → testes → documentação → PR/revisão humana.
7. Identifica como impedimentos: acesso direto a dados sem autorização, utilização de dados pessoais, desconsiderar trilha de auditoria e promover roadmap a recurso implementado.

## Evidências admitidas

Anotações técnicas expurgadas, URLs institucionais públicas, resultado de comandos offline e ficha de avaliação assinada pelo revisor. Não anexar informações reais de cidadãos, credenciais ou cópias de dados privados.

## Perguntas de controle para o revisor

- Qual é a fonte de autoridade para requisitos funcionais de indicadores?
- O que é evidência suficiente para marcar uma funcionalidade como implementada?
- Como agir se o catálogo identificar o produto, mas a documentação técnica e o código divergirem?
- Quais decisões exigem Cross-Layer Impact Check ou ADR?
- O que é permitido realizar sem autorização de escrita?

## Aceite e resultado

Aplicar os sete critérios do formulário, total máximo 14 pontos, mínimo 12, sem nota zero em MASTER/segurança, sem ação não autorizada. Registrar o resultado como **PENDENTE** até revisão humana efetiva; não deduzir aprovação a partir dos testes automatizados da SDKA.

**Continuidade:** após o piloto B, conduzir A (LegislaGD), C (integração) e D (SIGI-SD) segundo o plano principal.
