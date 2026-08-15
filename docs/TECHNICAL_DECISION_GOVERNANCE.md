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

### Exemplo Hipotético: Technical Decision Gate

> O exemplo abaixo é fictício e serve apenas para demonstrar o fluxo do Technical Decision Gate. Não representa uma decisão oficial do Sertão Digital.

**Mudança Proposta:** Exemplo ilustrativo de troca de autenticação em um sistema de referência genérico.

**Análise:**

1. **Código Atual**
   - ✅ Sistema A usa token de sessão em fluxo interno
   - ✅ Fluxo de refresh é gerenciado por serviço dedicado
   - ✅ A biblioteca específica pode variar conforme repositório

2. **Arquitetura**
   - ✅ Existe um provedor central de identidade
   - ✅ Protocolo de integração é definido por repositório
   - ✅ Alternativa específica deve ser validada antes da adoção

3. **ADRs**
   - ✅ Existe ADR documentado no repositório correspondente
   - ✅ A decisão real deve ser consultada no histórico do código
   - ⚠️ Exemplo não substitui ADR real

4. **Compatibilidade**
   - ⚠️ Repositório de origem pode ter requisitos específicos
   - ✅ A mudança deve preservar comportamento compatível
   - ⚠️ Implementação depende da análise técnica local

5. **Integrações**
   - ✅ Múltiplos módulos podem depender do mesmo padrão
   - ✅ Integrações devem ser avaliadas por repositório e contexto

6. **Skills**
   - ✅ A Skill deve refletir padrão institucional válido
   - ✅ Exemplo não deve ser tratado como regra universal

**Decisão:** ✅ **EXEMPLO ILUSTRATIVO**
- A alternativa específica precisa ser validada em ADR ou repositório real
- Exemplos hipotéticos nunca substituem decisão versionada
- O padrão correto depende do contexto técnico do produto

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

### Cenário Ilustrativo: Adicionar MFA em Produto Genérico

> Este cenário é hipotético e não representa uma decisão real do Sertão Digital.

**Passo 1: Technical Decision Gate**

```
Decisão: Implementar mecanismo de autenticação multifator em um sistema genérico.

✅ Código: analisar autenticação atual
✅ Arquitetura: validar provedor de identidade existente
✅ ADRs: consultar decisão versionada do repositório
✅ Compatibilidade: preservar fluxos compatíveis
✅ Integrações: avaliar módulos dependentes
✅ Skills: refletir contexto do produto e regras de acesso

Resultado: APROVADO SOMENTE SE VALIDADO
```

**Passo 2: Cross-Layer Impact Check**

```
Pergunta: Afeta funcionamento percebido pelo usuário?

Resposta: DEPENDE DO CONTEXTO
- Pode exigir novo passo de autenticação
- Pode demandar atualização operacional
- Pode exigir comunicação de uso

Pergunta: Acesso ao Drive?

Resposta: VARIA

Ação: Atualizar documentação funcional ou gerar handoff
- Atualizar manual de operação
- Ajustar FAQ ou procedimento de onboarding
- Registrar impacto no repositório correto
```

**Passo 3: Implementação**

1. **Código** (GitHub)
   - Validar biblioteca e prova de conceito
   - Atualizar API de login apenas se necessário
   - Manter segredos fora do repositório
   - Realizar testes de integração

2. **Documentação** (GitHub)
   - Atualizar documentação técnica relevante
   - Ajustar Skills ou referência do produto
   - Registrar impacto e compatibilidade

3. **Drive** (quando aplicável)
   - Atualizar manual operacional ou processo funcional
   - Registrar procedimento somente se houver decisão formal
   - Não usar exemplo como fato

4. **PR**
   - Título: "feat: add authentication hardening if validated"
   - Descrição referenciando regras de gate e impacto cruzado
   - Links para ADRs e contexto autorizados

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

**Exemplo em Skill (ilustrativo):**

```yaml
---
name: legislagd
status: active
decision_records:
  - example-adr-001-identity-provider
  - example-adr-002-protocol-selection
---

## Decisões Técnicas Importantes

- [x] Identidade centralizada do produto deve ser determinada por repositório e decisão versionada
- [x] Protocolo deve seguir análise técnica específica do produto
- [ ] Novas decisões exigem ADR real antes de consolidação
```

> O bloco acima é ilustrativo e não representa ADR real do projeto.

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
