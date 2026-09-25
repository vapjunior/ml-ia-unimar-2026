# Plano técnico — catálogo e navegação de unidades no GitHub Pages

Status: **READY**

Data: 24/09/2026

## Objetivo técnico

Publicar um catálogo estático na raiz do GitHub Pages e expor as duas apresentações Reveal.js em rotas próprias e previsíveis, preservando o conteúdo didático e o comportamento recebido. A solução continua sem backend e sem build obrigatório, funciona sob o subcaminho do repositório e permite adicionar unidades futuras sem editar apresentações já publicadas.

Este plano implementa `REQ-001` a `REQ-006`, `AC-001` a `AC-027` e `DES-001` a `DES-011` definidos em `prd.md` e `design.md`.

## Decisões de arquitetura

### Rotas públicas

| Entrada | Rota relativa ao site | GitHub Pages de projeto |
|---|---|---|
| Catálogo | `./` | `/ml-ia-unimar-2026/` |
| Unidade 1 | `./unidade-1/` | `/ml-ia-unimar-2026/unidade-1/` |
| Unidade 2 | `./unidade-2/` | `/ml-ia-unimar-2026/unidade-2/` |

As rotas usam diretórios com `index.html` e links relativos com barra final. Nenhum link interno próprio começa por `/`, contém domínio ou codifica o nome do repositório. Isso mantém o mesmo artefato funcional em servidor HTTP local e no subcaminho do GitHub Pages (`AC-012`, `AC-017`, `AC-020`, `AC-021`, `AC-023`, `DES-010`).

### Compatibilidade da raiz histórica

A raiz nua passa a ser o catálogo, conforme decisão explícita do PRD. Portanto, não é possível preservar simultaneamente o comportamento histórico da raiz nua como Unidade 1. A compatibilidade será seletiva e verificável:

- uma URL antiga na raiz com fragmento Reveal no formato `#/...` redireciona, com `location.replace`, para `./unidade-1/`, preservando integralmente `location.search` e `location.hash`;
- uma URL antiga na raiz com o parâmetro `print-pdf` redireciona da mesma forma para `./unidade-1/?print-pdf`, também preservando eventual fragmento;
- a raiz sem esses marcadores não redireciona e renderiza o catálogo;
- o catálogo não usa fragmentos iniciados por `#/`, reservando esse formato para compatibilidade Reveal.

O redirecionamento fica no `index.html` raiz, executa antes da interface do catálogo e não toca em histórico, teclado ou eventos das apresentações. Assim, links profundos e links antigos de impressão continuam úteis, enquanto a alteração inevitável da raiz nua fica documentada (`REQ-001`, `REQ-003`, `REQ-005`; `AC-004`, `AC-011`, `AC-023`).

### Estrutura de arquivos alvo

```text
/
├── .nojekyll
├── index.html                         # catálogo e único registro das unidades
├── assets/
│   ├── catalog.css                    # estilos exclusivos do catálogo
│   └── unit-shell.css                 # barra externa compartilhada
├── unidade-1/
│   ├── index.html                     # Reveal + integração externa mínima
│   ├── css/custom.css                 # bytes preservados
│   ├── js/slides.js                   # bytes preservados
│   ├── README.md                      # bytes preservados
│   └── REFERENCIAS.md                 # bytes preservados
├── unidade-2/
│   ├── index.html                     # Reveal + integração externa mínima
│   ├── css/custom.css                 # bytes preservados
│   ├── js/slides.js                   # bytes preservados
│   ├── README.md                      # bytes preservados
│   └── REFERENCIAS.md                 # bytes preservados
├── scripts/
│   └── verify-presentation-integrity.py
└── ADICIONAR_UNIDADE.md
```

A Unidade 1 é realocada da raiz para `unidade-1/`. A pasta recebida `ml-unidade2-regressao-reveal/` é realocada para `unidade-2/`. CSS, JavaScript, README e referências viajam com cada apresentação sem alteração de bytes. Os caminhos próprios atuais permanecem relativos ao diretório da unidade.

### Único ponto central para unidades futuras

O `index.html` raiz é a fonte única de verdade dos nomes, da ordem, da disponibilidade e dos destinos exibidos no catálogo. O catálogo é HTML semântico estático; não depende de JavaScript para renderizar os links.

Para adicionar uma unidade futura, o mantenedor:

1. inclui a pasta autocontida em `unidade-N/`;
2. acrescenta exatamente um item à lista central do `index.html` raiz;
3. valida o link conforme `ADICIONAR_UNIDADE.md`.

Não há registro duplicado em CSS, JavaScript ou nas Unidades 1 e 2. Itens futuros não são pré-renderizados. O verificador de integridade desta entrega protege especificamente as linhas de base das Unidades 1 e 2 e não é um cadastro de navegação; uma unidade futura não precisa alterá-lo (`AC-015` a `AC-019`, `DES-001`, `DES-011`).

## Contratos internos

### Contrato do catálogo

- Um único `h1` “Aprendizagem de Máquina”.
- Uma região `nav` identificada como “Unidades disponíveis”, contendo lista semântica ordenada.
- Cada item é uma única âncora nativa, sem elementos interativos aninhados, com rótulo completo e destino relativo real.
- A ordem do DOM é a ordem pedagógica: Unidade 1, Unidade 2 e futuras unidades.
- Sem listeners globais, atalhos próprios, `target="_blank"`, iframe ou dependência de runtime.
- `catalog.css` usa seletores próprios do catálogo, pilha de fontes do sistema, foco visível, alvo mínimo de 44 px, uma coluna abaixo de 768 px e duas colunas a partir de 768 px.
- Não há rolagem horizontal entre 320 px e 1440 px, nem informação disponível somente por cor, hover ou ícone.

Esse contrato cobre `AC-011`, `AC-012`, `AC-015`, `AC-024` a `AC-027` e `DES-001`, `DES-002`, `DES-007` a `DES-010`.

### Contrato da barra externa às apresentações

Cada `index.html` de unidade recebe somente a integração indispensável fora de `.reveal .slides`:

- referência a `../assets/unit-shell.css` depois dos estilos da apresentação;
- uma região de navegação irmã e anterior a `.reveal`, com uma única âncora `href="../"`, texto visível “Todas as unidades” e nome acessível “Voltar ao catálogo de unidades”;
- nenhuma mudança entre o primeiro `<section` e o último `</section>`;
- nenhum listener de teclado, toque, ponteiro, roda, histórico ou fullscreen;
- nenhum iframe, modal, gaveta ou camada sobreposta aos slides.

`unit-shell.css` é compartilhado e isolado por classes `unit-shell-*`. No modo normal, o `body` distribui barra e Reveal em duas linhas, a barra tem pelo menos 44 px e `.reveal` recebe somente o espaço restante, com `min-height: 0`, sem sobreposição. A integração não redefine seletores internos de slides.

Em `@media print`, a barra usa `display: none`, o `body` volta ao fluxo esperado pela impressão e nenhum espaço residual permanece. Em fullscreen, regras baseadas em `:fullscreen`/prefixo suportado escondem a barra quando o documento é o elemento fullscreen; quando o próprio `.reveal` entra em fullscreen, a barra irmã já fica fora da árvore fullscreen. A apresentação ocupa 100% do viewport fullscreen. Não se adiciona JavaScript para observar fullscreen (`AC-002`, `AC-004`, `AC-008`, `AC-009`, `AC-013`, `AC-014`; `DES-003` a `DES-006`).

### Contrato de URL

- Catálogo → Unidade 1: `./unidade-1/`.
- Catálogo → Unidade 2: `./unidade-2/`.
- Unidade → catálogo: `../`.
- Query string e fragmento pertencem à URL da unidade e não são removidos pela barra.
- Recursos próprios das unidades continuam relativos ao respectivo `index.html`.
- Acesso e recarga diretos em `unidade-N/?print-pdf#/...` não passam pelo catálogo.

## Preservação e verificação por hashes

### Linha de base protegida

Os hashes completos SHA-256 de `research.md` continuam sendo a referência dos cinco arquivos recebidos por unidade. Após a realocação:

- `css/custom.css`, `js/slides.js`, `README.md` e `REFERENCIAS.md` de cada unidade devem manter exatamente seus hashes completos;
- `index.html` pode divergir somente pela referência ao CSS compartilhado e pela barra externa, pois essa é a integração indispensável autorizada por `AC-005` e `AC-010`;
- a região didática exata, do primeiro `<section` ao último `</section>` inclusivo, deve conservar seus bytes e o hash SHA-256 abaixo.

| Unidade | Seções | SHA-256 da região de slides |
|---|---:|---|
| Unidade 1 | 53 | `e938e752fbbf1d17a836f21e00aec3ca3539c7f937f447d782a969af7892a15b` |
| Unidade 2 | 67 | `7e39c98217d44fe4a564dc2ad919d009a753614fa4a177dd0ff7891dd55ab4f2` |

O script de desenvolvimento `scripts/verify-presentation-integrity.py`, sem dependências externas, deve:

1. calcular os oito hashes completos imutáveis após a realocação;
2. extrair de forma determinística a região do primeiro `<section` ao último `</section>` de cada HTML e comparar os dois hashes acima;
3. confirmar as contagens de 53 e 67 tags `<section`;
4. falhar com código diferente de zero e mensagem que identifique unidade, arquivo e valor divergente;
5. não modificar arquivos e não participar do runtime ou da publicação.

O Coder registra em `implementation.md` os hashes completos finais dos dois `index.html`, a divergência esperada em relação à linha de base completa e um resumo exato das inserções externas. QA repete o verificador e inspeciona o diff dos HTMLs para confirmar que não houve mudança dentro da região protegida.

## Plano de validação

### Validações automatizáveis locais

- Executar o verificador de integridade e obter saída bem-sucedida para as duas unidades.
- Contar 53 e 67 seções.
- Subir servidor HTTP estático na raiz e verificar status 200 para catálogo, duas rotas, dois CSS próprios, dois JS próprios e assets compartilhados.
- Subir o mesmo conteúdo sob um prefixo local `/ml-ia-unimar-2026/` e repetir links e recursos, sem aceitar `file://` como evidência de subcaminho.
- Confirmar que nenhum `href`/`src` próprio começa por `/`.
- Confirmar que a raiz com `#/...` e com `?print-pdf` chega à Unidade 1 preservando query e fragmento.
- Confirmar que a raiz nua permanece no catálogo.

### Validações manuais obrigatórias de QA

- Catálogo em 320 × 568, 390 × 844, 768 × 1024 e 1440 × 900, mais zoom de 200%.
- Ordem de `Tab`/`Shift+Tab`, acionamento por `Enter`, foco visível e nomes acessíveis.
- Troca Unidade 1 → catálogo → Unidade 2 e caminho inverso em duas ações.
- Reveal das duas unidades: setas, hash, controles, progresso, `c/t`, auto-animate, transições, busca, zoom, notas, KaTeX e destaque.
- Quiz da Unidade 1 com alternativa correta e incorreta.
- Primeiro slide, conteúdo denso e último slide sem barra sobreposta.
- Entrada e saída de fullscreen nas duas unidades; barra ausente durante fullscreen e restaurada depois.
- `?print-pdf` e pré-visualização paisagem das duas unidades; barra e espaço residual ausentes.
- Recarga em fragmentos Reveal válidos dentro das rotas próprias.
- Simulação não versionada de uma terceira unidade para comprovar que somente a pasta nova e um item no catálogo são necessários.

## Documentação

`ADICIONAR_UNIDADE.md` documenta convenção `unidade-N/`, arquivos mínimos, edição única do catálogo, links relativos, servidor local, teste sob subcaminho, verificação de 404 e cuidados para não editar apresentações anteriores. A documentação de publicação existente deve ser ajustada somente onde descreve a antiga raiz como apresentação, mantendo branch `main`, pasta `/ (root)` e `.nojekyll`.

## Riscos e mitigações

| Risco | Mitigação / critério de decisão |
|---|---|
| A raiz nua deixa de abrir diretamente a Unidade 1. | Mudança necessária para atender ao catálogo raiz; preservar links profundos `#/...` e `?print-pdf`, documentar a quebra da raiz nua. |
| CSS do Reveal força altura de viewport e pode conflitar com a linha da barra. | Carregar `unit-shell.css` por último, limitar regras à shell e validar primeiro/denso/último slide nas duas versões Reveal. |
| Implementação de fullscreen varia conforme navegador/elemento alvo. | Cobrir documento e elemento `.reveal` somente com CSS; QA testa entrada e saída real. Sem listeners globais. |
| Hash completo de `index.html` muda. | Mudança limitada e auditada; hash exato da região de slides permanece, demais quatro arquivos por unidade mantêm hash completo. |
| Dependências CDN falham sem internet. | Limitação já existente e fora de escopo; não alterar versões nem introduzir fallback. |
| Redirecionamento legado pode reservar fragmentos `#/` no catálogo. | O catálogo não usa esse namespace; registrar a convenção. |

## Restrições de implementação

- Não revisar, corrigir, formatar ou reorganizar conteúdo dos slides.
- Não unificar versões do Reveal.js, CDN, configurações ou CSS gerados.
- Não introduzir bundler, framework, backend, service worker, iframe ou etapa obrigatória de build.
- Não capturar teclado/gestos para a barra.
- Não executar formatação automática sobre arquivos protegidos.
- Não alterar `.nojekyll` nem a origem de publicação `main` + `/ (root)`.

## Handoff

- **Papel:** Tech Lead
- **Status:** READY
- **Resumo:** rotas, compatibilidade histórica, catálogo central, shell externa, preservação por hashes e validação foram definidos.
- **Arquivos de propriedade:** `technical-plan.md`, `tasks.md`.
- **IDs relacionados:** REQ-001 a REQ-006; AC-001 a AC-027; DES-001 a DES-011; TASK-001 a TASK-005.
- **Evidências usadas:** estrutura estática sem build; Unidade 1 com 53 seções; Unidade 2 com 67 seções; recursos próprios relativos; hashes completos de `research.md`; hashes das regiões de slides registrados neste plano.
- **Próximo responsável:** Coder, executando `TASK-001` a `TASK-005` em ordem e registrando evidências em `implementation.md`.
