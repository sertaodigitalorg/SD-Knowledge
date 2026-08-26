# ADR-009: Functional Master Google Drive

**Data:** 2026-08-26

## Contexto

A SDKA precisa consultar conhecimento funcional e institucional sem transformar
produtos individuais em clientes diretos do Google Drive. O ecossistema ja
define duas autoridades complementares: Google Drive para conhecimento
funcional/institucional e GitHub para conhecimento tecnico, codigo, Skills,
schemas, deploy e ADRs.

Tambem ha necessidade de um ponto interno comum para leitura funcional por
agentes e futuras interfaces, evitando que LegislaGD, SIGI-SD, VEREDAS,
Plataforma360 ou outros produtos implementem integracoes proprias com o Drive.

## Decisao

Google Drive e a autoridade funcional e institucional.

GitHub e a autoridade tecnica.

O SDKA Functional Bridge e um modulo interno da SDKA, mantido no repositorio
`SD-Knowledge`. Ele nao e um repositorio independente e nao deve ser tratado
como produto separado.

O acesso ao Google Drive deve ocorrer diretamente pelas APIs oficiais do Google:

```text
Functional Bridge
    |
    |-- GoogleDriveClient -> Google Drive API
    |-- GoogleDocsClient  -> Google Docs API
```

Google Drive Desktop, rclone, mounts, pastas sincronizadas, filesystems remotos
ou copias locais do Drive nao devem ser usados como arquitetura da solucao.

Produtos individuais nao devem integrar diretamente com a Google Drive API para
consulta funcional. O modelo aprovado e:

```text
LegislaGD
SIGI-SD
VEREDAS
Plataforma360
Outros
    |
    v
SDKA -> Functional Bridge -> Functional Source -> Google Drive
```

O modelo evitado e:

```text
LegislaGD -> Google Drive API
SIGI-SD -> Google Drive API
VEREDAS -> Google Drive API
```

## Fases

```text
FASE 1: READ
FASE 2: PROPOSE
FASE 3: CONTROLLED WRITE
FASE 4: SDKA + MCP + MANDACARU
```

## Authority Resolver

Na Fase 1, o repositorio deve preparar a separacao conceitual entre autoridade
funcional e fonte funcional:

```text
Functional Authority
    |
    v
Functional Source
    |-- Google Drive
    |-- fontes futuras
```

Essa separacao preserva o caminho futuro:

```text
Authority Resolver
    |-- Functional -> Google Drive
    |-- Technical -> GitHub
```

Google Drive nao deve virar sinonimo tecnico de funcional. Ele e a fonte
funcional inicial autorizada.

## Alternativas Consideradas

- [ ] Criar um repositorio `sdka-functional-bridge` separado.
  Rejeitado porque fragmentaria a SDKA, duplicaria governanca e criaria
  acoplamento entre repositorios para uma capacidade interna.
- [ ] Implementar conectores Google Drive em cada produto.
  Rejeitado por duplicacao, maior superficie de seguranca e risco de regras de
  autoridade divergentes.
- [x] Manter o Functional Bridge como modulo interno do `SD-Knowledge`.
  Escolhido por centralizar autoridade tecnica, reduzir acoplamento e preservar
  menor privilegio.

## Consequencias

**Positivas:**

- Um unico ponto tecnico governa leitura funcional por agentes.
- Produtos permanecem desacoplados da API do Google Drive.
- A separacao entre master funcional e master tecnico fica versionada.
- A Fase 1 pode ser read-only by design.
- A autenticacao deve ser configurada para escopo funcional explicito, por
  exemplo `FUNCTIONAL_DRIVE_ID` e `FUNCTIONAL_ROOT_FOLDER_ID`.

**Negativas:**

- Consumidores precisam depender da interface SDKA, nao do Drive diretamente.
- A implementacao futura deve manter adaptadores bem isolados para evitar
  vazamento de conceitos Google Drive.
- A escolha entre Service Account e OAuth 2.0 depende da configuracao real do
  Google Workspace/Drive institucional e das permissoes em pastas ou Shared
  Drives.

## Impacto Cruzado

- Drive: permanece master funcional/institucional.
- GitHub: `SD-Knowledge` passa a documentar formalmente o modulo interno.
- Produtos: LegislaGD, SIGI-SD, VEREDAS, Plataforma360 e outros devem consumir
  capacidade funcional via SDKA quando ela existir.
- Seguranca: a Fase 1 deve usar somente leitura e menor privilegio.
