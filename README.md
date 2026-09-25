# Aprendizagem de Máquina — Unidades

Site estático da disciplina Aprendizagem de Máquina, com catálogo central e apresentações Reveal.js por unidade.

## Unidades publicadas

- [Unidade 1 — Fundamentos teóricos da aprendizagem](./unidade-1/)
- [Unidade 2 — Regressão](./unidade-2/)

O catálogo fica em `index.html`. Cada unidade mantém sua apresentação e seus recursos próprios em uma pasta independente.

## Executar localmente

Na raiz do repositório, execute:

```bash
python3 -m http.server 8000
```

Depois acesse:

```text
http://localhost:8000/
```

Não use `file://` para validar navegação ou caminhos. Para simular o subcaminho do GitHub Pages, sirva o diretório pai e acesse `http://localhost:8000/ml-ia-unimar-2026/`.

## Verificar a preservação das apresentações

```bash
python3 scripts/verify-presentation-integrity.py
```

O verificador confere os arquivos imutáveis, as regiões de slides e as contagens de seções das Unidades 1 e 2.

## Manutenção e publicação

- Para incluir uma unidade, siga [`ADICIONAR_UNIDADE.md`](./ADICIONAR_UNIDADE.md).
- Para publicar pela branch `main` e pasta `/ (root)`, siga [`PUBLICAR_GITHUB_PAGES.md`](./PUBLICAR_GITHUB_PAGES.md).

O site não usa build, Node.js, backend ou Jekyll. Reveal.js, KaTeX e plugins continuam sendo carregados pela CDN jsDelivr e exigem acesso à internet.
