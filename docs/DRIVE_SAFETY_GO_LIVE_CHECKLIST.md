# Drive Safety Go-Live Checklist

Status: BLOCKED
Data: 2026-08-27

A escrita de produção do SDKA Functional Bridge somente pode ser habilitada
quando todos os controles abaixo estiverem concluídos.

- [ ] identidade institucional operacional dedicada;
- [ ] scopes OAuth mínimos conhecidos e validados;
- [x] raiz funcional identificada e versionada;
- [x] quarentena física criada;
- [x] restauração testada com artefato descartável;
- [x] matriz de autorização versionada;
- [x] policy engine de referência implementado;
- [x] testes adversariais automatizados aprovados;
- [ ] integração obrigatória do gate no caminho real de escrita;
- [ ] storage de auditoria append-only isolado;
- [ ] identidade/credencial de backup separada;
- [ ] teste de restauração a partir do backup isolado;
- [ ] aprovação humana final para go-live.

Enquanto houver item pendente:

`FUNCTIONAL BRIDGE PRODUCTION WRITE = BLOCKED`
