# PRD — catálogo e navegação de unidades no GitHub Pages

Status: **READY**

Data: 25/09/2026

## Contexto

O repositório publica hoje a apresentação da Unidade 1 diretamente na raiz do GitHub Pages, sem build. A Unidade 2 existe localmente em `ml-unidade2-regressao-reveal/`, também como apresentação Reveal.js estática, mas ainda não faz parte da versão rastreada. É necessário publicar as duas unidades em um único site e oferecer uma navegação preparada para futuras unidades, preservando integralmente o conteúdo didático gerado.

Este documento é o PRD raiz desta funcionalidade, pois o repositório não possui `docs/PRD.md` no estado analisado.

## Resultado esperado

Visitantes encontram um catálogo claro na entrada do site, abrem a Unidade 1 ou a Unidade 2, conseguem retornar ao catálogo para trocar de unidade e continuam usando todas as funções existentes de cada apresentação. A adição futura de uma unidade não exige modificar apresentações já publicadas.

## Usuários e necessidades

- **Estudante:** identificar a unidade desejada e entrar rapidamente na apresentação, inclusive em tela pequena.
- **Docente/apresentador:** alternar entre unidades e usar os recursos Reveal.js, links por slide e exportação para PDF sem regressões.
- **Mantenedor:** adicionar unidades futuras com alteração localizada, previsível e sem tocar no conteúdo das unidades anteriores.

## Escopo funcional

### REQ-001 — Preservar a Unidade 1

A apresentação existente da Unidade 1 deve permanecer disponível em uma URL própria e conservar integralmente seu conteúdo, aparência e comportamento.

Critérios de aceite:

- **AC-001:** a apresentação entregue contém os mesmos 53 elementos `<section>`, na mesma ordem e com os mesmos textos, fórmulas, exemplos e referências da linha de base registrada em `research.md`.
- **AC-002:** controles, progresso, numeração `c/t`, navegação por hash, auto-animate, transições, notas, busca, zoom, KaTeX e destaque de código continuam funcionando.
- **AC-003:** o quiz mantém as mesmas alternativas, mensagens e distinção visual entre resposta correta e incorreta.
- **AC-004:** abrir a URL da Unidade 1 com `?print-pdf` continua produzindo a visualização de impressão paisagem sem sobrepor elementos de navegação do catálogo aos slides.
- **AC-005:** `css/custom.css`, `js/slides.js`, `README.md` e `REFERENCIAS.md` da Unidade 1 permanecem idênticos em bytes aos hashes da linha de base de `research.md`; no `index.html`, a região que contém os slides permanece idêntica, e qualquer diferença fora dela deve se limitar à integração indispensável com a navegação, ser justificada em `implementation.md` e não alterar a apresentação percebida.

### REQ-002 — Publicar a Unidade 2

A apresentação existente em `ml-unidade2-regressao-reveal/` deve ser integrada ao mesmo GitHub Pages e acessível em uma URL própria.

Critérios de aceite:

- **AC-006:** a URL da Unidade 2 responde sem erro e carrega seu CSS, JavaScript e dependências Reveal.js no subcaminho do repositório GitHub Pages.
- **AC-007:** a apresentação entregue contém os mesmos 67 elementos `<section>`, na mesma ordem e com os mesmos textos, fórmulas, exemplos, tabelas, códigos e referências da linha de base registrada em `research.md`.
- **AC-008:** controles, progresso, numeração `c/t`, navegação por hash, auto-animate, transições, notas, busca, zoom, KaTeX e destaque de código continuam funcionando conforme a versão recebida.
- **AC-009:** abrir a URL da Unidade 2 com `?print-pdf` continua produzindo a visualização de impressão sem sobreposição do catálogo ou de controles adicionais.
- **AC-010:** `css/custom.css`, `js/slides.js`, `README.md` e `REFERENCIAS.md` da Unidade 2 permanecem idênticos em bytes aos hashes da linha de base de `research.md`; no `index.html`, a região que contém os slides permanece idêntica, e qualquer diferença fora dela deve se limitar à integração indispensável com a navegação, ser justificada em `implementation.md` e não alterar a apresentação percebida.

### REQ-003 — Oferecer catálogo das unidades

A entrada principal do site deve apresentar um menu/catálogo que permita reconhecer e abrir cada unidade publicada.

Critérios de aceite:

- **AC-011:** a URL raiz do GitHub Pages apresenta, no mínimo, opções identificadas como “Unidade 1 — Fundamentos teóricos da aprendizagem” e “Unidade 2 — Regressão”.
- **AC-012:** cada opção abre a respectiva apresentação sem erro 404 e sem depender de URL absoluta na raiz do domínio.
- **AC-013:** a partir de qualquer uma das duas apresentações, o usuário alcança a outra unidade em no máximo duas ações de navegação, por meio de um caminho explícito de retorno ao catálogo; usar apenas o botão Voltar do navegador não satisfaz este critério.
- **AC-014:** a navegação adicional não captura teclas nem gestos usados pelo Reveal.js e não aparece na impressão/PDF dos slides.
- **AC-015:** o menu diferencia visualmente unidades disponíveis; não deve exibir links quebrados ou cartões clicáveis para unidades futuras ainda não publicadas.

### REQ-004 — Preparar a expansão para futuras unidades

A estrutura do catálogo deve permitir adicionar novas unidades sem alterar o conteúdo gerado das unidades anteriores.

Critérios de aceite:

- **AC-016:** adicionar uma terceira unidade exige somente incluir os arquivos da nova unidade e atualizar um único ponto central do catálogo/configuração; não exige editar HTML, CSS ou JavaScript das Unidades 1 e 2.
- **AC-017:** cada unidade possui URL própria, previsível e sem colisão com outras unidades.
- **AC-018:** nomes, ordem e disponibilidade exibidos no catálogo têm uma única fonte de verdade ou um único local documentado de manutenção.
- **AC-019:** a documentação do repositório inclui passos suficientes para um mantenedor adicionar uma unidade futura e validar seu link localmente antes da publicação.

### REQ-005 — Manter compatibilidade com GitHub Pages

O site completo deve continuar publicável como conteúdo estático, sem backend e sem etapa obrigatória de build.

Critérios de aceite:

- **AC-020:** o artefato funciona com a configuração já documentada: branch `main`, pasta `/ (root)` e `.nojekyll` na raiz.
- **AC-021:** catálogo, Unidade 1 e Unidade 2 funcionam tanto no subcaminho de projeto `/<repositorio>/` quanto em um servidor HTTP local; nenhum recurso próprio retorna 404 nos dois contextos.
- **AC-022:** não são introduzidas dependências de runtime, API externa de aplicação, banco de dados ou processamento do lado do servidor; as CDNs já utilizadas pelas apresentações podem permanecer.
- **AC-023:** recarregar uma apresentação em sua URL própria, incluindo um fragmento Reveal válido, mantém o usuário na unidade e no slide correspondente.

### REQ-006 — Tornar o catálogo utilizável e acessível

O catálogo deve ser operável em desktop e mobile e permitir navegação básica assistiva.

Critérios de aceite:

- **AC-024:** em larguras de viewport de 320 px a 1440 px, todo o texto e todas as opções permanecem legíveis e acionáveis, sem rolagem horizontal.
- **AC-025:** todas as opções do catálogo podem ser alcançadas e acionadas apenas por teclado, com foco visível.
- **AC-026:** títulos e links possuem nomes acessíveis que identificam a unidade de destino; contraste de texto e controles atende WCAG 2.1 AA.
- **AC-027:** o catálogo não depende exclusivamente de cor para indicar disponibilidade ou ação.

## Fora do escopo

- Alterar, revisar, resumir ou ampliar o conteúdo didático das Unidades 1 e 2.
- Unificar versões do Reveal.js, redesenhar os slides ou refatorar seus CSS/JavaScript.
- Tornar Reveal.js e plugins disponíveis offline.
- Criar backend, autenticação, banco de dados, telemetria ou painel administrativo.
- Criar conteúdo ou links ativos para unidades futuras que ainda não tenham arquivos entregues.
- Mudar o método de publicação para pipeline com build, salvo se uma limitação técnica comprovada exigir nova decisão de produto.

## Métricas de sucesso

- 100% das duas unidades publicadas abrem sem 404 em HTML, CSS e JavaScript próprios.
- 100% dos critérios de preservação das apresentações passam na validação de QA.
- Uma pessoa consegue trocar de qualquer unidade para a outra em no máximo duas ações explícitas.
- Uma unidade futura pode ser adicionada sem editar arquivos protegidos das unidades já existentes.
- Zero alteração não justificada nos conteúdos protegidos em relação à linha de base.

## Restrições e decisões

- A raiz pública será o catálogo; cada apresentação terá URL própria.
- O conteúdo protegido é definido em `research.md`; adaptação de hospedagem não autoriza mudanças didáticas, visuais ou comportamentais nos slides.
- Mover ou copiar os arquivos para as rotas públicas não autoriza reformatá-los, normalizar quebras de linha, atualizar bibliotecas, corrigir textos ou refatorar CSS/JavaScript. Quando a navegação exigir integração no `index.html`, ela deve ficar fora da região dos slides e ser a menor alteração possível.
- Os links internos devem ser relativos ao site/projeto e não assumir publicação na raiz do domínio.
- A navegação deve permanecer fora da área impressa e não interferir com Reveal.js.
- O mecanismo técnico exato e a rota final de cada unidade serão definidos pelo Tech Lead após a especificação de Design.

## Rastreabilidade

| Requisito | Critérios de aceite |
|---|---|
| REQ-001 | AC-001 a AC-005 |
| REQ-002 | AC-006 a AC-010 |
| REQ-003 | AC-011 a AC-015 |
| REQ-004 | AC-016 a AC-019 |
| REQ-005 | AC-020 a AC-023 |
| REQ-006 | AC-024 a AC-027 |

## Evidências esperadas no handoff de implementação e QA

- Mapa final de URLs do catálogo e das unidades.
- Comparação dos arquivos protegidos com os hashes de `research.md`, com justificativa de toda divergência.
- Teste HTTP local das três entradas e dos recursos próprios.
- Validação em URL com subcaminho equivalente ao GitHub Pages de projeto.
- Registro de navegação por teclado e em viewports de 320 px e 1440 px.
- Smoke test funcional das duas apresentações e teste de `?print-pdf`.
- Confirmação de que uma nova unidade requer alteração em um único ponto central e não nos arquivos das unidades existentes.

## Próximo responsável

**Design**, para especificar a experiência responsiva do catálogo e o caminho explícito de retorno a ele sem interferir na apresentação, no teclado do Reveal.js ou na impressão. Em seguida, o Tech Lead deve definir rotas, estrutura de arquivos e tarefas READY.
