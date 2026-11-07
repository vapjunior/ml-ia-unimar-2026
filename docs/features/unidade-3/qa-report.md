# Validação — Unidade 3

Resultado: APPROVED para AC-001 a AC-004, em 06/11/2026. Validação realizada pelo próprio agente principal; não houve agente QA independente, conforme pedido explícito de não usar subagentes.

Versão validada: árvore sobre `47d6858`, com alterações em `index.html`, `README.md` e novo `unidade-3/index.html`. Apenas documentação foi alterada após os testes.

## Evidências reais

- `python3 scripts/verify-presentation-integrity.py`: sucesso; 8 arquivos imutáveis, 53 seções da Unidade 1 e 67 da Unidade 2 preservados.
- `git diff --check`: sucesso.
- Comparação binária com o HTML recebido, removendo apenas CSS e navegação inseridos: igualdade confirmada; SHA-256 registrado em `implementation.md`.
- HTTP local: `python3 -m http.server 8001 --bind 127.0.0.1` na raiz e `python3 -m http.server 8000 --bind 127.0.0.1 --directory /Users/macbook/Workspace` no diretório pai.
- Playwright 1.65.0 com Google Chrome headless: `node /tmp/validate-ml-unidade-3.cjs`, sucesso nos dois endereços `http://127.0.0.1:8001/` e `http://127.0.0.1:8000/ml-ia-unimar-2026/`.
- Confirmados 3 cartões no catálogo, abertura da Unidade 3 e retorno relativo, 68 slides, avanço com seta, abertura e fechamento das notas, fragmento `#/slide-20`, ausência de erros JS e respostas HTTP >=400.
- Viewports 1440×900 e 390×844: capturas inspecionadas, barra de retorno visível e ausência de rolagem horizontal mobile.
- `?print-pdf`: páginas de impressão geradas; barra e botão de notas ocultos em mídia print.

A contagem textual inicial de 70 elementos `section` inclui dois painéis das notas. A contagem correta de slides, confirmada no DOM do Reveal, é 68. A expectativa do verificador temporário foi corrigida e a execução completa passou.

## Limites

Não foram auditados o conteúdo pedagógico, todos os widgets individualmente ou a publicação efetiva do GitHub Pages. O teste temporário e as capturas estão em `/tmp`; não adicionam dependências ao repositório.
