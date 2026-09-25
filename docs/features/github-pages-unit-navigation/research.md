# Pesquisa — navegação de unidades no GitHub Pages

Data do levantamento: 23/09/2026

## Objetivo do levantamento

Documentar o estado atual do repositório e estabelecer uma linha de base verificável para integrar a Unidade 2 e uma navegação extensível, sem modificar o conteúdo didático gerado das apresentações.

## Fontes inspecionadas

- `README.md`
- `PUBLICAR_GITHUB_PAGES.md`
- `.nojekyll`
- `.gitignore`
- `index.html`, `css/custom.css` e `js/slides.js` da Unidade 1
- `ml-unidade2-regressao-reveal/README.md`
- `ml-unidade2-regressao-reveal/REFERENCIAS.md`
- `ml-unidade2-regressao-reveal/index.html`
- `ml-unidade2-regressao-reveal/css/custom.css`
- `ml-unidade2-regressao-reveal/js/slides.js`
- histórico, arquivos rastreados, branches e remotos do Git

Não há `AGENTS.md`, `docs/PRD.md`, `workflow.md`, configuração de CI/CD, `package.json`, `CNAME` ou configuração Jekyll dentro deste repositório no estado analisado. Aplicam-se as instruções de equipe fornecidas no contexto da tarefa.

## Estado atual

### Repositório e publicação

- Repositório remoto: `https://github.com/vapjunior/ml-ia-unimar-2026.git`.
- Branch atual e remota: `main`, no commit `fa10de1` (`Publica apresentacao da unidade 1`).
- O guia existente prescreve GitHub Pages com `Deploy from a branch`, branch `main`, pasta `/ (root)`.
- Não existe etapa de build. A publicação é de arquivos estáticos diretamente da raiz.
- `.nojekyll` já existe na raiz.
- Reveal.js, KaTeX e plugins são carregados da CDN jsDelivr; portanto, a apresentação publicada depende de acesso à internet para esses recursos.
- Os recursos próprios usam caminhos relativos, compatíveis com um GitHub Pages de projeto quando cada apresentação e suas pastas `css/` e `js/` permanecem juntas.

### Unidade 1

- A Unidade 1 ocupa atualmente a raiz publicada: `index.html`, `css/custom.css` e `js/slides.js`.
- O HTML contém 53 elementos `<section>`.
- Mantém navegação Reveal por hash, controles, progresso, numeração, auto-animate, fórmulas, destaque de código, busca, zoom e notas.
- Possui um quiz interativo implementado em `js/slides.js`.
- A raiz também contém `README.md`, `REFERENCIAS.md` e o guia de publicação.

Linha de base SHA-256:

| Arquivo atual | SHA-256 |
|---|---|
| `index.html` | `597a43658092471ac7fbb4c2a6c308b634ce2c467928457732c82683062ca797` |
| `css/custom.css` | `20607ecc28571aee1dbdf335e88a6f061a98b843578d6d454317d3701418b904` |
| `js/slides.js` | `cd001b0523072e3411d8a81192a2ee1901e86300b2d94012727891c0f266c062` |
| `README.md` | `aeb785de67bb3a9f669a024b03135581c00b85117802f9fc4a2625b045cd6bb6` |
| `REFERENCIAS.md` | `6474d050ca014ed2512509271ad0d56e68e18fc1868c59b0ca8256e49c605c03` |

### Unidade 2

- A pasta `ml-unidade2-regressao-reveal/` está presente localmente, mas ainda não é rastreada pelo Git.
- É uma apresentação estática autocontida, formada por `index.html`, `css/custom.css`, `js/slides.js`, `README.md` e `REFERENCIAS.md`.
- O HTML contém 67 elementos `<section>`.
- Usa Reveal.js 5.2.1 e os plugins notes, highlight, math, search e zoom via CDN.
- Usa caminhos relativos `css/custom.css` e `js/slides.js`; por isso, pode ser publicada em um subdiretório sem reescrever esses caminhos, desde que sua estrutura interna seja mantida.
- Não há chamadas de rede além das dependências CDN, nem carregamento dinâmico de dados locais.

Linha de base SHA-256:

| Arquivo atual | SHA-256 |
|---|---|
| `ml-unidade2-regressao-reveal/index.html` | `b6044f4b5aa83eea1bab70f7b9aaae7cc2580b2d69a907d893aa763bc9e62b7e` |
| `ml-unidade2-regressao-reveal/css/custom.css` | `0d7e269135ba3c87bc73fc0136d115f1f69659e16bac5042de2759dd53e2e303` |
| `ml-unidade2-regressao-reveal/js/slides.js` | `d7996e6ba26a045ea8694e440f73e73256ecb007f3849e2424a42e44f8b265c1` |
| `ml-unidade2-regressao-reveal/README.md` | `b259dd9d84822878f3972ddeb17629807219217d725003809f8fab188f52233e` |
| `ml-unidade2-regressao-reveal/REFERENCIAS.md` | `86425599ff6ef61b897a2ce4ceb91a534079342557fd1cac7190d7b676b4cf78` |

## Interpretação de “não alterar o conteúdo gerado”

Considera-se conteúdo protegido das Unidades 1 e 2:

- texto, títulos, ordem e quantidade dos slides;
- fórmulas, exemplos, códigos, tabelas, referências e respostas do quiz;
- tema, cores, tipografia, composição e comportamento visual dos slides;
- configuração funcional do Reveal.js, transições, fragments, auto-animate e plugins;
- comportamento do quiz, navegação por hash e exportação por `?print-pdf`.

São admissíveis somente mudanças de integração indispensáveis à hospedagem e navegação, como organização em rotas, referências relativas equivalentes e controles externos ao conteúdo dos slides. Mesmo essas mudanças não podem alterar a apresentação percebida nem suas funcionalidades. Sempre que possível, os arquivos gerados devem ser movidos ou copiados sem alteração de bytes; se uma alteração de integração em um arquivo protegido for inevitável, ela deve ser isolada, justificada e validada por comparação funcional e visual.

## Necessidade de produto identificada

A raiz hoje serve diretamente a Unidade 1. Para oferecer um catálogo de unidades, a experiência pública precisa separar a página de seleção das apresentações. A solução deverá:

- expor uma entrada principal com Unidade 1 e Unidade 2;
- permitir ir de qualquer unidade ao catálogo e então a outra unidade sem depender de editar os slides didáticos;
- manter URLs relativas compatíveis com o subcaminho de projeto do GitHub Pages;
- permitir incluir futuras unidades sem modificar o conteúdo das unidades já publicadas.

O detalhamento visual e o padrão de controle de retorno ficam para Design, desde que atendam aos critérios do PRD.

## Riscos e decisões para as próximas etapas

| Risco | Impacto | Mitigação/decisão de produto |
|---|---|---|
| Substituir o `index.html` raiz por um catálogo muda a URL que hoje abre diretamente a Unidade 1. | Links salvos para a raiz, especialmente com fragmentos Reveal, deixam de abrir o mesmo slide. | Tech Lead deve prever rota estável para a Unidade 1 e avaliar compatibilidade/redirecionamento sem impedir o catálogo raiz. Registrar a decisão. |
| Inserir menu dentro do HTML/CSS gerado pode mudar layout, teclado, impressão ou tela cheia do Reveal. | Viola a preservação solicitada e pode causar regressão didática. | Preferir integração externa ao conteúdo dos slides; Design deve especificar navegação discreta e QA comparar apresentação normal e PDF. |
| URLs absolutas iniciadas por `/` apontariam para a raiz do domínio, não para `/ml-ia-unimar-2026/`. | Erros 404 no GitHub Pages de projeto. | Todos os links internos do catálogo devem funcionar sob subcaminho e em servidor local. |
| A pasta da Unidade 2 ainda não está versionada. | Ela não será publicada enquanto permanecer não rastreada. | A implementação deve adicionar a pasta e confirmar sua presença no artefato publicado. |
| Dependência de CDN. | Sem internet, estilos e plugins externos não carregam. | Fora do escopo tornar a apresentação offline; manter comportamento atual e documentar a limitação. |
| Menu rígido e duplicado em vários arquivos. | Cada nova unidade exige alterações dispersas e aumenta chance de inconsistência. | A inclusão futura deve ser centralizada e não exigir edição de unidades anteriores. |

## Comandos e resultados do levantamento

- `git status --short --branch`: branch `main` sincronizada com `origin/main`; `ml-unidade2-regressao-reveal/` aparece como não rastreada.
- `git log --oneline --decorate --stat -8`: um commit no histórico, `fa10de1`, contendo somente a Unidade 1 e arquivos de publicação.
- `git ls-files`: oito arquivos rastreados; nenhum arquivo da Unidade 2.
- `find . -maxdepth 4 ...`: nenhuma configuração de CI/CD ou ferramenta de build encontrada.
- `rg -n "<section" ...`: 53 seções na Unidade 1 e 67 na Unidade 2.
- `rg -n "href=|src=|url\\(" ...`: dependências externas via jsDelivr e recursos próprios relativos.
- `shasum -a 256 ...`: hashes registrados nas tabelas de linha de base.
