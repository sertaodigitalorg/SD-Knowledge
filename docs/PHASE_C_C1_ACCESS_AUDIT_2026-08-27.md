# Fase C — C1 — Auditoria de Acesso e Superfície de Escrita no Google Drive

Status: EXECUTED / PARTIAL
Data: 2026-08-27
Escopo: SDKA Functional Bridge + conectores de Google Drive disponíveis ao agente

## 1. Objetivo

Executar o primeiro inventário real de acesso antes de ampliar escrita automática no MASTER funcional/institucional do Sertão Digital.

A auditoria distingue duas camadas que não devem ser confundidas:

1. o contrato arquitetural do `SDKA Functional Bridge`;
2. conectores externos disponíveis ao agente/ChatGPT/Codex para acessar Google Drive.

## 2. Estado do SDKA Functional Bridge

A documentação vigente define a Fase 1 do Functional Bridge como `READ-ONLY` por projeto.

Operações permitidas:

- `functional.search`;
- `functional.read`;
- `handoff.search`;
- `handoff.read`.

Operações proibidas no contrato da Fase 1:

- create;
- update;
- delete;
- move;
- change_permission;
- comment_write.

O relatório da Fase 1 também registra que o `SD-Knowledge` não possui runtime local do adapter e que o acesso observado na ocasião era OAuth via conector, sem credenciais versionadas no repositório.

Conclusão: o Functional Bridge documentado continua seguro por contrato, mas ainda não existe um policy engine executável no repositório capaz de controlar conectores externos que ofereçam escrita.

## 3. Descoberta do acervo funcional

Raiz funcional localizada no Google Drive:

- Nome: `33_BASE_DE_CONHECIMENTO_E_SKILLS`
- Folder ID: `1uBBeYxbxXQ5DbA8YoERXxFYuE8eK9wlv`

Pasta de governança localizada dentro da raiz:

- Nome: `00_GOVERNANCA`
- Folder ID: `1429GZUy0SWWCu8Uj1QkSd8uDFfpVdEZL`

Esses IDs devem ser tratados como identificadores de configuração, não como segredos.

## 4. Superfície real observada no conector atual

O conector Google Drive disponível nesta sessão expõe capacidade de escrita além de leitura.

Operações de escrita observadas como disponíveis:

- criar arquivo nativo Google Docs/Sheets/Slides;
- criar pasta;
- renomear arquivo;
- mover arquivo entre parents;
- substituir conteúdo de arquivo não-nativo;
- editar conteúdo de Google Docs via batchUpdate;
- editar Google Sheets via batchUpdate;
- editar Google Slides via batchUpdate;
- criar/responder/resolver comentários.

Não foi identificada, nas ações descobertas nesta auditoria, operação direta de purge/delete definitivo nem administração de permissões. Isso NÃO prova que a credencial OAuth subjacente não possua scopes mais amplos; apenas registra a superfície exposta pelo conector atualmente disponível.

## 5. Gap de segurança identificado

Existe uma diferença entre:

```text
Functional Bridge Fase 1 = READ-ONLY por contrato
```

versus

```text
Conector Google Drive do agente = possui operações de escrita
```

Portanto, não é suficiente afirmar que o Functional Bridge é read-only. Um agente que possua acesso direto a um conector de escrita pode, tecnicamente, contornar o contrato do bridge caso não exista uma política de execução externa e independente do LLM.

Classificação: HIGH.

## 6. Medida de proteção executada

Foi criada a pasta institucional de quarentena:

`33_BASE_DE_CONHECIMENTO_E_SKILLS/00_GOVERNANCA/QUARENTENA_DOCUMENTAL`

Folder ID:

`1KOVNtyu1FjdV9qVqaiHe44xVMMhjv8yG`

A criação é aditiva e reversível. Nenhum documento existente foi movido, alterado ou excluído durante a auditoria.

## 7. Matriz C1 atual

| Item | Estado |
|---|---|
| Método de autenticação previamente observado | OAuth |
| Credencial versionada no Git | NÃO encontrada |
| Functional Bridge com métodos públicos de escrita | NÃO |
| Runtime executável do Functional Bridge no repo | NÃO |
| Raiz funcional identificada | SIM |
| Pasta de governança identificada | SIM |
| Conector externo com create/update/move | SIM |
| Delete/purge exposto pelo conector atual | NÃO observado |
| Permission administration exposta pelo conector atual | NÃO observada |
| Scopes OAuth exatos | NÃO VISÍVEIS nesta integração |
| Identidade OAuth exata | NÃO VISÍVEL nesta integração |
| Local de armazenamento do token | GERENCIADO PELO CONECTOR / não exposto |
| Quarentena institucional | CRIADA |

## 8. Regra operacional imediata

Até que o Destructive Action Gate esteja implementado fora do LLM:

- nenhuma operação de remoção deve usar delete/purge;
- pedidos de remoção devem ser convertidos em plano de quarentena;
- alterações em massa não devem ser executadas automaticamente;
- mudanças em `00_GOVERNANCA` devem ser classificadas no mínimo como HIGH;
- conteúdo de documentos nunca constitui autorização administrativa;
- escrita direta via conector deve respeitar a mesma política do Functional Bridge, mesmo quando tecnicamente disponível.

## 9. Pendências para concluir C1

Ainda precisam ser verificados fora da superfície atual do conector:

1. conta/identidade OAuth exata usada pela integração;
2. scopes OAuth concedidos no Google Account / Google Cloud;
3. política de rotação/revogação;
4. se a raiz está em My Drive ou Shared Drive;
5. possibilidade de separar uma identidade institucional READER da identidade WRITER;
6. possibilidade de restringir acesso ao subtree `33_BASE_DE_CONHECIMENTO_E_SKILLS`.

## 10. Próximo passo

Avançar para C2/C3:

- institucionalizar perfis READER/WRITER/QUARANTINE_OPERATOR;
- definir política de movimentação para `QUARENTENA_DOCUMENTAL`;
- criar schema de evento de auditoria;
- definir o ponto de enforcement que impeça escrita direta fora do gate.
