# Tarefas — catálogo e navegação de unidades no GitHub Pages

Status geral: **READY**

Data: 24/09/2026

Todas as tarefas pertencem ao **Coder** e devem ser executadas em ordem. Nenhuma tarefa autoriza alteração didática, visual ou funcional dentro das apresentações. O Coder não deve reformatar arquivos protegidos e deve registrar decisões, comandos e resultados reais em `implementation.md`.

## TASK-001 — Realocar e proteger as apresentações

- **Status:** READY
- **Responsável:** Coder
- **Dependências:** nenhuma
- **Rastreabilidade:** REQ-001, REQ-002, REQ-004, REQ-005; AC-001, AC-005 a AC-007, AC-010, AC-017, AC-020 a AC-023
- **Arquivos de responsabilidade:** `unidade-1/**`, `unidade-2/**`, `scripts/verify-presentation-integrity.py`

### Implementação

1. Criar `unidade-1/` realocando para ela `index.html`, `css/custom.css`, `js/slides.js`, `README.md` e `REFERENCIAS.md` atuais da raiz.
2. Realocar `ml-unidade2-regressao-reveal/` para `unidade-2/`, sem normalização ou regravação desnecessária.
3. Criar o verificador de integridade sem dependências externas conforme o contrato de `technical-plan.md`.
4. Manter intactos os caminhos relativos internos `css/custom.css` e `js/slides.js` e as dependências CDN recebidas.
5. Não inserir ainda conteúdo dentro de `.reveal .slides` nem alterar CSS/JS próprios.

### Critérios de conclusão

- Os oito arquivos imutáveis (CSS, JS, README e referências das duas unidades) mantêm os hashes completos de `research.md`.
- A região entre o primeiro `<section` e o último `</section>` mantém os hashes definidos no plano técnico.
- O verificador confirma 53 seções na Unidade 1 e 67 na Unidade 2 e encerra com código zero.
- As duas unidades abrem diretamente em servidor HTTP local e carregam seus recursos próprios sem 404.

### Evidências esperadas

- Comando e saída do verificador.
- `git diff --summary` mostrando as realocações ou evidência equivalente.
- Status HTTP das duas páginas, CSS e JS.

## TASK-002 — Criar o catálogo raiz e a compatibilidade histórica

- **Status:** READY
- **Responsável:** Coder
- **Dependências:** TASK-001
- **Rastreabilidade:** REQ-003, REQ-004, REQ-005, REQ-006; AC-004, AC-011, AC-012, AC-015 a AC-018, AC-020 a AC-027; DES-001, DES-002, DES-007 a DES-011
- **Arquivos de responsabilidade:** `index.html`, `assets/catalog.css`

### Implementação

1. Criar na raiz o catálogo semântico especificado por Design, com exatamente as duas unidades publicadas.
2. Usar `./unidade-1/` e `./unidade-2/` como destinos e manter `index.html` como único ponto de manutenção de nomes, ordem, disponibilidade e rotas.
3. Implementar CSS responsivo e acessível isolado em `assets/catalog.css`, incluindo foco visível, alvos de 44 px, uma coluna no mobile, duas no desktop e `prefers-reduced-motion`.
4. Implementar no início do catálogo a compatibilidade seletiva: redirecionar `#/...` e `?print-pdf` históricos à Unidade 1 com `location.replace`, preservando query e fragmento; não redirecionar a raiz nua.
5. Não criar cartões ou links para unidades futuras.

### Critérios de conclusão

- A raiz nua exibe os rótulos completos exigidos por `AC-011` e permanece utilizável sem JavaScript para abrir as unidades.
- Os dois cartões são âncoras únicas, operáveis por teclado, com nomes acessíveis completos.
- Não há URL interna absoluta nem rolagem horizontal de 320 px a 1440 px.
- URLs antigas com hash Reveal ou `print-pdf` chegam à Unidade 1 sem perder query/fragmento; a raiz nua não é redirecionada.
- Adicionar uma unidade ao menu exige editar somente um item central em `index.html`.

### Evidências esperadas

- Capturas ou registro de inspeção nos quatro viewports definidos.
- Registro da navegação por teclado e zoom de 200%.
- URLs de entrada e destino dos casos de compatibilidade histórica.
- Busca por `href`/`src` próprios iniciados por `/`, com resultado vazio.

## TASK-003 — Integrar a barra externa compartilhada

- **Status:** READY
- **Responsável:** Coder
- **Dependências:** TASK-001, TASK-002
- **Rastreabilidade:** REQ-001, REQ-002, REQ-003, REQ-005; AC-002 a AC-005, AC-008 a AC-010, AC-013, AC-014, AC-021, AC-023; DES-003 a DES-006, DES-010
- **Arquivos de responsabilidade:** `assets/unit-shell.css`, `unidade-1/index.html`, `unidade-2/index.html`

### Implementação

1. Adicionar a cada HTML somente a referência ao CSS compartilhado e a barra utilitária irmã, anterior à `.reveal` e fora de `.slides`.
2. Usar uma única âncora nativa `../`, com texto “Todas as unidades” e nome acessível “Voltar ao catálogo de unidades”.
3. Fazer o layout normal reservar a altura da barra sem sobrepor ou cortar o Reveal.
4. Remover completamente barra e espaço reservado em impressão/`?print-pdf`.
5. Ocultar a barra em fullscreen exclusivamente por CSS e devolver 100% do viewport ao Reveal.
6. Não adicionar JavaScript, listeners, iframe ou mudanças dentro da região protegida dos slides.

### Critérios de conclusão

- O verificador de integridade continua passando sem alteração nos hashes de slides e arquivos imutáveis.
- A troca entre unidades ocorre em duas ações explícitas por meio do catálogo.
- A barra não captura teclas nem gestos e não cobre controles, progresso, numeração, conteúdo ou quiz.
- A barra desaparece em fullscreen e retorna ao sair.
- Impressão e `?print-pdf` não contêm barra, fundo, sombra, margem ou espaço residual.
- Recursos, query string e fragmentos Reveal continuam funcionais nas rotas próprias.

### Evidências esperadas

- Diff restrito das duas integrações HTML e do CSS compartilhado.
- Saída do verificador após a integração.
- Registro funcional de teclado, hash, fullscreen e impressão nas duas unidades.

## TASK-004 — Documentar publicação e inclusão futura

- **Status:** READY
- **Responsável:** Coder
- **Dependências:** TASK-002, TASK-003
- **Rastreabilidade:** REQ-004, REQ-005; AC-016 a AC-022
- **Arquivos de responsabilidade:** `ADICIONAR_UNIDADE.md`, `PUBLICAR_GITHUB_PAGES.md`, `README.md`, `docs/features/github-pages-unit-navigation/implementation.md`

### Implementação

1. Criar `ADICIONAR_UNIDADE.md` com convenção de rota, estrutura mínima, edição única do catálogo e validação local/subcaminho.
2. Atualizar a documentação raiz para descrever catálogo e rotas atuais, sem alterar os READMEs preservados dentro das unidades.
3. Manter explícita a publicação `main` + `/ (root)` e a presença de `.nojekyll`, sem introduzir build obrigatório.
4. Registrar em `implementation.md` o mapa final de URLs, arquivos movidos/criados, hashes finais, justificativa das duas divergências de `index.html`, comandos reais, resultados e limitações CDN.

### Critérios de conclusão

- Um mantenedor consegue adicionar `unidade-3/` e um único item de catálogo sem editar as Unidades 1 e 2.
- A documentação inclui validação HTTP local e simulação do prefixo `/ml-ia-unimar-2026/`.
- Nenhuma documentação sugere backend, Jekyll, Node ou build obrigatório.
- `implementation.md` vincula evidências a TASK/REQ/AC e não alega testes não executados.

### Evidências esperadas

- Revisão do procedimento completo de uma unidade futura.
- Referência aos comandos e resultados reais no relatório de implementação.

## TASK-005 — Executar smoke test e preparar handoff para QA

- **Status:** READY
- **Responsável:** Coder
- **Dependências:** TASK-001, TASK-002, TASK-003, TASK-004
- **Rastreabilidade:** REQ-001 a REQ-006; AC-001 a AC-027; DES-001 a DES-011
- **Arquivos de responsabilidade:** `docs/features/github-pages-unit-navigation/implementation.md` (somente evidências; correções permanecem nos arquivos das tarefas proprietárias)

### Implementação

1. Executar novamente o verificador de integridade no diff final.
2. Servir o repositório na raiz e em prefixo equivalente a `/ml-ia-unimar-2026/` e verificar catálogo, unidades e todos os recursos próprios.
3. Executar os cenários funcionais proporcionais descritos no plano técnico, incluindo compatibilidade histórica, teclado, quiz, fullscreen, `?print-pdf` e recarga com fragmento.
4. Registrar testes não executados e limitações reais; não substituir QA independente por autoaprovação.
5. Entregar ao QA o commit/diff exato ou identificador inequívoco do estado validado.

### Critérios de conclusão

- Nenhuma entrada ou recurso próprio retorna 404 nos dois contextos HTTP.
- Integridade, seções, links relativos e rotas passam.
- Fluxos essenciais das duas versões Reveal funcionam e a barra não interfere.
- `implementation.md` contém comandos, saídas resumidas, evidências e pendências.
- O handoff identifica explicitamente o estado/diff que QA deve validar.

### Handoff esperado

- **De:** Coder
- **Para:** QA
- **Status:** IMPLEMENTED, nunca APPROVED
- **Conteúdo mínimo:** objetivo; TASKs concluídas; REQ/AC/DES cobertos; arquivos alterados; mapa de URLs; hashes; comandos e resultados; testes não executados; riscos/limitações; diff/commit validado.

## TASK-006 — Corrigir linha em branco excedente antes do commit

- **Status:** READY
- **Responsável:** Coder
- **Dependências:** TASK-001 a TASK-005 concluídas; QA rodada 2 `APPROVED`
- **Origem:** falha de higiene pré-commit, sem `BUG-NNN`: `git diff --cached --check` encerrou com código 2 e informou `research.md:117: new blank line at EOF`
- **Rastreabilidade:** TASK-005; REQ-001, REQ-002; AC-005, AC-010
- **Arquivo de responsabilidade:** `docs/features/github-pages-unit-navigation/research.md`

### Implementação autorizada

1. Remover somente a linha em branco excedente ao final de `research.md`, mantendo uma única quebra de linha após o último conteúdo.
2. Não reformatar, reordenar, corrigir ou alterar semanticamente qualquer trecho de `research.md`.
3. Não alterar apresentações, catálogo, assets, scripts ou outros documentos como parte desta correção.
4. Atualizar o staging somente com a correção autorizada e preservar o restante exato da árvore aprovada.

### Critérios de conclusão

- O diff de `research.md` mostra exclusivamente a remoção da linha em branco final excedente.
- `git diff --check` encerra com código zero.
- `git diff --cached --check` encerra com código zero.
- `python3 scripts/verify-presentation-integrity.py` encerra com código zero e continua confirmando os 8 arquivos imutáveis, 53 seções na Unidade 1 e 67 seções na Unidade 2.
- Nenhum hash ou arquivo das apresentações é alterado.

### Evidências e handoff

- Registrar os comandos, códigos de saída e a inspeção do diff restrito de `research.md`.
- Entregar ao QA/release check o estado staged exato para revalidação pertinente antes do commit.

## Plano de retorno de QA

- `APPROVED`: QA confirma a implementação atual e todos os critérios obrigatórios; o principal pode concluir.
- `CHANGES_REQUIRED`: QA registra `BUG-NNN`; o trabalho retorna ao Tech Lead, que cria uma TASK corretiva vinculada antes de qualquer nova alteração do Coder.
- `BLOCKED`: não equivale a aprovação; registrar ambiente, comandos e dependência externa necessária.
