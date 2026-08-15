# Cross-Layer Synchronization Flows

Diagramas visuais dos fluxos de sincronização bidirecional entre camadas funcional e técnica.

---

## Fluxo Principal: Decisão com Impacto Cruzado

```mermaid
flowchart TD
    A["Mudança identificada"] --> B{"Impacta outra<br/>camada?"}
    B -->|Não| C["✅ FINISH"]
    B -->|Sim| D{"Possui acesso<br/>à camada<br/>destino?"}
    D -->|Sim| E["✅ Atualizar diretamente"]
    D -->|Não| F["✅ Gerar Prompt Handoff"]
    E --> G["Validar consistência<br/>entre camadas"]
    F --> H["Registrar PENDING_SYNC"]
    G --> C
    H --> C
```

---

## Fluxo Técnico: Technical Decision Gate + Cross-Layer Check

```mermaid
flowchart TD
    A["Mudança Técnica<br/>Identificada"] --> B["Carregue Contexto<br/>AGENTS.md, Skills, Código"]
    B --> C["Technical Decision<br/>Gate"]
    C --> D{"Decisão<br/>Aprovada?"}
    D -->|Não| E["Rejeitar ou<br/>Revisar"]
    D -->|Sim| F["CROSS-LAYER<br/>IMPACT CHECK"]
    F --> G{"Afeta funcionamento<br/>percebido pelo<br/>usuário?"}
    G -->|Não| H["✅ FINISH<br/>Implementar no GitHub"]
    G -->|Sim| I{"Acesso<br/>ao Drive?"}
    I -->|Sim| J["✅ Atualizar Drive<br/>Documentação/Manual"]
    I -->|Não| K["✅ PROMPT HANDOFF<br/>Functional"]
    J --> L["Validar Sincronização"]
    K --> M["Registrar PENDING_SYNC"]
    L --> N["✅ FINISH"]
    M --> O["Agente Drive<br/>Executa"]
    O --> N
```

---

## Fluxo Funcional: Functional Change Gate + Cross-Layer Check

```mermaid
flowchart TD
    A["Mudança Funcional<br/>Identificada<br/>(Google Drive)"] --> B["Identificar Impacto<br/>Técnico Necessário"]
    B --> C{"Impacta<br/>Técnico?"}
    C -->|Não| D["✅ FINISH<br/>Update Drive apenas"]
    C -->|Sim| E["FUNCTIONAL<br/>CHANGE GATE"]
    E --> F["Carregue Contexto<br/>Skills, Código, ADRs"]
    F --> G["Technical Decision"]
    G --> H{"Acesso<br/>ao GitHub?"}
    H -->|Sim| I["✅ Atualizar GitHub<br/>Código/Docs/Skills"]
    H -->|Não| J["✅ PROMPT HANDOFF<br/>Technical"]
    I --> K["Validar Sincronização"]
    J --> L["Registrar PENDING_SYNC"]
    K --> M["✅ FINISH"]
    L --> N["Agente GitHub<br/>Executa"]
    N --> M
```

---

## Sincronização Bidirecional: Visão Completa

```mermaid
flowchart LR
    A["Google Drive<br/>(Master Funcional)<br/><br/>• Estratégia<br/>• Requisitos<br/>• Fluxos<br/>• Políticas"] -->|Mudança<br/>Funcional| B{"Impacta<br/>Técnico?"}
    
    B -->|Não| C["Apenas Drive<br/>Atualizado"]
    C --> D["✅ Fim"]
    
    B -->|Sim| E{"Acesso<br/>GitHub?"}
    E -->|Sim| F["Atualizar GitHub<br/>• Código<br/>• Docs<br/>• Skills"]
    E -->|Não| G["TECHNICAL<br/>HANDOFF"]
    
    F --> H["Validar"]
    G --> I["PENDING_SYNC"]
    
    H --> J["GitHub<br/>(Master Técnico)<br/><br/>• Arquitetura<br/>• Código<br/>• Skills<br/>• ADRs"]
    I --> J
    
    J -->|Mudança<br/>Técnica| K{"Afeta<br/>Funcional?"}
    
    K -->|Não| L["Apenas GitHub<br/>Atualizado"]
    L --> D
    
    K -->|Sim| M{"Acesso<br/>Drive?"}
    M -->|Sim| N["Atualizar Drive<br/>• Documentação<br/>• Manuais<br/>• Políticas"]
    M -->|Não| O["FUNCTIONAL<br/>HANDOFF"]
    
    N --> P["Validar"]
    O --> Q["PENDING_SYNC"]
    
    P --> A
    Q --> A
```

---

## Fluxo de Prompt Handoff

```mermaid
flowchart TD
    A["Identificar<br/>Impacto Cruzado"] --> B["SEM acesso à<br/>camada destino?"]
    B -->|Não| C["Atualizar direto"]
    B -->|Sim| D["GERAR PROMPT<br/>HANDOFF"]
    
    D --> E["Estruturar<br/>Handoff<br/><br/>• ID único<br/>• Origem/Destino<br/>• Contexto<br/>• Mudança necessária<br/>• Critérios validação"]
    
    E --> F["Documentar em<br/>• Issue GitHub<br/>• ou docs/handoffs/"]
    
    F --> G["Registrar<br/>PENDING_SYNC<br/><br/>Status: PENDING"]
    
    G --> H["Atribuir a<br/>agente receptor"]
    
    H --> I["Agente Receptor<br/>Recebe Handoff"]
    
    I --> J["Executar mudança<br/>na camada destino"]
    
    J --> K["Validar contra<br/>critérios"]
    
    K --> L{"Passou<br/>validação?"}
    
    L -->|Sim| M["Atualizar PENDING_SYNC<br/>Status: COMPLETED"]
    L -->|Não| N["Reportar bloqueadores"]
    
    N --> O["Discutir com<br/>autor handoff"]
    
    M --> P["✅ SYNC<br/>COMPLETO"]
    O --> Q["Revisar handoff"]
    Q --> J
```

---

## Matriz de Decisão: Access-Aware Handoff

```mermaid
graph TD
    A["Mudança em uma<br/>camada"] --> B{"Impacta<br/>outra camada?"}
    
    B -->|NÃO| C["Nenhuma ação<br/>de handoff"]
    
    B -->|SIM| D{"Acesso à<br/>camada destino?"}
    
    D -->|SIM| E["UPDATE TARGET<br/>LAYER DIRECTLY<br/><br/>✅ Na mesma atividade<br/>✅ Respeitar governança<br/>✅ Sincronizar versão"]
    
    D -->|NÃO| F["GENERATE PROMPT<br/>HANDOFF<br/><br/>✅ Obrigatório<br/>✅ Estruturado<br/>✅ PENDING_SYNC"]
    
    E --> G["VALIDATE<br/>CROSS-LAYER<br/>CONSISTENCY"]
    F --> H["REGISTER<br/>PENDING_SYNC"]
    
    G --> I["✅ Mudança<br/>Completa"]
    H --> J["Agente com acesso<br/>recebe e executa"]
    J --> I
    
    C --> I
```

---

## Status de PENDING_SYNC

```mermaid
stateDiagram-v2
    [*] --> PENDING: Handoff gerado
    
    PENDING --> IN_PROGRESS: Agente começou
    PENDING --> CANCELLED: Necessidade cancelada
    
    IN_PROGRESS --> COMPLETED: Mudança validada
    IN_PROGRESS --> PENDING: Bloqueador encontrado
    
    COMPLETED --> [*]: Sincronização completa
    CANCELLED --> [*]: Não necessária
```

---

## Fluxo de Sincronização Drive ↔ GitHub

```mermaid
sequenceDiagram
    participant D as Google Drive<br/>Master Funcional
    participant A as Agente/Dev
    participant G as GitHub<br/>Master Técnico
    
    Note over D,G: Fluxo: Funcional → Técnico
    
    D ->> A: Mudança funcional<br/>(novo requisito)
    A ->> A: Avaliar impacto técnico
    
    alt Com acesso ao GitHub
        A ->> G: Atualizar código + docs
        A ->> A: Validar sincronização
        G ->> A: ✅ Sincronizado
    else Sem acesso ao GitHub
        A ->> A: Gerar TECHNICAL HANDOFF
        A ->> G: Issue com handoff (tag: handoff)
        A ->> A: Registrar PENDING_SYNC
        G ->> G: Agente técnico executa
        G ->> A: ✅ Sincronizado
    end
    
    Note over D,G: Fluxo: Técnico → Funcional
    
    G ->> A: Mudança técnica<br/>(novo endpoint)
    A ->> A: Avaliar impacto funcional
    
    alt Com acesso ao Drive
        A ->> D: Atualizar manual/docs
        A ->> A: Validar sincronização
        D ->> A: ✅ Sincronizado
    else Sem acesso ao Drive
        A ->> A: Gerar FUNCTIONAL HANDOFF
        A ->> D: Drive comment/doc
        A ->> A: Registrar PENDING_SYNC
        D ->> D: Agente funcional executa
        D ->> A: ✅ Sincronizado
    end
```

---

## Checklist de Sincronização

```mermaid
flowchart TD
    A["Antes de encerrar<br/>uma mudança"] --> B["1. Mudança identifi-<br/>cada em uma camada"]
    
    B --> C["2. Verificar impacto<br/>na outra camada"]
    
    C --> D{"3. Há impacto<br/>cruzado?"}
    
    D -->|Não| E["Fin fim"]
    D -->|Sim| F{"4. Possui acesso?"}
    
    F -->|Sim| G["5. Atualizar<br/>diretamente"]
    F -->|Não| H["5. Gerar Handoff"]
    
    G --> I["6. Validar<br/>consistência"]
    H --> J["6. Registrar<br/>PENDING_SYNC"]
    
    I --> K["7. Nunca deixar<br/>divergência consciente"]
    J --> K
    
    K --> L["✅ Mudança<br/>Completa"]
```

---

## Exemplos Visuais

### Exemplo 1: Novo Fluxo Legislativo (Funcional → Técnico com Acesso)

```mermaid
flowchart LR
    A["Google Drive<br/>Novo Fluxo 3-stage<br/>(Pré-análise,<br/>Análise, Votação)"]
    
    B["Agente identifica<br/>impacto técnico"]
    
    C["✅ Tem acesso GitHub?<br/>SIM"]
    
    D["Technical Decision Gate<br/>• Revisa código SAPL<br/>• Valida ADRs<br/>• Aprova design"]
    
    E["Implementa em<br/>GitHub<br/>• DB migration<br/>• API endpoints<br/>• Testes"]
    
    F["Atualiza Skill<br/>legislagd<br/>• references/domain.md<br/>• manifests/product.yaml"]
    
    G["Pull Request<br/>com contexto<br/>cruzado"]
    
    H["✅ SINCRONIZADO<br/>Drive + GitHub"]
    
    A --> B --> C --> D --> E --> F --> G --> H
```

### Exemplo 2: Nova Autenticação Biométrica (Técnico → Funcional sem Acesso)

```mermaid
flowchart LR
    A["GitHub<br/>Nova autenticação<br/>biométrica<br/>(implementada)"]
    
    B["Agente GitHub<br/>identifica impacto<br/>funcional"]
    
    C["❌ Tem acesso Drive?<br/>NÃO"]
    
    D["Gera FUNCTIONAL<br/>HANDOFF<br/>• Como usar<br/>• Compatibilidade<br/>• Consentimento LGPD"]
    
    E["Registra PENDING_SYNC<br/>ID: 2026-08-15-FUNC-001<br/>Status: PENDING"]
    
    F["Issue GitHub<br/>tag: handoff:functional<br/>referencia Handoff"]
    
    G["Agente Drive<br/>recebe Handoff"]
    
    H["Atualiza Google Drive<br/>• Manual operacional<br/>• FAQ<br/>• Aviso RH"]
    
    I["PENDING_SYNC<br/>Status: COMPLETED"]
    
    A --> B --> C --> D --> E --> F --> G --> H --> I
```

---

## Legenda de Cores (Mermaid)

- 🟢 **Verde:** Ação executada, sucesso
- 🟠 **Laranja:** Decisão, ponto de escolha
- 🔴 **Vermelho:** Bloqueador, rejeição
- 🟡 **Amarelo:** Aguardando ação externa
- 🔵 **Azul:** Informação, referência

---

**Versão:** 1.0.0  
**Última atualização:** 2026-08-15
