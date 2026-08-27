# Matriz de Auditoria Documental — Organização Sertão Digital

**Data da auditoria:** 2026-08-27  
**Escopo:** repositórios acessíveis da organização `sertaodigitalorg`  
**Objetivo:** classificar documentação entre MASTER funcional (Google Drive) e MASTER técnico (GitHub), identificar material híbrido e planejar migrações sem perda de histórico.

## Legenda

- **FUNCIONAL** — requisitos, regras, processos, manual do usuário/operador, comportamento esperado. MASTER: Google Drive.
- **TÉCNICO** — código, arquitetura, ADR, API, infraestrutura, deploy, troubleshooting, desenvolvimento. MASTER: GitHub.
- **HÍBRIDO** — contém elementos funcionais e técnicos; deve ser separado ou manter parte executável no GitHub com referência funcional no Drive.
- **PONTEIRO** — arquivo derivado que referencia o MASTER correspondente.
- **N/A** — repositório sem evidência de manual funcional próprio nesta rodada.

## Matriz consolidada

| # | Repositório | Perfil documental predominante | Manual/artefato funcional identificado | Classificação / autoridade | Ação | Prioridade | Estado |
|---:|---|---|---|---|---|---|---|
| 1 | `SD-Knowledge` | Governança técnica do conhecimento, Skills, ADRs, integração Drive/GitHub | Não há Manual do Usuário de produto; referências de domínio podem conter contexto funcional derivado | TÉCNICO / GitHub, com referências ao Drive | Manter; impedir que referências derivadas concorram com o MASTER funcional | Alta | AUDITADO |
| 2 | `VEREDAS` | Workspace e documentação operacional/técnica | `docs/manual-usuario.md`; `docs/manual-operador-funcional.md` | FUNCIONAL / Drive | **Migrado** para Drive; arquivos GitHub convertidos em PONTEIROS | Alta | SYNCED |
| 3 | `VEREDAS` | Suporte e implantação | `docs/manual-suporte-tecnico.md` | TÉCNICO / GitHub | Manter no GitHub e referenciar manuais funcionais no Drive | Alta | SYNCED |
| 4 | `VEREDAS` | Testes e validação | cenários e matriz de teste funcional | HÍBRIDO | Manter casos executáveis no GitHub; requisitos/resultados funcionais oficiais devem apontar para Drive | Alta | REVIEW_REQUIRED |
| 5 | `VEREDAS-Core` | Backend/Core, setup e operação técnica | README contém setup/uso técnico, não Manual do Usuário final | TÉCNICO / GitHub | Manter | Média | AUDITADO |
| 6 | `VEREDAS-Edge` | Edge/IoT, PWA e infraestrutura | README técnico; nenhum Manual do Usuário final confirmado | TÉCNICO / GitHub | Manter; revisar futuros guias de motorista/monitor como FUNCIONAL | Média | AUDITADO |
| 7 | `VEREDAS-PWA` | Frontend PWA | README técnico; nenhum manual funcional confirmado nesta rodada | TÉCNICO / GitHub | Manter; futuro guia de uso deve nascer no Drive | Média | AUDITADO |
| 8 | `LegislaGD` | Plataforma legislativa e integração de componentes | Nenhum arquivo de Manual do Usuário confirmado pela árvore pública nesta rodada | TÉCNICO predominante / GitHub | Criar/centralizar Manual do Usuário no Drive quando consolidado; GitHub apenas ponteiro | Alta | REVIEW_REQUIRED |
| 9 | `SAPL-SD` | Fork/evolução técnica do SAPL | README do upstream é documentação técnica/de projeto; nenhum manual funcional SD confirmado | TÉCNICO / GitHub | Manter; documentação de uso específica do LegislaGD/SAPL-SD deve ficar no Drive | Alta | AUDITADO |
| 10 | `PortalModelo-SD` | Fork/evolução do Portal Modelo | Nenhum manual funcional SD confirmado nesta rodada | TÉCNICO predominante / GitHub | Manter documentação upstream/técnica; guias de editor/usuário do produto SD devem ficar no Drive | Média | REVIEW_REQUIRED |
| 11 | `e-Cidade-SD` | Fork/evolução do e-Cidade | Árvore extensa; não foi confirmado Manual do Usuário SD próprio por nome nesta rodada | TÉCNICO predominante / GitHub | Não migrar documentação upstream automaticamente; separar futuros manuais funcionais SD para Drive | Média | REVIEW_REQUIRED |
| 12 | `Plenario-Digital-Core` | Core técnico do Plenário Digital | Nenhum manual de usuário identificado na árvore; repositório essencialmente técnico | TÉCNICO / GitHub | Manter; Manual do Operador do Plenário deve ser criado/mantido no Drive | Alta | AUDITADO |
| 13 | `SIGI-SD` | Sistema omnichannel, arquitetura e operação | Não foi confirmado Manual do Usuário por nome nesta rodada | TÉCNICO predominante / GitHub | Revisar docs de operação: separar uso de atendente/gestor (Drive) de implantação/admin técnico (GitHub) | Alta | REVIEW_REQUIRED |
| 14 | `Plataforma360` | Plataforma/arquitetura 360 | Nenhum Manual do Usuário confirmado na árvore nesta rodada | TÉCNICO predominante / GitHub | Manuais de gestor/operador devem ser Drive; documentação de API/ETL/BI permanece GitHub | Média | REVIEW_REQUIRED |
| 15 | `NoticiaSertaneja` | Aplicação Symfony/automação editorial | README técnico; nenhum Manual do Usuário confirmado | TÉCNICO / GitHub | Manter; se houver manual editorial/operacional, classificar como FUNCIONAL no Drive | Média | AUDITADO |
| 16 | `wpNoticiaSertaneja` | WordPress privado | Não confirmado nesta rodada | TÉCNICO predominante / GitHub | Configuração/deploy no GitHub; manual editorial no Drive | Média | REVIEW_REQUIRED |
| 17 | `Roteiro-Comercial` | Produto/aplicação comercial | Não confirmado nesta rodada | TÉCNICO predominante / GitHub | Manual de comerciante/operador no Drive; documentação técnica no GitHub | Média | REVIEW_REQUIRED |
| 18 | `Chatwoot-SD` | Fork/integração Chatwoot | Documentação upstream pode conter guias de uso, mas não deve ser migrada automaticamente | TÉCNICO/upstream / GitHub | Manter upstream; criar manual funcional específico do SIGI-SD no Drive, sem duplicar documentação externa | Baixa | REVIEW_REQUIRED |
| 19 | `BOT-SD` | Bot/automação | Não confirmado | TÉCNICO predominante / GitHub | Manter; fluxos conversacionais/regras de atendimento aprovadas devem ter autoridade funcional no Drive | Média | REVIEW_REQUIRED |
| 20 | `sistema-escolar` | Sistema escolar | Não confirmado | A CLASSIFICAR | Fazer revisão funcional específica antes de qualquer migração | Baixa | PENDING_REVIEW |
| 21 | `sertaodigital` | Site/repositório institucional | Não confirmado | TÉCNICO para código; institucional/funcional no Drive | Manter código no GitHub; políticas/conteúdo institucional autoritativo no Drive | Baixa | REVIEW_REQUIRED |
| 22 | `SEI` | Fork/espelho de sistema externo | Não confirmado | TÉCNICO/upstream / GitHub | Não migrar manuais upstream automaticamente; documentação institucional de uso SD, se criada, vai para Drive | Baixa | REVIEW_REQUIRED |
| 23 | `SoftwarePublico` | Portal/espelho de software público | Não confirmado | TÉCNICO/upstream / GitHub | Não migrar documentação upstream automaticamente | Baixa | REVIEW_REQUIRED |
| 24 | `e-Cidade` | Base/fork do e-Cidade | Não confirmado | TÉCNICO/upstream / GitHub | Não migrar documentação upstream automaticamente | Baixa | REVIEW_REQUIRED |
| 25 | `PortalModelo` | Base/fork do Portal Modelo | Não confirmado | TÉCNICO/upstream / GitHub | Não migrar documentação upstream automaticamente | Baixa | REVIEW_REQUIRED |
| 26 | `Portal-Padrao` | Base/fork de portal | Não confirmado | TÉCNICO/upstream / GitHub | Não migrar documentação upstream automaticamente | Baixa | REVIEW_REQUIRED |
| 27 | `e-gov` | Repositório de referência e-gov | Não confirmado | TÉCNICO/referência / GitHub | Revisar apenas se houver documentação autoral do Sertão Digital | Baixa | REVIEW_REQUIRED |
| 28 | `README` | Perfil/metadata da organização | Não se aplica | TÉCNICO/institucional derivado | Manter como apresentação; políticas oficiais continuam no Drive | Baixa | AUDITADO |

> A organização retornou 22 repositórios na listagem atual, porém a matriz contém linhas adicionais porque o `VEREDAS` foi decomposto por classes documentais distintas para preservar a rastreabilidade da auditoria.

## Achados principais

### 1. VEREDAS é o caso-piloto concluído

O VEREDAS possuía uma separação clara entre:

- Manual do Usuário — funcional;
- Manual do Operador Funcional — funcional;
- Manual de Suporte Técnico — técnico.

Os dois primeiros foram promovidos ao Google Drive e os arquivos no GitHub passaram a funcionar como ponteiros. O Manual de Suporte Técnico permaneceu no GitHub.

### 2. Manual do usuário não é sinônimo de README

README de repositório, instruções de build, setup, Docker, API, health check, comandos e desenvolvimento são documentação técnica mesmo quando descrevem como "usar" o software em contexto de engenharia.

### 3. Operador funcional e administrador técnico são papéis diferentes

- **Operador funcional:** Drive.
- **Administrador/implantador técnico:** GitHub.

Um documento que mistura os dois deve ser dividido.

### 4. Forks e documentação upstream não devem ser migrados automaticamente

Repositórios como SAPL, e-Cidade, Portal Modelo, Chatwoot e SEI podem carregar documentação do projeto de origem. Essa documentação não se torna automaticamente documentação funcional autoritativa do Sertão Digital.

O correto é manter upstream no GitHub e produzir no Drive somente a documentação funcional específica da implantação/produto do Sertão Digital.

### 5. Testes funcionais são híbridos

Casos de teste versionados, fixtures, cenários automatizados e matrizes executáveis permanecem no GitHub. A regra funcional e o resultado esperado que lhes dão origem devem estar no Drive.

## Estrutura funcional recomendada no Drive por produto

```text
PRODUTO/
├── 00_CONTROLE_FUNCIONAL/
├── 01_REFERENCIAS_ESTRATEGICAS/
├── 02_MANUAIS_DE_USUARIO/
│   ├── Manual do Usuário
│   ├── Manual do Operador Funcional
│   └── Guias por Perfil (quando necessário)
├── 03_REQUISITOS_E_REGRAS/
├── 04_PROCESSOS_E_FLUXOS/
└── 05_HANDOFFS_E_REVISOES/
```

A estrutura deve ser adaptada quando o produto já possuir taxonomia funcional oficial; não criar duplicação apenas para obedecer nomes de pastas.

## Estrutura técnica recomendada no GitHub

```text
docs/
├── architecture/
├── adr/
├── api/
├── deployment/
├── troubleshooting/
├── development/
└── functional-references/
```

Arquivos históricos de Manual do Usuário migrados podem permanecer no mesmo caminho como **PONTEIRO**, preservando links e histórico Git.

## Ordem recomendada de saneamento

### Prioridade A — produtos ativos com forte impacto funcional

1. `LegislaGD`
2. `SIGI-SD`
3. `Plenario-Digital-Core`
4. `VEREDAS` — concluir classificação dos testes híbridos
5. `Plataforma360`

### Prioridade B — produtos operacionais/comerciais

6. `NoticiaSertaneja`
7. `wpNoticiaSertaneja`
8. `Roteiro-Comercial`
9. `BOT-SD`

### Prioridade C — forks, upstream e referências

10. `SAPL-SD`
11. `PortalModelo-SD`
12. `e-Cidade-SD`
13. `Chatwoot-SD`
14. demais forks/repositórios de referência

## Regra de execução da migração

Para cada documento candidato:

```text
IDENTIFICAR
   ↓
CLASSIFICAR
   ↓
FUNCIONAL? ── sim ──> localizar/criar destino no Drive
   │                         ↓
   │                    migrar conteúdo
   │                         ↓
   │                    validar leitura
   │                         ↓
   │                    GitHub vira PONTEIRO
   │                         ↓
   │                       SYNCED
   │
   ├─ TÉCNICO ─────────────> manter GitHub
   │
   └─ HÍBRIDO ─────────────> separar autoridades + referências cruzadas
```

Não excluir histórico Git. Não migrar upstream de terceiros automaticamente. Não criar cópia editável concorrente.

## Próximas ações

1. Fazer revisão profunda dos repositórios de Prioridade A, começando por `LegislaGD` e `SIGI-SD`.
2. Identificar conteúdo funcional escondido sob nomes genéricos (`README`, `OPERACAO`, `FLUXO`, `GUIA`, `RUNBOOK`, `TESTE`, `PROCESSO`).
3. Migrar somente após classificação segura.
4. Registrar cada migração como `SYNCED`, `PENDING_SYNC`, `UNDER_REVIEW` ou `NO_CROSS_LAYER_IMPACT`.
5. Manter esta matriz como inventário técnico da auditoria no `SD-Knowledge`.
