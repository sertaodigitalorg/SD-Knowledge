# Política Técnica de Sincronização Documental — SDKA

**Status:** PADRÃO OFICIAL  
**Data:** 2026-08-26  
**Repositório:** `sertaodigitalorg/SD-Knowledge`  
**Escopo:** padrão oficial de desenvolvimento, documentação e sincronização entre as camadas funcional e técnica do Sertão Digital.

## 1. Princípio central

O desenvolvimento do Sertão Digital opera com duas fontes autoritativas complementares:

- **Google Drive — MASTER funcional/institucional**: requisitos, regras de negócio, processos, políticas, decisões institucionais, documentação funcional, Manual do Usuário, Manual do Operador e demais guias orientados ao uso e comportamento esperado.
- **GitHub — MASTER técnico**: código, arquitetura, ADRs, APIs, infraestrutura, deploy, CI/CD, troubleshooting técnico, documentação para desenvolvedores, Skills, Agents e artefatos técnicos versionados.

O critério de classificação é a **natureza da informação**, não a ferramenta, agente ou ambiente que a produziu.

## 2. Agentes e ambientes

ChatGPT, VS Code/Codex e agentes equivalentes podem atuar como consumidores e mantenedores das duas camadas quando possuírem acesso autorizado.

O fluxo preferencial é acesso direto às fontes oficiais, evitando cópia e cola manual de contexto como mecanismo rotineiro:

```text
                 Desenvolvimento / Agentes
                    ChatGPT | VS Code
                           |
             +-------------+-------------+
             |                           |
             v                           v
      Google Drive                    GitHub
    MASTER FUNCIONAL               MASTER TÉCNICO
             |                           |
             +-------------+-------------+
                           |
                          SDKA
```

Nenhum agente se torna fonte de verdade por possuir capacidade de leitura ou escrita.

## 3. Cross-Layer Impact Check

Toda alteração relevante deve avaliar impacto na camada complementar.

### Funcional → Técnico

Mudanças em requisitos, processos, regras de negócio, políticas ou comportamento esperado devem verificar impacto em arquitetura, código, APIs, testes, Skills, ADRs e documentação técnica.

### Técnico → Funcional

Mudanças em código, arquitetura, autenticação, integrações, APIs ou operação técnica devem verificar impacto em comportamento percebido, processos, requisitos, documentação funcional e Manual do Usuário.

Uma atividade somente poderá ser considerada **documentalmente sincronizada** após essa avaliação.

Nem toda alteração exige escrita nas duas fontes; toda alteração relevante exige verificar a outra camada.

## 4. Manual do Usuário

O **Manual do Usuário** e documentos equivalentes orientados ao uso pertencem ao **Google Drive / MASTER funcional**.

Incluem, entre outros:

- como utilizar funcionalidades;
- comportamento esperado do sistema;
- fluxos operacionais;
- papéis percebidos pelo usuário;
- procedimentos do operador;
- regras apresentadas ao usuário;
- orientações funcionais.

Permanecem no GitHub / MASTER técnico:

- instalação;
- deploy;
- infraestrutura;
- APIs;
- troubleshooting técnico;
- configuração técnica;
- documentação para desenvolvedores.

O GitHub pode manter referências para o Manual do Usuário, mas não uma segunda cópia editável concorrente como fonte oficial.

## 5. Sincronização direta

Quando o agente que executa a atividade possui acesso autorizado à camada impactada, deve preferencialmente atualizar diretamente o MASTER correspondente na mesma atividade, respeitando permissões, governança, revisão e versionamento.

Exemplo:

```text
Mudança funcional no Drive
        |
        v
Cross-Layer Impact Check
        |
        +--> impacto técnico? --> atualizar GitHub

Mudança técnica no GitHub
        |
        v
Cross-Layer Impact Check
        |
        +--> impacto funcional? --> atualizar Drive / Manual
```

A sincronização direta reduz divergências e elimina a necessidade de transportar manualmente contexto entre ChatGPT e VS Code como rotina.

## 6. Prompt Handoff — mecanismo resiliente

O **Prompt Handoff permanece oficial e não é eliminado** pela sincronização direta.

Ele funciona como mecanismo de contingência, revisão, transferência controlada e recuperação.

Deve ser utilizado quando:

1. a camada de destino estiver indisponível;
2. houver falha de autenticação, permissão, API, conector ou automação;
3. o agente não possuir capacidade de escrita na fonte de destino;
4. a alteração exigir revisão humana ou especializada antes da consolidação;
5. houver transferência entre agentes, ambientes ou responsáveis;
6. for necessário preservar um pacote explícito de contexto para auditoria, validação ou retomada posterior;
7. a sincronização direta falhar total ou parcialmente.

Quando houver impacto cruzado não sincronizado, registrar `PENDING_SYNC` conforme o padrão vigente.

Princípio operacional:

> **Sincronização direta é o caminho preferencial; Prompt Handoff é o mecanismo resiliente de fallback, revisão e recuperação.**

A falha da automação nunca autoriza divergência silenciosa entre os MASTERS.

## 7. Não duplicação de autoridade

Não criar duas fontes editáveis concorrentes para a mesma informação.

Podem existir:

- referências;
- links;
- índices;
- exportações;
- caches;
- contexto compilado para IA.

Esses artefatos devem indicar sua natureza derivada e apontar para o MASTER correspondente.

## 8. Estados de sincronização

Uma mudança com impacto cruzado deve ser tratada conceitualmente como:

- `SYNCED` — impacto avaliado e fontes necessárias alinhadas;
- `NO_CROSS_LAYER_IMPACT` — impacto cruzado avaliado e inexistente;
- `PENDING_SYNC` — existe atualização pendente na outra camada;
- `SYNC_BLOCKED` — sincronização impedida por acesso, serviço, revisão ou dependência externa;
- `UNDER_REVIEW` — atualização cruzada preparada, aguardando validação.

## 9. Regra para agentes de IA

Antes de concluir uma alteração relevante, o agente deve:

1. identificar a natureza da informação;
2. localizar o MASTER correto;
3. consultar a fonte autoritativa quando disponível;
4. executar a alteração autorizada;
5. realizar o Cross-Layer Impact Check;
6. atualizar diretamente a outra camada quando houver impacto e acesso autorizado;
7. validar consistência entre as fontes alteradas;
8. usar Prompt Handoff + `PENDING_SYNC` quando a sincronização direta não puder ser concluída;
9. informar o estado final da sincronização.

## 10. Relação com a governança existente

Esta política complementa `docs/SOURCE_OF_TRUTH.md` e a Política de Governança do Conhecimento mantida no Google Drive.

Em caso de conflito, aplica-se a autoridade por domínio definida em `SOURCE_OF_TRUTH.md`: Drive governa conteúdo funcional/institucional e GitHub governa conteúdo técnico.

## 11. Resultado esperado

O padrão de desenvolvimento do Sertão Digital passa a operar com documentação viva e coordenada:

```text
Regra / Processo / Manual
        Drive
          |
          v
 Desenvolvimento
 ChatGPT / VS Code
          |
          v
 Código / ADR / API
        GitHub
          |
          v
 Cross-Layer Check
          |
     +----+----+
     |         |
   SYNCED   HANDOFF
             |
        PENDING_SYNC
```

O objetivo é preservar coerência entre o que o produto **deve fazer**, o que o usuário **entende e utiliza** e o que o software **efetivamente implementa**.

## 12. Adoção oficial

A partir de 2026-08-26, esta política é adotada como **padrão oficial de desenvolvimento e sincronização documental do ecossistema Sertão Digital**.

Novos produtos, novas Skills, novos Agents e fluxos de manutenção deverão adotar este padrão por default. Exceções devem ser justificadas e registradas na camada autoritativa correspondente.
