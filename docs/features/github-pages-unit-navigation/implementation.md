# Implementação — catálogo e navegação de unidades no GitHub Pages

Status: **IMPLEMENTED**

Data: 25/09/2026

## Handoff

- **De:** Coder
- **Para:** QA
- **Estado validado:** árvore de trabalho não commitada sobre `fa10de1cad96ca5f4fb0a365b6c417cfb885e520`
- **TASKs implementadas:** TASK-001 a TASK-005
- **Rastreabilidade:** REQ-001 a REQ-006; AC-001 a AC-027; DES-001 a DES-011
- **Decisão de qualidade:** implementação pronta para validação independente; este relatório não representa aprovação de QA.

## Resultado implementado

- A raiz passou a ser o catálogo estático e contém somente as duas unidades publicadas.
- A Unidade 1 foi realocada para `unidade-1/` e a Unidade 2 para `unidade-2/`.
- As apresentações receberam apenas uma referência a `../assets/unit-shell.css` no `head` e uma barra externa anterior a `.reveal`, fora da região de slides.
- `assets/catalog.css` implementa catálogo responsivo, foco visível, alvos acionáveis e redução de movimento.
- `assets/unit-shell.css` reserva o espaço da barra no modo normal e a remove em impressão e fullscreen sem JavaScript.
- `scripts/verify-presentation-integrity.py` protege os oito arquivos imutáveis, as regiões de slides e suas contagens.
- `ADICIONAR_UNIDADE.md`, `README.md` e `PUBLICAR_GITHUB_PAGES.md` documentam manutenção e publicação sem build.
- O diretório-fonte residual `ml-unidade2-regressao-reveal/` foi reconfirmado sem arquivos e seus três diretórios vazios foram removidos com `rmdir`.

## Mapa final de URLs

| Entrada | Rota local relativa | GitHub Pages de projeto |
|---|---|---|
| Catálogo | `./` | `/ml-ia-unimar-2026/` |
| Unidade 1 | `./unidade-1/` | `/ml-ia-unimar-2026/unidade-1/` |
| Unidade 2 | `./unidade-2/` | `/ml-ia-unimar-2026/unidade-2/` |

Os cartões usam `./unidade-1/` e `./unidade-2/`; cada barra usa `../`. A raiz preserva URLs históricas iniciadas por `#/` ou contendo o parâmetro `print-pdf` por `location.replace`, mantendo `location.search` e `location.hash` e encaminhando para a Unidade 1. A raiz nua permanece no catálogo.

## Preservação e hashes

O comando `python3 scripts/verify-presentation-integrity.py` encerrou com código zero e produziu:

```text
Integridade preservada: 8 arquivos imutáveis conferidos.
Unidade 1: região de slides preservada; 53 seções.
Unidade 2: região de slides preservada; 67 seções.
```

### Arquivos imutáveis

| Unidade | Arquivo | SHA-256 obtido |
|---|---|---|
| 1 | `css/custom.css` | `20607ecc28571aee1dbdf335e88a6f061a98b843578d6d454317d3701418b904` |
| 1 | `js/slides.js` | `cd001b0523072e3411d8a81192a2ee1901e86300b2d94012727891c0f266c062` |
| 1 | `README.md` | `aeb785de67bb3a9f669a024b03135581c00b85117802f9fc4a2625b045cd6bb6` |
| 1 | `REFERENCIAS.md` | `6474d050ca014ed2512509271ad0d56e68e18fc1868c59b0ca8256e49c605c03` |
| 2 | `css/custom.css` | `0d7e269135ba3c87bc73fc0136d115f1f69659e16bac5042de2759dd53e2e303` |
| 2 | `js/slides.js` | `d7996e6ba26a045ea8694e440f73e73256ecb007f3849e2424a42e44f8b265c1` |
| 2 | `README.md` | `b259dd9d84822878f3972ddeb17629807219217d725003809f8fab188f52233e` |
| 2 | `REFERENCIAS.md` | `86425599ff6ef61b897a2ce4ceb91a534079342557fd1cac7190d7b676b4cf78` |

Todos coincidem com `research.md`.

### HTML das apresentações

| Unidade | SHA-256 completo de referência | SHA-256 completo final | SHA-256 da região de slides | Seções |
|---|---|---|---|---:|
| 1 | `597a43658092471ac7fbb4c2a6c308b634ce2c467928457732c82683062ca797` | `114835f24e20c9fdee85c8147209c1975c887beea1bd07d86e999b7e6471cd33` | `e938e752fbbf1d17a836f21e00aec3ca3539c7f937f447d782a969af7892a15b` | 53 |
| 2 | `b6044f4b5aa83eea1bab70f7b9aaae7cc2580b2d69a907d893aa763bc9e62b7e` | `f7b5dee9a18c45ce2d46e0c7d700fd98f24b543be054a52b4a0809efe88bae33` | `7e39c98217d44fe4a564dc2ad919d009a753614fa4a177dd0ff7891dd55ab4f2` | 67 |

A divergência dos hashes completos dos dois `index.html` é esperada e se limita às duas inserções externas previstas: o `link` para o CSS compartilhado no `head` e a navegação irmã anterior a `.reveal`. Nenhum byte entre o primeiro `<section` e o último `</section>` foi alterado.

## Arquivos do escopo

- Realocados: `unidade-1/**` e `unidade-2/**`.
- Criados: `assets/catalog.css`, `assets/unit-shell.css`, `scripts/verify-presentation-integrity.py`, `ADICIONAR_UNIDADE.md` e este relatório.
- Atualizados: `index.html`, `README.md` e `PUBLICAR_GITHUB_PAGES.md`.
- Removidos da raiz por realocação: `css/custom.css`, `js/slides.js` e `REFERENCIAS.md`.
- Preservado: `.nojekyll` e a publicação por `main` + `/ (root)`.

## Comandos e resultados reais

| Comando | Resultado |
|---|---|
| `python3 scripts/verify-presentation-integrity.py` | código 0; oito arquivos imutáveis, duas regiões de slides e contagens 53/67 preservados |
| `shasum -a 256 ...` nos dez arquivos protegidos/finais | hashes registrados nas tabelas acima |
| `rg -c '<section(?:\\s|>)' unidade-1/index.html unidade-2/index.html` | `53` e `67` |
| `find ml-unidade2-regressao-reveal -mindepth 1 -type f -print` | saída vazia |
| `rmdir ml-unidade2-regressao-reveal/css ml-unidade2-regressao-reveal/js ml-unidade2-regressao-reveal` | código 0; árvore residual ausente após o comando |
| `git rev-parse HEAD` | `fa10de1cad96ca5f4fb0a365b6c417cfb885e520` |
| `python3 -m http.server 8766 --bind 127.0.0.1` na raiz | servidor iniciado, mas a checagem HTTP em outro processo não conseguiu conectar no isolamento disponível |
| `python3 -m http.server 8767 --bind 127.0.0.1` no diretório pai | servidor iniciado, mas a checagem HTTP em outro processo não conseguiu conectar no isolamento disponível |

O estado entregue é a árvore de trabalho não commitada sobre o commit-base acima. `git status --short` identifica `PUBLICAR_GITHUB_PAGES.md`, `README.md` e `index.html` como modificados; `REFERENCIAS.md`, `css/custom.css` e `js/slides.js` da raiz como removidos por realocação; e `ADICIONAR_UNIDADE.md`, `assets/`, `docs/`, `scripts/`, `unidade-1/` e `unidade-2/` como novos/não rastreados.

## Validações pendentes para QA

As seguintes verificações não foram concluídas no ambiente do Coder e não são declaradas como aprovadas:

- smoke HTTP completo na raiz e sob `/ml-ia-unimar-2026/`, incluindo ausência de 404 em todos os recursos próprios;
- execução real do redirecionamento histórico de `#/...` e `?print-pdf` em navegador;
- catálogo nos viewports 320 × 568, 390 × 844, 768 × 1024 e 1440 × 900, zoom de 200%, `Tab`, `Shift+Tab`, `Enter`, foco e contraste;
- Reveal.js nas duas unidades: setas, hashes, controles, progresso, `c/t`, auto-animate, transições, notas, busca, zoom, KaTeX e destaque;
- quiz da Unidade 1 com respostas correta e incorreta;
- fullscreen real e retorno da barra nas duas unidades;
- `?print-pdf` e pré-visualização paisagem sem barra ou espaço residual;
- recarga em fragmentos Reveal válidos e simulação não versionada de Unidade 3.

## Limitações e riscos conhecidos

- Reveal.js, KaTeX e plugins continuam dependentes da CDN jsDelivr; funcionamento offline permanece fora do escopo.
- A raiz nua agora é o catálogo; somente links históricos com hash Reveal ou `print-pdf` são encaminhados à Unidade 1.
- A integração de fullscreen é exclusivamente CSS e precisa de validação real pelos navegadores-alvo.
- O teste HTTP ficou inconclusivo por isolamento entre processos no ambiente de execução, não por uma resposta 404 observada.

## Próximo responsável

**QA** deve validar exatamente a árvore de trabalho sobre `fa10de1cad96ca5f4fb0a365b6c417cfb885e520`, repetir o verificador de integridade, revisar as duas inserções externas nos HTMLs e executar as validações HTTP e de navegador pendentes. Em caso de defeito, registrar `BUG-NNN` e retornar ao Tech Lead para criação de TASK corretiva.
