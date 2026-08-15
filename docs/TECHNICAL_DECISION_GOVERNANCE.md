# Technical Decision Governance

Como decisões técnicas são tomadas e seu impacto é avaliado entre camadas.

---

## Princípio Central

Decisões técnicas não devem ser consolidadas com base apenas em:
- Chat e conversas informais
- Exportações de Drive
- Contexto fornecido por usuários
- Consenso verbal

**Devem passar por:**
1. Código atual
2. Arquitetura documentada
3. Architecture Decision Records (ADRs)
4. Referências e padrões
5. Histórico de git
6. Validação contra integração/compatibilidade

E **após** aprovação técnica: **Cross-Layer Impact Check**

---

## Fluxo de Decisão Técnica

```
Mudança Técnica Identificada
            ↓
    Carregue Contexto
    - AGENTS.md
    - Skills relevantes
    - Código
    - ADRs
            ↓
    Technical Decision Gate
            ↓
    Decisão Aprovada?
        ↙        ↘
       SIM        NÃO
        ↓         ↓
        v         REJEITAR
                 (ou revisar
                  pressuposto)
        ↓
    CROSS-LAYER
    IMPACT CHECK
        ↓
    Impacta funcional?
        ↙        ↘
       NÃO        SIM
        ↓         ↓
    FINISH       ↓
               Possui acesso
               ao Drive?
                  ↙    ↘
                 SIM     NÃO
                  ↓       ↓
               UPDATE   HANDOFF
               DRIVE    FUNCIONAL
                  ↓       ↓
                FINISH   FINISH
                        (agente
                         executa)
```

---

## Etapa 1: Technical Decision Gate

### O Que É

Análise formal antes de executar mudança técnica.

### Checklist

- [ ] **Código Atual**
  - Revisar código existente
  - Entender padrões em uso
  - Identificar dependências

- [ ] **Arquitetura**
  - Consultar docs/SDKA.md
  - Revisar documentação arquitetural
  - Entender componentes e fluxos

- [ ] **ADRs (Architecture Decision Records)**
  - Procurar decisões anteriores relacionadas
  - Entender rationale histórico
  - Validar compatibilidade com decisões existentes

- [ ] **Compatibilidade**
  - Manter compatibilidade upstream (se aplicável)
  - Não quebrar breaking change sem comunicação
  - Validar contra esquemas/APIs existentes

- [ ] **Integrações**
  - Que componentes dependem desta mudança?
  - Que componentes esta mudança afeta?
  - Quais repositórios precisam ser sincronizados?

- [ ] **Skills**
  - Carregue Skills relevantes
  - Validar decisão contra documentação de domínio
  - Atualizar Skills se necessário

### Exemplo: Technical Decision Gate

**Mudança Proposta:** Mudança de autenticação de JWT para SAML em LegislaGD

**Análise:**

1. **Código Atual**
   - ✅ Código em SAPL-SD usa JWT
   - ✅ Token salvo em localStorage (frontr)
   - ✅ Refresh token em cookie seguro

2. **Arquitetura**
   - ✅ Keycloak centralizado (já existe)
   - ✅ Protocolo OIDC suportado
   - ✅ SAML seria redundante se OIDC funciona

3. **ADRs**
   - ✅ ADR-2026-001: "Use Keycloak como IdP central"
   - ✅ ADR-2026-002: "Prefira OIDC para novos cliente"
   - ⚠️ SAML não foi decidido antes

4. **Compatibilidade**
   - ⚠️ Upstream SAPL usa JWT
   - ✅ Mas permite plugin de autenticação
   - ⚠️ PortalModelo precisa rodar sem Keycloak

5. **Integrações**
   - ✅ SIGI-SD usa Keycloak OIDC
   - ✅ e-Cidade-SD usa Keycloak OIDC
   - ✅ Todos podem usar OIDC

6. **Skills**
   - ✅ legislagd/references/identity.md documenta Keycloak
   - ✅ Menciona OIDC como protocolo
   - ✅ SAML não é mencionado

**Decisão:** ✅ **APROVADO COM RESTRIÇÃO**
- OIDC é suficiente
- SAML é redundante
- Manter padrão OIDC conforme ADRs
- Se necessário SAML: buscar caso de uso específico

---

## Etapa 2: Cross-Layer Impact Check

**Após** decisão técnica aprovada, **ANTES** de implementar:

### 1. Verificar Impacto

Pergunta-chave:

**"Esta mudança técnica afeta comportamento percebido pelo usuário?"**

---

### 2. Categorias de Mudança SEM impacto funcional

(Não requerem handoff)

- Refatoração interna
- Otimização de performance
- Mudança de banco de dados interno
- Mudança de estrutura de código
- Melhorias de logging
- Mudança de CI/CD
- Atualização de dependências (sem change behavior)

**Exemplo:**
- Refatorar autenticação JWT interno
- Permanecer compatível com API externa
- Usuário não nota mudança
- ❌ Sem handoff necessário

---

### 3. Categorias de Mudança COM impacto funcional

(Requerem handoff se sem acesso)

- Comportamento de API muda
- Fluxo percebido pelo usuário muda
- Nova funcionalidade acessível
- Remover funcionalidade acessível
- Mudança de permissões/acesso
- Mudança de integração de negócio
- Mudança de manual de operação
- Mudança de SLA/disponibilidade
- Novo requisito de dispositivo
- Mudança de formato de importação/exportação

**Exemplo:**
- Adicionar autenticação biométrica na API
- Nova capacidade que usuário acessa
- ✅ Handoff necessário para documentação de uso

---

### 4. Fluxo de Decisão

```
Mudança Técnica Aprovada
            ↓
Afeta funcionamento
percebido pelo usuário?
        ↙        ↘
       NÃO        SIM
        ↓         ↓
    FINISH     Acesso a Drive?
               (para atualizar)
                  ↙    ↘
                 SIM     NÃO
                  ↓       ↓
             ATUALIZAR  PROMPT
             DRIVE      HANDOFF
             DIRETO
                  ↓       ↓
              FINISH    PENDING
                        _SYNC
```

---

## Exemplo Completo: Technical Decision + Cross-Layer

### Cenário: Adicionar MFA em LegislaGD

**Passo 1: Technical Decision Gate**

```
Decisão: Implementar Time-based OTP (TOTP) para MFA

✅ Código: estudar autenticação atual
✅ Arquitetura: Keycloak suporta TOTP natively
✅ ADRs: compatível com ADR-2026-001 (Keycloak)
✅ Compatibilidade: não quebra cliente JWT
✅ Integrações: SIGI-SD também pode usar
✅ Skills: legislagd/references/identity.md menciona MFA

Resultado: APROVADO
```

**Passo 2: Cross-Layer Impact Check**

```
Pergunta: Afeta funcionamento percebido pelo usuário?

Resposta: SIM
- Usuário precisa gerar código TOTP
- Novo passo no login
- Nova política de segurança

Pergunta: Acesso ao Drive?

Resposta: SIM (estamos executando)

Ação: Atualizar Drive diretamente
- Atualizar manual de operação
- Avisar RH sobre nova política
- Adicionar procedimento de setup MFA
```

**Passo 3: Implementação**

1. **Código** (GitHub)
   - Integrar biblioteca TOTP
   - Atualizar API de login
   - Armazenar secrets com segurança
   - Testes de integração

2. **Documentação** (GitHub)
   - API Reference
   - Skill legislagd
   - Documentação técnica

3. **Drive** (Simultaneamente)
   - Manual de operação
   - Procedimento passo-a-passo
   - FAQ de MFA
   - Notificar RH

4. **PR**
   - Título: "feat: add MFA (TOTP) for user authentication"
   - Descrição referencia impacto cruzado
   - Links para PR e documentação Drive
   - Validação de sincronização completa

---

## Fluxo SEM Acesso Direto

### Cenário: Agente GitHub identifica mudança, mas sem acesso ao Drive

**Situação:**
- Implementou MFA em código (GitHub)
- Sabe que afeta usuários (novo procedimento de login)
- Não tem acesso direto ao Google Drive

**Ação:**

1. **Criar TECHNICAL HANDOFF** (Prompt Handoff)
   - ID: 2026-08-15-TECHNICAL-002
   - Origem: GitHub (código implementado)
   - Destino: Drive (documentação)
   - Tipo: FUNCTIONAL HANDOFF (para agente Drive)

2. **Handoff contém:**
   - Código está pronto (link PR)
   - Mudança percebida: novo passo "MFA"
   - Documentação necessária:
     - Manual: Procedimento de setup MFA
     - FAQ: Perguntas sobre TOTP
     - RH: Nova política de segurança
   - Instruções: Atualizar manual no Drive conforme template

3. **Registrar PENDING_SYNC:**
   ```yaml
   pending_sync:
     handoff_id: 2026-08-15-TECHNICAL-002
     product: legislagd
     status: PENDING
     blocking: false  # PR pode merge, mas handoff pende
     assigned_to: null (agente Drive)
     expected: 2026-08-22
   ```

4. **Entregar ao agente Drive:**
   - Criar issue no GitHub: `kind:handoff target:drive`
   - Referenciar Prompt Handoff
   - Agente Drive executa e confirma

---

## ADRs (Architecture Decision Records)

### O Que É

Um ADR documenta:
- Decisão técnica importante
- Contexto (por que foi necessária)
- Alternativas consideradas
- Decisão aprovada
- Consequências (impactos)

### Quando Criar

- Decisão afeta múltiplos componentes
- Decisão é reversível?
- Impacto de segurança
- Tradeoff entre alternativas

### Não É Necessário

- Bug fixes
- Pequenas refatorações
- Atualizações de dependências

### Template (Minimal)

```markdown
# ADR-YYYY-NNN: [Título]

**Data:** [ISO 8601]

## Contexto

[Por que foi necessária]

## Decisão

[O que foi decidido]

## Alternativas Consideradas

- [ ] Alternativa 1 (por que rejeitada)
- [ ] Alternativa 2 (por que rejeitada)
- [x] Alternativa 3 (ESCOLHIDA)

## Consequências

**Positivas:**
- ...

**Negativas:**
- ...

## Impacto Cruzado

- Drive: [se houver]
- Produtos: [afetados]
```

### Armazenamento

ADRs devem estar em:
- GitHub: `/docs/adr/` ou similar
- Versionado com git
- Referenciado em Skills quando aplicável

---

## Integration with Skills

Skills devem referenciar:

- **decision_records:** lista de ADRs relevantes
- **technical_decisions:** resumo de decisões importantes
- **compatibility_notes:** como mudanças afetam downstream

**Exemplo em Skill:**

```yaml
---
name: legislagd
decision_records:
  - adr-2026-001-keycloak-idp
  - adr-2026-002-oidc-preferred
---

## Decisões Técnicas Importantes

- [x] Keycloak centralizado (ADR-2026-001)
- [x] OIDC é protocolo padrão (ADR-2026-002)
- [ ] MFA será implementado T3 2026
```

---

## Validation Checklist

Antes de marcar como "APPROVED":

- [ ] Technical Decision Gate concluído
- [ ] Cross-Layer Impact Check concluído
- [ ] Se há impacto funcional: Access-Aware Handoff criado
- [ ] Se sem acesso: PENDING_SYNC registrado
- [ ] ADR criado (se decisão maior)
- [ ] Skills atualizadas (se aplicável)
- [ ] Código está pronto para PR
- [ ] Documentação planejada
- [ ] Sem secrets expostos
- [ ] Compatibilidade validada

---

## Summary

**Decisão técnica ≠ Decisão isolada**

```
Technical Decision
        ↓
Technical Decision Gate
        ↓
Cross-Layer Impact Check
        ↓
        ├─→ Sem impacto → FINISH
        └─→ Com impacto → Access-Aware Handoff
                ├─→ Com acesso → UPDATE DIRETO
                └─→ Sem acesso → PROMPT HANDOFF
```

---

**Versão:** 1.0.0  
**Última atualização:** 2026-08-15
