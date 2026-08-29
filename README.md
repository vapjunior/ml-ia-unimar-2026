# Unidade 1 — Fundamentos teóricos da aprendizagem

Apresentação em Reveal.js para a disciplina Aprendizagem de Máquina.

## Como executar

Abra o arquivo `index.html` em um navegador moderno ou execute um servidor local:

```bash
python -m http.server 8000
```

Depois acesse:

```text
http://localhost:8000
```

## Estrutura

```text
index.html
css/custom.css
js/slides.js
PUBLICAR_GITHUB_PAGES.md
.nojekyll
.gitignore
```

## Publicar no GitHub Pages

O projeto já está preparado para publicação direta no GitHub Pages, sem etapa de build.

Siga o tutorial em [`PUBLICAR_GITHUB_PAGES.md`](PUBLICAR_GITHUB_PAGES.md).

## Exportar para PDF

Abra:

```text
http://localhost:8000/index.html?print-pdf
```

Use a impressão do navegador e salve como PDF, em modo paisagem, com gráficos de fundo habilitados.

## Recursos usados

- Reveal.js
- KaTeX para fórmulas
- Highlight.js para código
- Fragments e Auto-Animate
- Quiz interativo em JavaScript

## Observação

A apresentação usa CDN para carregar Reveal.js e plugins. Para uso offline, baixe o Reveal.js e ajuste os caminhos no `index.html`.
