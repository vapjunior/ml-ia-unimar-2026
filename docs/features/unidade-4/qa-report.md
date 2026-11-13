# Validação — Unidade 4

Resultado: APPROVED para AC-001 a AC-004 em 13/11/2026, após correção de BUG-001. Executado pelo próprio agente principal, sem agente QA independente, conforme pedido explícito do usuário.

Versão validada: árvore sobre `d566aca`, com `index.html`, `README.md`, `unidade-4/index.html` e `unidade-4/css/unit-navigation.css`. Após a última execução, apenas documentação foi alterada.

## Evidências reais

- Comparação binária: removendo os dois links de CSS e a barra inserida, o HTML coincide integralmente com o arquivo original. Hash registrado em `implementation.md`.
- `python3 scripts/verify-presentation-integrity.py`: sucesso; 8 arquivos imutáveis e slides das Unidades 1 e 2 preservados.
- `git diff --exit-code HEAD -- unidade-1 unidade-2 unidade-3`: sucesso, nenhuma apresentação anterior alterada.
- `git diff --check`: sucesso.
- Servidores: `python3 -m http.server 8001 --bind 127.0.0.1` na raiz e `python3 -m http.server 8000 --bind 127.0.0.1 --directory /Users/macbook/Workspace` no diretório pai.
- Playwright com Google Chrome headless: `node /tmp/validate-ml-unidade-4.cjs`, sucesso na raiz `http://127.0.0.1:8001/` e subcaminho `http://127.0.0.1:8000/ml-ia-unimar-2026/`.
- Confirmados: 4 cartões, abertura da Unidade 4, 78 slides, avanço por teclado, notas do aluno e do professor, retorno desktop/mobile e fragmento `#/slide-20`.
- Mobile 390×844: slide dentro da tela, sem rolagem horizontal, avanço por rolagem e retorno dentro do viewport e clicável após rolar. Desktop 1440×900: barra acima dos slides. Capturas do catálogo e da apresentação inspecionadas.
- `?print-pdf`: páginas de impressão geradas; barra e botão de notas ocultos na mídia print.
- Sem erros JavaScript ou respostas HTTP >=400 nas execuções completas aprovadas.

## Defeito corrigido

BUG-001: na primeira validação, a rolagem automática do Reveal deixava a barra acima do viewport; clicar no retorno mobile excedia o timeout. TASK-005 corrigiu a integração com CSS local. A revalidação final cobriu avanço por rolagem e clique no retorno em ambos os caminhos HTTP.

## Limitações

Não foram auditados o conteúdo pedagógico, cada widget individualmente ou a publicação efetiva do GitHub Pages. Validação temporária e capturas em `/tmp`; nenhuma dependência de teste adicionada ao repositório.
