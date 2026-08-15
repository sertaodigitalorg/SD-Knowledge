# Domain: Processo Legislativo

## Conceitos Principais

### Proposições

- Projetos de Lei (PL)
- Emendas
- Indicações
- Moções
- Requerimentos

Cada proposição tem:
- Autor(es)
- Data de apresentação
- Status (em tramitação, aprovado, rejeitado, etc)
- Histórico de ações

### Sessões

- Sessões do Plenário
- Comissões
- Extraordinárias
- Especiais

Características:
- Data e horário
- Ordem do dia
- Proposições em pauta
- Presença de parlamentares
- Votações

### Votações

- Nominal (each deputy identifies)
- Simbólica
- Secreta
- Eletrônica

Registra:
- Sim/Não/Abstenção
- Ausência justificada/não
- Resultado final

### Parlamentares

- Dados básicos
- Gabinete
- Comissões
- Histórico legislativo
- Contribuições e autorias

---

## Fluxo Legislativo Típico

```
Apresentação da Proposição
        ↓
Protocolo
        ↓
Distribuição a Comissões
        ↓
Pareceres
        ↓
Plenário
        ↓
Votação
        ↓
Resultado
        ├─ Aprovado → Sanção/Execução
        └─ Rejeitado → Arquivo

Pode haver:
- Tramitação em várias comissões
- Emendas durante comissão
- Votação em 1ª e 2ª discussão
- Veto
- Reconsideração
```

---

## Compatibilidade Upstream

SAPL-SD mantém compatibilidade com SAPL (projeto origem).

Conceitos de domínio devem respeitar:
- Estrutura SAPL original
- Nomes e termos
- Fluxos legislativos
- APIs de compatibilidade

Mudanças que quebram upstream devem ser excepcionais e bem justificadas.

---

## Padrões de Nomenclatura

- `Proposição`, não "projeto" ou "bill"
- `Parlamentar`, não "deputy" ou "congressman"
- `Sessão`, não "meeting"
- `Voto`, não "vote"
- `Comissão`, não "committee"

Use termos em português para clareza.

---

## Auditoria

Todo processo legislativo deve ser auditável:

- Proposições com histórico completo
- Sessões com atas
- Votações com registros
- Ausência de modificação retroativa
- Rastreamento de mudanças
