# Segurança e Privacidade

Políticas de segurança para SD-Knowledge e operação do Sertão Digital.

---

## Repositório Público

Este repositório é **público**. Portanto:

### ❌ NUNCA Commit

- Tokens de autenticação (JWT, OAuth, API keys)
- Senhas ou passphrases
- Chaves privadas (SSH, TLS, PGP)
- Credenciais (banco de dados, cloud)
- Configuração local com segredos (`.env` com dados reais)
- Dados pessoais (PII — emails, IDs, endereços)
- CNPJ ou dados sensíveis desnecessários
- Contratos ou documentos jurídicos restritos
- Links com tokens embutidos
- Credenciais de APIs de terceiros
- Endpoints administrativos internos sensíveis
- Informações de infraestrutura interna crítica

### ✅ Use Alternativas

**Para credenciais:**
- Variáveis de ambiente (.env, .env.local em .gitignore)
- Secrets do GitHub Actions
- Vaults locais (HashiCorp Vault, etc)
- Gestores de secrets (1Password, LastPass, etc)

**Para configuração de exemplo:**
- `.example.env` (sem valores reais)
- `config.example.yaml` (com placeholders)
- Documentação de "como configurar"

**Para dados sensíveis:**
- Google Drive privado (Acervo Institucional)
- Sistema seguro de gestão de documentos
- Nunca em repositório público

---

## Detecção Automática

Este repositório possui validação automática para detectar:

- Padrões comuns de secrets (AWS keys, GitHub tokens, etc)
- Credenciais conhecidas
- Estruturas suspeitas

**Mas você é responsável:**
- ✅ Revisar seu código antes de commit
- ✅ Não confiar 100% em detecção automática
- ✅ Reportar falsos negativos

---

## Reportar Vulnerabilidades

Se você descobre vulnerabilidade de segurança:

### ❌ NÃO Faça

- Não abra issue pública
- Não post em foruns públicos
- Não envie em PR
- Não mencione em conversas públicas

### ✅ Faça

- Utilize os canais institucionais oficiais do Sertão Digital
- Reporte via email direto a responsável de segurança
- Forneça detalhes técnicos (sem expor exploits)
- Aguarde orientação antes de divulgar

---

## Conformidade Legal

### LGPD (Lei Geral de Proteção de Dados)

- Nenhum dado pessoal (PII) em repositório público
- Consentimento para coletar dados
- Direitos dos titulares e hipóteses de eliminação, retenção e tratamento conforme LGPD e obrigações legais aplicáveis
- Dados minimizados
- Transparência em política de privacidade

### Produtos com Dados de Cidadão

Documentações de produtos que lidam com dados de cidadão devem:

- [ ] Descrever coleta de dados
- [ ] Explicar armazenamento
- [ ] Explicar retenção
- [ ] Descrever direitos do cidadão
- [ ] Indicar conformidade com LGPD

Exemplos:
- SIGI-SD (atendimento ao cidadão)
- PortalModelo-SD (consulta pública, mas sem dados pessoais)

---

## Segurança de Dependências

Ao adicionar dependências externas (npm, pip, etc):

- [ ] Verifique reputação e manutenção
- [ ] Verifique licença (compatível com projeto)
- [ ] Procure por vulnerabilidades conhecidas
- [ ] Revise mudanças recentes
- [ ] Considere alternativas mais seguras
- [ ] Use versões pinned (não `*` ou `latest`)

### Ferramentas de Validação

- `npm audit`
- `pip install safety`
- `cargo audit`
- GitHub Dependabot (nativo)
- Snyk (opcional)

---

## Práticas de Desenvolvimento Seguro

### Código

- ✅ Input validation
- ✅ Output encoding
- ✅ Prepared statements (SQL)
- ✅ HTTPS/TLS
- ✅ Autenticação forte
- ✅ Autorização granular (RBAC)
- ✅ Auditoria de ações críticas
- ❌ Comentários com segredos
- ❌ Hardcoded credentials
- ❌ Desserialização sem validação

### Logs

- ✅ Log de eventos de segurança
- ✅ Armazenar logs de forma segura
- ✅ Período de retenção apropriado
- ✅ Anonimizar dados pessoais em logs
- ❌ Não log de senhas/tokens
- ❌ Não log de dados pessoais desnecessários

### Deployment

- ✅ Variáveis de ambiente para configuração
- ✅ Controle de acesso ao ambiente
- ✅ Segregação de ambientes (dev/staging/prod)
- ✅ Backup e recovery testados
- ✅ Plano de incidente
- ❌ Senhas em arquivos de configuração
- ❌ Acesso público a banco de dados
- ❌ Debug mode em produção

---

## Segurança de Drive

Documentação no Google Drive (Acervo Institucional):

- [ ] Apenas pessoas autorizadas têm acesso
- [ ] Estrutura clara de permissões
- [ ] Dados sensíveis protegidos
- [ ] Backup regular
- [ ] Auditoria de acesso
- [ ] Versioning de documentos

---

## Incidente de Segurança

Se você comete erro e expõe secret:

1. **Imediatamente:** Revocar a credencial (se possível)
2. **Comunicar:** Informe ao time de segurança
3. **Remediar:** Remover do histórico git (se necessário)
4. **Aprender:** Analise o que deu errado

---

## Privacidade em Skills e Documentação

Ao criar Skills ou documentação:

- ✅ Explicite o que é público vs privado
- ✅ Descrever proteção de dados
- ✅ Indicar conformidade com regulações
- ✅ Anonimizar exemplos com dados pessoais
- ❌ Não use dados pessoais reais em exemplos
- ❌ Não documente segredos de produção

---

## Recursos

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [LGPD — Lei Geral de Proteção de Dados](https://www.gov.br/cidadania/pt-br/acesso-a-informacao/lgpd)
- [GitHub Security](https://docs.github.com/en/code-security)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

---

**Versão:** 1.0.0  
**Última atualização:** 2026-08-15
