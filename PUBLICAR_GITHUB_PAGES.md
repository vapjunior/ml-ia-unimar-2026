# Publicar no GitHub Pages

Este projeto é um site estático com um catálogo de unidades e apresentações Reveal.js. Não precisa de build, Node.js, Jekyll ou backend.

## Estrutura publicada

Mantenha na raiz do repositório:

```text
index.html
assets/
unidade-1/
unidade-2/
README.md
ADICIONAR_UNIDADE.md
PUBLICAR_GITHUB_PAGES.md
.nojekyll
.gitignore
```

O arquivo `.nojekyll` deve permanecer na raiz para que os arquivos estáticos sejam publicados diretamente. Cada apresentação mantém seu HTML, CSS, JavaScript, README e referências dentro da pasta da unidade.

## Configurar a publicação

1. Abra o repositório no GitHub.
2. Acesse `Settings` e depois `Pages`.
3. Em `Build and deployment`, escolha:

```text
Source: Deploy from a branch
Branch: main
Folder: / (root)
```

4. Clique em `Save`.

O endereço deste repositório fica normalmente neste formato:

```text
https://vapjunior.github.io/ml-ia-unimar-2026/
```

A raiz exibe o catálogo. As apresentações ficam em:

```text
https://vapjunior.github.io/ml-ia-unimar-2026/unidade-1/
https://vapjunior.github.io/ml-ia-unimar-2026/unidade-2/
```

## Conferir a publicação

Depois que o GitHub Pages concluir a publicação:

- abra o catálogo e os dois cartões;
- use “Todas as unidades” para retornar de cada apresentação;
- confirme que CSS e JavaScript próprios não retornam 404;
- teste setas, progresso, numeração, fórmulas, destaque, busca, zoom e notas;
- teste o quiz da Unidade 1;
- recarregue uma unidade em um fragmento Reveal válido;
- teste fullscreen e a exportação com `?print-pdf` nas duas unidades.

Exemplos de impressão:

```text
https://vapjunior.github.io/ml-ia-unimar-2026/unidade-1/?print-pdf
https://vapjunior.github.io/ml-ia-unimar-2026/unidade-2/?print-pdf
```

Use a impressão do navegador em modo paisagem, com gráficos de fundo habilitados. A barra “Todas as unidades” não deve aparecer nem deixar espaço residual.

## Atualizar o site

Após validar as alterações:

```bash
git add .
git commit -m "Atualiza unidades de aprendizagem"
git push
```

O GitHub Pages republicará a branch `main` a partir de `/ (root)`. Para acrescentar uma unidade, siga [`ADICIONAR_UNIDADE.md`](./ADICIONAR_UNIDADE.md).

## Limitação externa

Reveal.js, KaTeX e plugins são carregados pela CDN jsDelivr. A versão publicada precisa de acesso à internet para carregar essas bibliotecas; essa dependência já existia nas apresentações e não foi alterada.
