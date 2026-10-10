# Domínio — Observatório Mandacaru

## Núcleo implementado

| Entidade | Relação principal |
|---|---|
| `User` | responsável por cadastros; autor de avisos; papéis; perfil autodeclarado; formação profissional e organização associada opcionais |
| `Instituicao` | possui projetos; responsável opcional |
| `Projeto` | pertence opcionalmente a uma instituição; possui indicadores |
| `Indicador` | pertence opcionalmente a um projeto |
| `Post` / `Tag` | avisos e classificação por tags |
| `CadastroHistorico` | registra ação, tipo/id, observação, dados, responsável/revisor e data |

As três entidades de cadastro guardam estados e alterações propostas; não há modelo estruturado de fonte/proveniência. O histórico existente não cobre toda alteração administrativa.

## Papéis e workflow

Papéis: `ROLE_USER`, `ROLE_EDITOR`, `ROLE_ADMIN`. Perfis autodeclarados `pessoa`, `instituicao`, `empresa`, `estudante` e `professor` não são papéis de autorização. O cadastro público concede somente `ROLE_USER`.

O perfil profissional registra formação; o perfil empresarial associa o nome da empresa à conta da pessoa responsável. Esses campos não criam entidades próprias de profissional ou empresa.

O contribuinte cria rascunhos próprios, envia à análise e o editor aprova/publica, devolve ou rejeita. A versão publicada é mantida durante revisão de proposta. Administração direta pode alterar status fora desse fluxo; classificar o workflow global como parcial.

## Expansão conceitual

Cadastros empresariais básicos existem como perfil e metadado da conta; uma entidade de Empresa com dados, relações ou ciclo editorial próprios não está implementada. Órgãos públicos, startups, universidades, pesquisadores, profissionais como entidade, comunidades, projetos/iniciativas ampliados, programas, políticas, pesquisas, documentos, evidências, tecnologias, softwares, territórios, indicadores, oportunidades e relações ampliadas são conceitos para validação/taxonomia e roadmap. Não presumir que sejam tabelas ou APIs atuais.

## Proveniência

Definir fonte, origem, coleta, responsável, método, atualização, confiabilidade, evidência e validação antes de ingestão ampliada ou IA. Não introduzir entidades sem análise de domínio, privacidade, retenção, migração e ADR.
