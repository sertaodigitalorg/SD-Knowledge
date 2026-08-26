# SDKA Functional Bridge

## Definicao

O SDKA Functional Bridge e um modulo interno da SDKA, mantido no repositorio
`SD-Knowledge`. Ele existe para consultar fontes funcionais autorizadas e
entregar documentos funcionais a agentes e consumidores tecnicos sem acoplar
produtos diretamente ao Google Drive.

O Functional Bridge nao e projeto, produto ou repositorio independente.

## Autoridades

```text
Google Drive = MASTER FUNCIONAL / INSTITUCIONAL
GitHub       = MASTER TECNICO
```

Uma decisao tecnica nao altera automaticamente uma regra funcional. Quando uma
regra funcional estiver ausente ou ambigua, registre:

```text
STATUS: PENDING FUNCTIONAL DECISION
```

## Arquitetura Conceitual

```text
VS Code / Codex
    |
    v
SD-Knowledge
    |
    v
SDKA
    |
    v
Functional Bridge
    |
    |-- GoogleDriveClient -> Google Drive API
    |-- GoogleDocsClient  -> Google Docs API
    |
    v
Google Drive institucional
    |
    v
MASTER FUNCIONAL
```

O VS Code e apenas o ambiente de execucao do agente e do repositorio. O Google
Drive permanece remoto.

Nao usar como arquitetura:

- Google Drive Desktop;
- rclone;
- mount de Drive;
- pasta sincronizada;
- filesystem remoto;
- copia local do Drive como fonte funcional.

## Interfaces Da Fase 1

As operacoes conceituais da Fase 1 sao:

```text
functional.search
functional.read
handoff.search
handoff.read
```

Essas operacoes devem ser independentes do mecanismo de transporte. Elas podem
ser expostas futuramente por CLI, SDK, MCP ou outro mecanismo autorizado.

Aliases historicos como `functional.handoff.search` e
`functional.handoff.read` podem ser aceitos por compatibilidade, mas a semantica
canonica e `handoff.search/read`, porque handoffs cruzam camadas.

## Modelo De Dominio

```text
FunctionalDocument
```

Campos:

```yaml
authority: functional
source: google-drive
documentId: string
name: string
mimeType: string
modifiedAt: datetime
content: string | null
metadata: object
product: string | null
documentType: string | null
status: string | null
```

`product`, `documentType` e `status` so devem ser preenchidos quando estiverem
presentes ou forem determinaveis com seguranca. Nao invente classificacao.

## Contratos Conceituais

### FunctionalSource

Responsavel por representar uma fonte funcional consultavel.

Operacoes permitidas na Fase 1:

```text
search(query, filters) -> FunctionalDocument[]
read(documentId) -> FunctionalDocument
```

Operacoes proibidas na Fase 1:

```text
create
update
delete
move
change_permission
comment_write
```

### HandoffSource

Responsavel por localizar e ler handoffs tecnicos ou funcionais em fontes
autorizadas, quando existirem.

Regra de direcao:

```text
TECHNICAL HANDOFF
    origin_layer: functional
    target_layer: technical
    leitor natural: agente tecnico

FUNCTIONAL HANDOFF
    origin_layer: technical
    target_layer: functional
    leitor natural: agente funcional
```

Um agente tecnico deve conseguir pesquisar e ler TECHNICAL HANDOFFs gerados pela
camada funcional. Um agente funcional deve conseguir pesquisar e ler FUNCTIONAL
HANDOFFs gerados pela camada tecnica.

Operacoes permitidas na Fase 1:

```text
handoff.search(query, filters) -> HandoffDocument[]
handoff.read(documentId) -> HandoffDocument
```

Filtros minimos:

```yaml
type: TECHNICAL | FUNCTIONAL | null
origin_layer: functional | technical | null
target_layer: functional | technical | null
product: string | null
status: PENDING | IN_PROGRESS | COMPLETED | CANCELLED | null
```

## GoogleDriveFunctionalSource

O adaptador Google Drive da Fase 1 deve:

- usar apenas escopos de leitura compatíveis com a necessidade real;
- listar metadados de arquivos e pastas autorizados;
- ler conteudo de documentos funcionais suportados;
- falhar de forma explicita para documentos inexistentes, permissao insuficiente
  ou tipo MIME nao suportado;
- nunca expor metodos publicos de escrita;
- nunca armazenar tokens ou credenciais no Git.

Chamadas especificas do Google devem ficar nos clientes de infraestrutura:

```text
GoogleDriveClient
    |-- search
    |-- metadata
    |-- list
    |-- export/read

GoogleDocsClient
    |-- readDocument
```

O dominio da SDKA deve depender dos contratos funcionais, nao das APIs Google.

## Autenticacao E Escopo

A implementacao futura deve avaliar:

```text
Service Account
OAuth 2.0
```

Preferir identidade institucional, sem dependencia permanente de conta pessoal,
quando o Google Workspace/Drive permitir.

Configuracao conceitual minima:

```text
FUNCTIONAL_DRIVE_ID
FUNCTIONAL_ROOT_FOLDER_ID
```

O Functional Bridge deve considerar somente documentos pertencentes ao escopo
funcional autorizado. Se a raiz estiver em Shared Drive, a implementacao deve
usar corretamente o identificador do Drive compartilhado e os parametros da
Drive API para drives compartilhados.

## Proveniencia

Toda leitura deve preservar origem:

```json
{
  "authority": "functional",
  "source": "google-drive",
  "document_id": "...",
  "name": "...",
  "mime_type": "...",
  "modified_at": "...",
  "content": "..."
}
```

Para handoffs, preservar tambem:

```json
{
  "handoff_id": "...",
  "type": "TECHNICAL",
  "origin_layer": "functional",
  "target_layer": "technical",
  "status": "PENDING"
}
```

## Erros Padronizados

```text
UNAUTHORIZED
DOCUMENT_NOT_FOUND
PERMISSION_DENIED
UNSUPPORTED_MIME_TYPE
EXPIRED_AUTHENTICATION
NETWORK_FAILURE
```

## Seguranca

A Fase 1 e read-only by design.

```text
READ-ONLY: YES
WRITE CAPABILITY: NO
LEAST PRIVILEGE: REQUIRED
```

Se um mecanismo autorizado oferecer escrita por capacidade tecnica, o modulo da
Fase 1 ainda deve bloquear essa capacidade no contrato publico.
