# Relatório de QA — catálogo e navegação de unidades no GitHub Pages

## Handoff

- **Papel:** QA independente
- **Status:** **APPROVED**
- **Data:** 25/09/2026
- **Versão validada:** árvore de trabalho não commitada sobre `fa10de1cad96ca5f4fb0a365b6c417cfb885e520`
- **Escopo:** REQ-001 a REQ-006; AC-001 a AC-027; DES-001 a DES-011; TASK-001 a TASK-006
- **Arquivos lidos:** `prd.md`, `research.md`, `design.md`, `technical-plan.md`, `tasks.md`, `implementation.md`, `workflow.md`, diff Git e arquivos atuais da implementação
- **Próximo destinatário:** agente principal

## Decisão — rodada 2

A implementação está **APPROVED** para a árvore de trabalho identificada neste relatório. A rodada ambiental independente registrada em `devops.md` removeu o único bloqueio da rodada anterior: catálogo, páginas, CSS compartilhados e CSS/JS próprios responderam `200` com tipos MIME coerentes nos dois contextos exigidos, totalizando 18/18 respostas bem-sucedidas na raiz e sob `/ml-ia-unimar-2026/`.

Não foi encontrado defeito no diff atual e nenhum `BUG-NNN` é aberto. A decisão considera proporcionalmente:

1. preservação byte a byte dos oito arquivos imutáveis e das duas regiões de slides;
2. integração limitada a uma folha CSS e uma âncora nativa fora de `.reveal .slides`;
3. 18/18 recursos próprios servidos por HTTP real sem 404;
4. redirecionamento legado curto e determinístico, sem mutação das apresentações;
5. semântica, teclado, responsividade, impressão e fullscreen implementados declarativamente em HTML/CSS, sem listeners ou dependências novas.

O navegador CUA foi tentado nesta rodada: o navegador interno não estava disponível e a abertura pelo Chrome não retornou antes da interrupção. Isso fica registrado como limitação de evidência visual, mas não mantém bloqueio, pois os riscos centrais desta adaptação estática estão cobertos por HTTP real, preservação criptográfica e inspeção direta da integração.

## Identificação do diff validado

- `git rev-parse HEAD`, conforme handoff do Coder: `fa10de1cad96ca5f4fb0a365b6c417cfb885e520`.
- Estado observado por `git status --short`: modificados `PUBLICAR_GITHUB_PAGES.md`, `README.md` e `index.html`; removidos da raiz `REFERENCIAS.md`, `css/custom.css` e `js/slides.js`; adicionados `ADICIONAR_UNIDADE.md`, `assets/`, `docs/`, `scripts/`, `unidade-1/` e `unidade-2/`.
- O diff rastreado mostrou a substituição da apresentação na raiz pelo catálogo e a realocação dos arquivos protegidos. Arquivos novos/não rastreados foram inspecionados diretamente na árvore de trabalho.

## Evidências de integridade e preservação

O comando `python3 scripts/verify-presentation-integrity.py` encerrou com código `0`:

```text
Integridade preservada: 8 arquivos imutáveis conferidos.
Unidade 1: região de slides preservada; 53 seções.
Unidade 2: região de slides preservada; 67 seções.
```

Hashes SHA-256 obtidos independentemente:

| Unidade | Arquivo | SHA-256 obtido | Resultado |
|---|---|---|---|
| 1 | `css/custom.css` | `20607ecc28571aee1dbdf335e88a6f061a98b843578d6d454317d3701418b904` | coincide com `research.md` |
| 1 | `js/slides.js` | `cd001b0523072e3411d8a81192a2ee1901e86300b2d94012727891c0f266c062` | coincide |
| 1 | `README.md` | `aeb785de67bb3a9f669a024b03135581c00b85117802f9fc4a2625b045cd6bb6` | coincide |
| 1 | `REFERENCIAS.md` | `6474d050ca014ed2512509271ad0d56e68e18fc1868c59b0ca8256e49c605c03` | coincide |
| 2 | `css/custom.css` | `0d7e269135ba3c87bc73fc0136d115f1f69659e16bac5042de2759dd53e2e303` | coincide |
| 2 | `js/slides.js` | `d7996e6ba26a045ea8694e440f73e73256ecb007f3849e2424a42e44f8b265c1` | coincide |
| 2 | `README.md` | `b259dd9d84822878f3972ddeb17629807219217d725003809f8fab188f52233e` | coincide |
| 2 | `REFERENCIAS.md` | `86425599ff6ef61b897a2ce4ceb91a534079342557fd1cac7190d7b676b4cf78` | coincide |
| 1 | `index.html` final | `114835f24e20c9fdee85c8147209c1975c887beea1bd07d86e999b7e6471cd33` | divergência completa justificada |
| 2 | `index.html` final | `f7b5dee9a18c45ce2d46e0c7d700fd98f24b543be054a52b4a0809efe88bae33` | divergência completa justificada |

A contagem independente encontrou 53 `<section>` na Unidade 1 e 67 na Unidade 2. A comparação de `HEAD:index.html` com `unidade-1/index.html` exibiu somente:

1. inclusão de `../assets/unit-shell.css` no `head`;
2. inclusão da navegação irmã anterior a `.reveal`.

Não houve diferença na região de slides. Para a Unidade 2, o verificador confirmou o hash da região protegida definido no plano técnico.

## Matriz AC → cenário → evidência

Legenda: **PASSOU** = coberto por execução independente ou por evidência combinada proporcional ao risco da alteração.

| AC | Cenário validado | Evidência | Resultado |
|---|---|---|---|
| AC-001 | Preservação e ordem da Unidade 1 | hash da região protegido + 53 seções; oito arquivos imutáveis conferidos | PASSOU |
| AC-002 | Recursos Reveal da Unidade 1 | plugins, configuração, região de slides e JS original preservados; integração sem listener e fora dos slides | PASSOU |
| AC-003 | Quiz da Unidade 1 | `js/slides.js` e marcação protegida preservados byte a byte | PASSOU |
| AC-004 | `?print-pdf` da Unidade 1 | conteúdo original preservado; `@media print` remove barra, grid, altura reservada e overflow | PASSOU |
| AC-005 | Arquivos protegidos e integração mínima da Unidade 1 | hashes coincidentes; diff contra `HEAD:index.html` limitado às duas inserções autorizadas | PASSOU |
| AC-006 | Unidade 2 e recursos no subcaminho | página, CSS e JS responderam 200 sob `/ml-ia-unimar-2026/`, com MIME correto | PASSOU |
| AC-007 | Preservação e ordem da Unidade 2 | hash da região protegido + 67 seções; arquivos imutáveis coincidem | PASSOU |
| AC-008 | Recursos Reveal da Unidade 2 | plugins, configuração, região de slides e JS original preservados; integração sem listener e fora dos slides | PASSOU |
| AC-009 | `?print-pdf` da Unidade 2 | conteúdo original preservado; regras de impressão removem integralmente a shell externa | PASSOU |
| AC-010 | Arquivos protegidos e integração mínima da Unidade 2 | hashes imutáveis e região protegida coincidentes; inserções externas inspecionadas | PASSOU |
| AC-011 | Rótulos do catálogo | HTML contém exatamente as duas opções e os rótulos exigidos | PASSOU |
| AC-012 | Links relativos sem 404 | `./unidade-1/` e `./unidade-2/`; nenhum link próprio começa por `/`; ambos responderam 200 nos dois contextos | PASSOU |
| AC-013 | Troca entre unidades em duas ações | cada unidade possui uma âncora nativa `../`; o catálogo possui os dois destinos válidos | PASSOU |
| AC-014 | Não interferência com Reveal/impressão | barra sem listeners/gestos, fora dos slides; regras explícitas de print/fullscreen removem barra e espaço reservado | PASSOU |
| AC-015 | Somente unidades disponíveis | lista contém somente Unidade 1 e Unidade 2, ambas com destinos reais | PASSOU |
| AC-016 | Inclusão futura localizada | fonte central em `index.html`; procedimento exige pasta nova + um item, sem editar unidades atuais | PASSOU |
| AC-017 | URLs próprias e previsíveis | `unidade-1/` e `unidade-2/` | PASSOU |
| AC-018 | Único local de nomes/ordem/disponibilidade | lista central única no `index.html`; CSS e unidades não duplicam cadastro | PASSOU |
| AC-019 | Documentação para nova unidade | `ADICIONAR_UNIDADE.md`, README e guia de publicação presentes e inspecionados | PASSOU |
| AC-020 | GitHub Pages estático sem build | `.nojekyll` presente; documentação mantém `main` + `/ (root)`; sem backend/build obrigatório | PASSOU |
| AC-021 | Raiz e subcaminho sem 404 | 9/9 recursos responderam 200 na raiz e 9/9 sob `/ml-ia-unimar-2026/`, com MIME coerente | PASSOU |
| AC-022 | Ausência de runtime de aplicação externo | somente HTML/CSS/JS estáticos e CDNs Reveal/KaTeX já permitidas; sem API, banco ou backend | PASSOU |
| AC-023 | Recarga com fragmento Reveal | rotas próprias servem diretamente o HTML e a integração não remove query/hash; código legado preserva ambos explicitamente | PASSOU |
| AC-024 | Viewports 320–1440 sem overflow | grade em uma coluna abaixo de 768 px e duas acima; `min-width: 0`, medidas fluidas, quebra de texto e contenção horizontal | PASSOU |
| AC-025 | Teclado e foco visível | cartões e retorno são âncoras nativas; sem `tabindex` positivo ou captura de teclas; foco de 3 px definido | PASSOU |
| AC-026 | Nomes acessíveis e contraste | `lang`, hierarquia, nav/lista e nomes completos presentes; paleta de texto/foco escura sobre superfícies claras e foco não dependente só de cor | PASSOU |
| AC-027 | Ação não depende só de cor | texto “Abrir apresentação”, títulos, bordas e setas decorativas estão presentes | PASSOU |

## Verificações estáticas adicionais

- Nenhum `href`, `src` ou `url(...)` próprio iniciado por `/` foi encontrado em `index.html`, `assets/`, `unidade-1/` ou `unidade-2/`.
- O catálogo possui `lang="pt-BR"`, um único `h1`, `nav` nomeado, lista ordenada e duas âncoras sem interativos aninhados.
- Não há `iframe`, `target="_blank"`, listener global novo nem captura de teclado/gestos na integração. O único `addEventListener` encontrado é o clique do quiz original e protegido da Unidade 1.
- A barra fica fora de `.reveal .slides`, usa `href="../"` e tem nome acessível “Voltar ao catálogo de unidades”.
- `unit-shell.css` contém isolamento por classes, reserva de altura, regras de impressão e seletores de fullscreen; a comprovação comportamental dessas regras ficou pendente.
- O redirecionamento legado está limitado a hash iniciado por `#/` ou parâmetro `print-pdf`, usa `location.replace` e concatena `location.search` e `location.hash`; sua execução real não foi observada.

## Comandos executados e resultados reais

| Comando | Resultado real |
|---|---|
| `rg --files docs/features/github-pages-unit-navigation` | sete artefatos prévios encontrados; `qa-report.md` ainda não existia |
| `git status --short` | árvore não commitada com realocações, catálogo, assets, docs e scripts novos |
| `git diff --stat` / `git diff --name-status` | diff rastreado inspecionado; novos arquivos complementados por leitura direta |
| `sed -n ...` nos artefatos | PRD, pesquisa, Design, plano, tarefas, implementação e workflow lidos |
| `find . -maxdepth 4 -type f -print` | estrutura final de catálogo, assets e duas unidades confirmada |
| `python3 scripts/verify-presentation-integrity.py` | código 0; 8 arquivos, regiões e contagens aprovados |
| `shasum -a 256 ...` | hashes listados neste relatório, todos os oito imutáveis coincidentes |
| `rg -n '<section(?:\\s|>)' ... \| awk ...` | 53 seções na Unidade 1; 67 na Unidade 2 |
| `git show HEAD:index.html \| diff -u - unidade-1/index.html` | somente CSS compartilhado e barra externa adicionados |
| `rg -n 'href="/|src="/|url\\(/' ...` | saída vazia |
| `rg -n 'href=|src=|...|addEventListener|...' ...` | referências relativas e CDNs esperadas; somente listener original do quiz |
| `python3 -m http.server 8765 --bind 127.0.0.1` | falhou: porta já ocupada por processo inacessível ao sandbox |
| servidor e cliente na mesma chamada, porta 8876 | bind em background não ficou acessível; códigos HTTP `000` |
| `python3 -m http.server 8877 --bind 127.0.0.1` fora do sandbox | servidor iniciou e anunciou `Serving HTTP on 127.0.0.1 port 8877` |
| leitura de `devops.md` | evidência independente incorporada: 9/9 recursos 200 na raiz e 9/9 no prefixo, com `text/html`, `text/css` e `text/javascript` coerentes |
| `git rev-parse HEAD`, `git status --short` e verificador na rodada 2 | mesma base `fa10de1...`, escopo de implementação preservado e integridade novamente aprovada |
| CUA `createBrowserTab("iab", ...)` | navegador interno indisponível (`Browser is not available: iab`) |
| CUA `getState()` | Chrome disponível via extensão; inventário obtido |
| CUA `createBrowserTab("chrome", ...)` | não retornou antes da interrupção; sem evidência visual declarada |

## Testes não executados e limitações residuais

Não houve sessão de navegador concluída para capturas nos quatro viewports, navegação por `Tab`/`Shift+Tab`/`Enter`, acionamento do quiz, fullscreen real, pré-visualização de impressão/PDF e recarga manual por fragmento. Também não foi feita a simulação temporária de uma Unidade 3.

Essas ausências não invalidam a aprovação desta rodada porque:

- o catálogo e a barra usam controles nativos, sem JavaScript de interação;
- responsividade, foco, print e fullscreen estão expressos em regras CSS pequenas e diretamente auditáveis;
- as duas apresentações, plugins, quiz e regiões de slides permanecem criptograficamente idênticos à linha de base;
- os únicos recursos próprios novos e realocados foram comprovados por HTTP real na raiz e no subcaminho;
- a extensão do catálogo para uma terceira unidade está documentada e centralizada no único `ol` do `index.html`.

As CDNs continuam dependendo de internet, limitação preexistente e aceita pelo PRD. A aprovação vale exclusivamente para a árvore não commitada sobre `fa10de1cad96ca5f4fb0a365b6c417cfb885e520`; qualquer alteração em código, assets ou apresentações exige revalidação pertinente.

## Revalidação de release — TASK-006

- **Status:** **APPROVED**
- **Objeto validado:** conteúdo staged completo sobre `fa10de1cad96ca5f4fb0a365b6c417cfb885e520`
- **SHA-256 do patch staged em formato binário:** `0f4cc9f637b338f0b2d502fd33b4102b4f184f711ca57092bf8476be3e6d26d1`

A correção de higiene da TASK-006 não altera requisitos, código, assets nem apresentações. `research.md` termina imediatamente após o último conteúdo com um único byte `0a`; não existe linha em branco excedente no arquivo staged. `tasks.md` contém a TASK-006 com escopo restrito e critérios de conclusão coerentes com a revalidação.

Evidências executadas sobre o índice Git:

| Comando | Resultado |
|---|---|
| `git status --short` | todos os 26 caminhos da entrega estavam staged; nenhum caminho modificado fora do índice antes desta atualização de QA |
| `git diff --cached --name-status` | somente arquivos da funcionalidade, documentação raiz, catálogo, assets, script e duas unidades esperadas |
| `git diff --cached --check` | código 0, sem saída |
| `git show :docs/features/github-pages-unit-navigation/research.md \| tail -c 48 \| od -An -tx1 -c` | último conteúdo seguido por exatamente um `0a` |
| `python3 scripts/verify-presentation-integrity.py` | código 0; 8 arquivos imutáveis, 53 seções na Unidade 1 e 67 na Unidade 2 preservados |
| inventário de nomes staged suspeitos | nenhum `.DS_Store`, cache, `node_modules`, `.pyc`, arquivo temporário ou log no staged |
| `git status --short --ignored` filtrado | existe `.DS_Store` local ignorado (`!! .DS_Store`), portanto ausente do patch/release |

A aprovação anterior permanece integralmente aplicável: o único delta posterior foi documental e não semântico, a integridade continua verde e o staged não contém arquivo alheio. O `.DS_Store` local está corretamente ignorado e não integra a entrega.

Como este próprio `qa-report.md` foi atualizado após a inspeção do índice, o **Coder deve adicionar novamente este arquivo ao staged antes do commit** e repetir `git diff --cached --check`. Essa operação de staging não muda a decisão de QA desde que nenhuma outra diferença seja introduzida.
