# AGENTS.md

Bootstrap de contexto para Agentes de IA trabalhando no Sertão Digital.

---

## ⚡ Instruções Essenciais

Quando receber uma tarefa envolvendo Sertão Digital:

### 1. Carregar Contexto

- [ ] Leia o `README.md` para entender a SDKA
- [ ] Consulte `docs/SOURCE_OF_TRUTH.md` para hierarquia de fontes
- [ ] Identifique qual Skill é relevante
- [ ] Entenda que este arquivo é um bootstrap operacional e não uma fonte normativa
- [ ] Exemplos ilustrativos nunca substituem decisões oficiais ou ADRs reais

### 2. Skill Apropriada

Produtos e contextos exigem Skills específicas:

**Contexto Institucional e Arquitetura Geral:**
```
skills/sertaodigital-core/SKILL.md
```

**Plataforma Legislativa (LegislaGD e integração):**
```
skills/legislagd/SKILL.md
```

**Novos domínios:**
- Procure por `skills/[domain]/SKILL.md`
- Se não existir, registre a necessidade em uma issue

### 3. Consultar Manifestos

- `knowledge.yaml` — índice de conhecimento
- `sources.yaml` — registro de fontes de autoridade
- `products.yaml` — catálogo de produtos
- `repositories.yaml` — catálogo de repositórios

### 4. Validar Contra SOURCE_OF_TRUTH

Hierarquia de autoridade:

1. **Documento oficial vigente** (decisão formal)
2. **Documentação funcional oficial** (Google Drive)
3. **Documentação técnica** (GitHub)
4. **Manifestos SDKA**
5. **Knowledge Base derivada**
6. **Inferência do agente** (nunca substitua as acima)

⚠️ **Nunca invente decisões funcionais ou arquiteturais.**

### 5. Nunca Substituir Documentação Oficial

- Google Drive é **MASTER** para institucional/funcional
- GitHub é **MASTER** para técnico
- Markdown exportado é **DERIVADO** (referência apenas)
- Inferências nunca devem substituir fontes oficiais

### 6. Proteger Segredos

Antes de escrever, aplique a política READ / WRITE / ACCESS de `docs/SOURCE_OF_TRUTH.md`: falha de descoberta não significa inexistência; capacidade técnica de escrita não substitui autorização explícita; use menor privilégio e registre o estado de acesso padronizado.

- ❌ Não inclua tokens, senhas, credentials, secrets
- ❌ Não exponha dados sensíveis
- ❌ Consulte SECURITY.md para política

### 7. Registrar Mudanças Arquiteturais

Se você propõe uma mudança estrutural:

- Abra uma issue no GitHub
- Documente a decisão
- Solicite revisão
- Mantenha compatibilidade com projetos existentes

### 8. Compatibilidade

- Não quebre workflows existentes
- Mantenha retrocompatibilidade quando possível
- Comunique mudanças de breaking change
- Versione alterações (CHANGELOG.md)

### 9. Cross-Layer Impact Rule

**ANTES de encerrar uma alteração:**

1. **Verificar impacto na camada funcional** (Google Drive)
   - Esta mudança técnica afeta usuário/fluxo/operação?
   - Esta mudança requer mudança funcional?

2. **Verificar impacto na camada técnica** (GitHub)
   - Esta mudança funcional exige atualização técnica?
   - Código/arquitetura precisa mudar?

3. **Se há impacto cruzado E você tem acesso:**
   - ✅ Atualizar diretamente a outra camada na mesma atividade
   - Respeitar governança, fonte de verdade, versionamento

4. **Se há impacto cruzado E você NÃO tem acesso:**
   - ✅ Gerar **Prompt Handoff** para agente com acesso
   - Documentar em issue com tag `handoff`
   - Registrar em **PENDING_SYNC**

5. **Nunca deixar impacto cruzado conhecido sem registro:**
   - ❌ Não implemente apenas um lado
   - ✅ Sempre sincronize ou gere handoff
   - ✅ Registre se fica pendente

**Referência:** `docs/PROMPT_HANDOFF_STANDARD.md` e `docs/TECHNICAL_DECISION_GOVERNANCE.md`

### 10. Technical Decision Gate e GPT_SOURCE

- Antes de consolidar decisão técnica, execute `docs/TECHNICAL_DECISION_GOVERNANCE.md`
- Siga a descoberta e o roteamento de `GPT_SOURCE` definidos em `docs/SOURCE_OF_TRUTH.md`
- Um `GPT_SOURCE` é derivado e nunca decide arquitetura técnica isoladamente

---

## 📚 Recursos Rápidos

| Necessidade | Arquivo |
|---|---|
| Entender arquitetura | `docs/SDKA.md` |
| Hierarquia de fontes | `docs/SOURCE_OF_TRUTH.md` |
| Contexto institucional | `skills/sertaodigital-core/SKILL.md` |
| Contexto legislativo | `skills/legislagd/SKILL.md` |
| Índice de conhecimento | `knowledge.yaml` |
| Registro de fontes | `sources.yaml` |
| Catálogo de produtos | `products.yaml` |
| Catálogo de repositórios | `repositories.yaml` |
| Como contribuir | `CONTRIBUTING.md` |
| Segurança | `SECURITY.md` |

---

## 🔄 Fluxo Típico

```
Tarefa Recebida
    ↓
Identificar Domínio
    ↓
Carregar Skill Apropriada
    ↓
Consultar Manifestos
    ↓
Validar contra SOURCE_OF_TRUTH
    ↓
Executar Tarefa
    ↓
Documentar Mudanças
    ↓
Abrir PR (se aplicável)
```

---

## ⛔ O Que NÃO Fazer

- ❌ Inventar informações funcional/arquiteturais
- ❌ Substituir Google Drive com inferências
- ❌ Editar Markdown exportado como fonte oficial
- ❌ Commit secrets ou credentials
- ❌ Quebrar compatibilidade sem discussão
- ❌ Ignorar hierarquia de fontes
- ❌ Criar manifestos duplicados

---

## ✅ Boas Práticas

- ✅ Sempre validar contra SOURCE_OF_TRUTH.md
- ✅ Usar Skills para contexto de domínio
- ✅ Registrar mudanças em manifestos
- ✅ Manter compatibilidade
- ✅ Proteger segredos
- ✅ Comunicar breaking changes
- ✅ Descrever decisões e impacto
- ✅ Abrir issues para discussão

---

## 🚀 Começar Uma Tarefa

### Tarefa Simples (pequena mudança de documentação)

1. Carregue `README.md` e `CONTRIBUTING.md`
2. Execute mudança
3. Abra PR com descrição clara

### Tarefa Média (nova funcionalidade ou feature)

1. Carregue Skill apropriada
2. Consulte manifestos
3. Valide contra SOURCE_OF_TRUTH.md
4. Execute mudança
5. Registre em manifestos
6. Abra issue + PR

### Tarefa Grande (mudança arquitetural)

1. Carregue `docs/SDKA.md`
2. Consulte todas as Skills relevantes
3. Mapeie impacto em produtos/repositórios
4. Valide contra hierarquia de fontes
5. Abra issue para discussão
6. Documente ADR (Architecture Decision Record)
7. Abra PR com contexto completo
8. Aguarde revisão

---

## 📞 Suporte

Para questões não documentadas:

- Consulte `docs/` para especificações
- Verifique `skills/*/SKILL.md` para domínio
- Abra uma issue no GitHub
- Utilize canais institucionais oficiais do Sertão Digital

---

**Versão:** 1.0.0  
**Última atualização:** 2026-08-15
