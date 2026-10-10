# Roteamento de Skills e orientação inicial — SDKA

**Estado:** proposta de melhoria do fluxo existente; sujeita a revisão no PR #26.

## Ponto de entrada único

O agente inicia pelo `AGENTS.md`, consulta a Skill `sertaodigital-core` e resolve o escopo pelos manifestos `knowledge.yaml`, `products.yaml` e `repositories.yaml`. **Não existe uma segunda Skill master ou catálogo paralelo**. Este workflow orienta a execução da Skill central.

## Identificação guiada

1. Perguntar somente o mínimo necessário: intenção/tarefa, produto/repositório e nível de familiaridade, caso não estejam no contexto.
2. Consultar os catálogos oficiais; confirmar registro ativo e Skill de produto ativa. Não deduzir apenas por nome/prefixo de organização.
3. Classificar a tarefa: aprendizado, entendimento, código, teste, documentação, arquitetura, segurança, implantação ou mudança funcional.
4. Carregar `SOURCE_OF_TRUTH.md`, regras de acesso e documentação oficial para o tipo de tarefa.
5. Direcionar para a Skill do produto; usar Skills técnicas complementares **somente se ativas e pertinentes**. Skill inexistente ou inativa: registrar lacuna/issue, não improvisar decisões.
6. Para tarefas híbridas, carregar todas as Skills necessárias e distinguir proprietários das decisões, evitando instruções conflitantes.

## Modo orientado para iniciantes e juniores

O nível de explicação **não muda as exigências de segurança, revisão e aprovação**.

- Explicar brevemente o que será feito, por que, qual repositório e quais arquivos oficiais consultar.
- Oferecer sequência executável: preparar ambiente, ler contexto, definir escopo, modificar em branch, testar, documentar, abrir PR.
- Mostrar exemplos mínimos e critérios de aceite; identificar comandos destrutivos e alternativas seguras.
- Antes de operações irreversíveis, acesso autenticado, produção, exposição de dados ou merge: parar e solicitar autorização/revisão humana apropriada.
- Ao final, relatar o que foi comprovado, o que depende de validação e links para issue/PR.
- Evitar sobrecarregar o iniciante com detalhes fora do problema; aprofundar quando solicitado.

## Roteamento mínimo

| Contexto identificado | Skill primária | Complemento |
| --- | --- | --- |
| Institucional, documentação geral e governança | `sertaodigital-core` | Fonte MASTER do domínio |
| LegislaGD | `legislagd` | `sertaodigital-core` |
| Observatório Mandacaru | `observatorio-mandacaru` | `sertaodigital-core` |
| Reconhecimento e análise de lacunas | Skill do produto | `sdka-engineering-intelligence` **apenas após ativação** |
| Produto sem Skill ativa | `sertaodigital-core` para orientação preliminar | Criar issue; não assumir regras específicas |

Esta tabela é **orientação**, não uma segunda fonte de verdade. Sempre prevalece `knowledge.yaml` e o registro do produto.

## Formato da primeira resposta a um colaborador

1. **Contexto identificado:** projeto, repositório, Skill e nível de certeza.
2. **Objetivo e cautelas:** resultado desejado, proibições e permissões.
3. **Primeiros passos:** sequência curta, com localização dos arquivos e comandos seguros.
4. **Verificação:** teste esperado, evidências, aprovação humana e PR.
5. **Lacunas:** o que ainda precisa ser confirmado, sem inventar estado do projeto.

## Exemplo ilustrativo

**Pedido:** "Sou novo e preciso corrigir um problema no LegislaGD."

**Orientação esperada:** apontar `AGENTS.md`, `sertaodigital-core` e `legislagd`; localizar o repositório no manifesto; identificar o problema reproduzível, branch permitida, teste, revisão e PR. Não escolher framework, endpoint, acesso ou instruções de deploy sem consultar código/ADRs do produto.

## Verificação de qualidade

- [ ] Entrada central existente, sem criar outro MASTER.
- [ ] Roteamento compatível com os manifestos oficiais.
- [ ] Iniciantes recebem instruções pedagógicas, sem relaxar gates.
- [ ] Evidências são separadas de hipóteses.
- [ ] Skill técnica inativa não é executada.
- [ ] Mudanças funcionais encaminhadas ao MASTER do Drive.
