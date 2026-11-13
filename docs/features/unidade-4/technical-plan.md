# Plano técnico — Unidade 4

Execução somente pelo agente principal, conforme solicitação explícita do usuário.

- REQ-001: publicar o HTML recebido como Unidade 4 — Séries temporais, previsão e sistemas de recomendação.
- REQ-002: disponibilizar pelo catálogo e incluir retorno às unidades conforme `ADICIONAR_UNIDADE.md`.
- REQ-003: criar commit e atualizar `origin/main`, única branch remota existente; não existe `master`.
- AC-001: HTML original preservado byte a byte, exceto inclusão dos links de CSS de navegação e barra de retorno externa ao Reveal.
- AC-002: catálogo e README apresentam quatro unidades em ordem; retorno usa `../`.
- AC-003: navegação funciona na raiz e no subcaminho do Pages, com apresentações anteriores preservadas.
- AC-004: apresentação inicializa com 78 slides; teclado, notas, fragmentos e impressão funcionam.

Mover o arquivo fornecido para `unidade-4/index.html`, inserir somente a navegação e atualizar catálogo e README. Não adicionar dependências nem alterar apresentações anteriores. Validar integridade, HTTP e comportamento no Chrome desktop/mobile antes do commit e push.

## Ajuste após validação móvel

BUG-001: o modo `reveal-scroll` insere uma barra de rolagem e desloca o retorno para fora da tela. Corrigir com CSS exclusivo em `unidade-4/css/unit-navigation.css`: layout em bloco e navegação sticky nesse modo, mantendo a configuração original do Reveal. Posicionar a ajuda abaixo da barra para evitar sobreposição no celular. Revalidar AC-003 e AC-004.
