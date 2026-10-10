# SDKA — Escopo institucional das capacidades de engenharia

**Status:** proposta técnica para revisão, vinculada às issues #25 e #27 e ao PR #26.

## Identidade e finalidade

A SDKA pertence ao ecossistema Sertão Digital. Não constitui framework neutro de mercado, serviço SaaS externo ou produto genérico. API Anything e Replica Skill são referências de engenharia, nunca autoridades arquiteturais.

## Regras mandatórias para próximas implementações

1. Todo diagnóstico deverá identificar `institution: sertaodigital`, o repositório do produto e a Skill de contexto correspondente. Produtos e repositórios devem ser resolvidos nos manifestos oficiais, sem duplicar catálogos.
2. Carregar `AGENTS.md`, `skills/sertaodigital-core/SKILL.md`, `docs/SOURCE_OF_TRUTH.md`, regras de decisão técnica, ADRs e Skills de produto antes de produzir recomendações.
3. Não presumir ausência de capacidades quando a descoberta falhar. Diferenciar `observed`, `inferred` e `not_verified`.
4. Não exportar dados institucionais internos, pessoais, tokens, documentos restritos ou resultados de autenticação para repositórios públicos, logs ou ferramentas externas.
5. A arquitetura deve aproveitar provedores e bibliotecas externas por integração opcional, com controle de versão e licença, sem dependência obrigatória deles.
6. Toda operação externa deve ter escopo, finalidade, base de autorização, limites e registro de proveniência; testes iniciais permanecem offline e read-only.
7. Mudanças funcionais exigem validação no MASTER Drive ou handoff; decisões técnicas permanecem no GitHub e exigem ADR quando aplicável.
8. Nenhuma Skill proposta deve ser ativada em `knowledge.yaml` antes de revisão de segurança, schema, testes e aprovação.

## Próximo incremento técnico

Alterar os schemas de avaliação e conector para exigir contexto institucional e referências canônicas, adaptar as fixtures e ampliar o validador para casos negativos. Em seguida, realizar um teste offline com um artefato não sensível de um produto Sertão Digital. Nenhuma integração runtime está autorizada por este documento.
