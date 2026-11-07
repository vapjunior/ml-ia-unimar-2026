# Plano técnico — Unidade 3

Execução pelo agente principal, sem subagentes, conforme instrução explícita do usuário.

- REQ-001: disponibilizar o HTML fornecido como Unidade 3 — Validação e Seleção de Modelos.
- REQ-002: integrar o catálogo e o retorno às unidades seguindo `ADICIONAR_UNIDADE.md`.
- REQ-003: criar commit e atualizar a branch principal remota existente (`main`; não existe `master`).
- AC-001: `/unidade-3/` preserva todo o HTML original, exceto a inclusão da navegação externa e de seu CSS compartilhado.
- AC-002: catálogo e README apresentam as três unidades em ordem; retorno usa `../`.
- AC-003: navegação funciona na raiz e no subcaminho do GitHub Pages; as Unidades 1 e 2 preservam integridade.
- AC-004: slides, notas e impressão mantêm o comportamento do arquivo fornecido.

O arquivo fornecido contém estilos e scripts embutidos; será movido para `unidade-3/index.html`. Não há build nem dependências novas. A barra fica fora de `.reveal`, usando o CSS compartilhado já existente. Validar caminhos HTTP, conteúdo preservado e comportamento em navegador. A publicação usa `main`, segundo o remoto e a documentação do projeto.
