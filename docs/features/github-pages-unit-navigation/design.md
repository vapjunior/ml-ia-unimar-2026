# Design — catálogo e navegação de unidades no GitHub Pages

Status: **READY**

Data: 25/09/2026

## Objetivo de experiência

Oferecer uma entrada simples para as unidades publicadas e um caminho explícito de volta ao catálogo, sem incorporar navegação à área dos slides nem alterar a experiência didática do Reveal.js. A solução deve funcionar do viewport de 320 px ao de 1440 px, sob o subcaminho de um GitHub Pages de projeto, com teclado e tecnologias assistivas.

Este documento detalha **REQ-003**, **REQ-004**, **REQ-005** e **REQ-006** e as restrições de preservação de **REQ-001** e **REQ-002**. As fontes são `prd.md` e `research.md` desta funcionalidade.

## Leitura da experiência atual

A inspeção do estado presente do repositório confirma uma separação adequada entre navegação e conteúdo didático:

- a raiz pública funciona como catálogo e apresenta duas âncoras nativas, uma para cada unidade publicada;
- a Unidade 1 permanece uma apresentação de 53 seções e a Unidade 2, uma apresentação de 67 seções;
- cada apresentação possui um único caminho explícito de retorno antes do canvas Reveal e fora de `.reveal .slides`;
- os estilos de catálogo e da navegação de retorno estão separados dos estilos próprios das apresentações;
- nomes, ordem e destinos das unidades ficam no catálogo, sem cartões inativos para conteúdo futuro.

Essa leitura serve para alinhar a especificação ao material recebido e não substitui a validação independente de QA. O conteúdo das apresentações — inclusive textos, ordem, fórmulas, exemplos, referências, tema e comportamento — continua tratado como imutável para fins de Design. A única superfície nova é a navegação externa descrita neste documento.

## Princípios

1. **O catálogo é a entrada; cada unidade é um destino.** A raiz não reproduz conteúdo dos slides e não tenta funcionar como apresentação.
2. **A navegação entre unidades fica fora do canvas.** Nenhum título, seção, controle ou gesto do Reveal.js é reutilizado para o catálogo.
3. **Uma unidade publicada é uma opção real.** Unidades futuras não aparecem como cartões desabilitados, “em breve” ou links sem destino.
4. **A navegação principal usa comportamento nativo da Web.** Links são âncoras comuns, sem captura global de teclado, gesto ou roda do mouse.
5. **O endereço é portátil.** Links internos são relativos ao site e não pressupõem a raiz do domínio.

## Arquitetura da informação

### Entrada do site

A URL raiz apresenta, nesta ordem:

1. cabeçalho do curso;
2. título principal “Aprendizagem de Máquina”;
3. instrução curta “Escolha uma unidade para abrir a apresentação.”;
4. região de navegação “Unidades disponíveis”;
5. lista ordenada das unidades publicadas.

O catálogo inicial contém exatamente estas opções:

| Ordem | Rótulo visível | Nome acessível mínimo |
|---|---|---|
| 1 | **Unidade 1** — Fundamentos teóricos da aprendizagem | Abrir Unidade 1 — Fundamentos teóricos da aprendizagem |
| 2 | **Unidade 2** — Regressão | Abrir Unidade 2 — Regressão |

Não há cartão genérico, espaço reservado ou contador para uma unidade futura. A inclusão posterior acrescenta um item à mesma lista e segue a sequência numérica definida na fonte central do catálogo (**AC-015**, **AC-016**, **AC-018**).

### Página de uma unidade

Em uso normal, a página de cada unidade possui duas regiões distintas:

1. uma barra utilitária compacta com o link visível “Todas as unidades” e nome acessível “Voltar ao catálogo de unidades”;
2. o canvas original do Reveal.js, sem elementos do catálogo dentro de `.slides`.

A barra é anterior ao canvas na ordem de leitura e de foco. Ela não apresenta seletor com todas as unidades nem links anterior/próxima: uma única saída consistente reduz interferência e garante a jornada em duas ações prevista por **AC-013**.

```text
┌─────────────────────────────────────────────┐
│ ← Todas as unidades                         │  barra externa
├─────────────────────────────────────────────┤
│                                             │
│          apresentação Reveal.js             │  conteúdo preservado
│                                             │
└─────────────────────────────────────────────┘
```

## Jornada principal

### Estudante no catálogo

1. Abre a raiz do site.
2. Lê o título e encontra as unidades em ordem.
3. Aciona o cartão da unidade por clique, toque ou `Enter`.
4. A apresentação abre na mesma aba e mantém seu comportamento Reveal.js.

### Troca de unidade

1. Na Unidade 1 ou 2, aciona “Todas as unidades”.
2. No catálogo, aciona a outra unidade.

São duas ações explícitas, sem depender do botão Voltar do navegador (**AC-013**).

### Apresentação em tela cheia

1. Ao entrar em tela cheia, a barra utilitária deixa de ocupar espaço e somente o Reveal.js permanece visível.
2. O apresentador usa teclado, gestos e controles sem uma camada adicional sobre os slides.
3. Ao sair da tela cheia, a barra reaparece no modo normal, preservando o caminho ao catálogo.

### Impressão ou PDF

1. Ao abrir a unidade com `?print-pdf` ou imprimir, a barra utilitária é removida do layout antes da composição das páginas.
2. Nenhum rótulo, espaço reservado, fundo, sombra ou margem da barra aparece no PDF.
3. Os slides ocupam a área prevista pela apresentação original (**AC-004**, **AC-009**, **AC-014**).

## Especificação visual do catálogo

### Direção visual

O catálogo usa uma linguagem neutra e coerente com as apresentações existentes: fundo muito claro, texto azul-marinho e detalhes em azul. Ele não replica componentes internos dos slides e não altera seus arquivos de estilo.

Tokens recomendados, sujeitos à validação de contraste na implementação:

| Uso | Valor |
|---|---|
| Fundo da página | `#F8FBFD` |
| Superfície do cartão | `#FFFFFF` |
| Texto principal | `#173F5F` |
| Texto secundário | `#3D5363` |
| Borda | `#B9D2E2` |
| Ação e foco | `#173F5F` |
| Fonte | pilha de sistema (`system-ui`, sem dependência nova) |

A tipografia deve respeitar zoom do navegador e preferências do sistema; medidas de texto devem usar unidades relativas. O conteúdo principal tem largura máxima aproximada de 1120 px e permanece centralizado com respiro lateral fluido.

### Cartão de unidade

Cada cartão é **um único link**, sem botão ou link aninhado. Sua composição é:

- identificador “Unidade N”;
- título completo da unidade;
- chamada textual “Abrir apresentação”, acompanhada por indicação visual de avanço;
- toda a superfície do cartão acionável, com alvo mínimo de 44 × 44 CSS px.

O título e a chamada tornam a ação compreensível sem depender de cor ou do ícone. O indicador de avanço é decorativo e não entra no nome acessível. Não devem ser inventados carga horária, status, resumo ou data para o catálogo.

### Estados

| Estado | Comportamento verificável |
|---|---|
| Padrão | Título e ação legíveis; cartão identificado também por borda/forma, não apenas por cor. |
| Hover | Borda e fundo ganham ênfase discreta; nenhuma informação aparece exclusivamente no hover. |
| Foco | Contorno contínuo de pelo menos 3 px, com contraste mínimo de 3:1 e sem ser cortado. |
| Ativo | Resposta visual curta de pressionamento, sem deslocamento que cause instabilidade. |
| Visitado | Pode manter o mesmo tratamento visual; não pode reduzir contraste ou ocultar a opção. |
| Indisponível | O item não é renderizado. Não existe cartão sem link. |

Transições, se usadas, limitam-se a cor, borda e sombra. Sob `prefers-reduced-motion: reduce`, devem ser removidas. Não há entrada animada obrigatória.

## Comportamento responsivo

### Desktop e tablet largo — a partir de 768 px

- cabeçalho e instrução permanecem alinhados ao início do conteúdo;
- lista de unidades usa duas colunas de largura equivalente;
- cartões da mesma linha têm altura visual consistente sem truncar texto;
- espaçamento entre cartões é de aproximadamente 24 px;
- a ordem visual e a ordem do DOM são Unidade 1, Unidade 2 e unidades posteriores.
- quando uma futura unidade formar uma última linha incompleta, ela permanece alinhada ao início da grade; não se centraliza nem se reordena para preencher lacunas.

### Mobile e tablet estreito — de 320 px a 767 px

- lista usa uma única coluna;
- conteúdo tem margem lateral mínima de 16 px;
- títulos quebram em linhas naturais, sem elipse e sem redução forçada da fonte;
- cartão preserva área acionável confortável e espaçamento mínimo de 12 px entre itens;
- não há rolagem horizontal no viewport de 320 px (**AC-024**).

### Barra utilitária nas unidades

- usa toda a largura disponível e altura mínima de 44 px;
- respeita `env(safe-area-inset-top)` e `env(safe-area-inset-left)` quando disponíveis;
- o link fica alinhado ao início e não quebra em duas linhas a 320 px;
- o canvas recebe somente o espaço restante do viewport, sem ficar sob a barra e sem corte;
- em tela cheia, a barra é removida e o canvas recupera 100% do viewport;
- em impressão, a barra e o espaço por ela reservado usam `display: none`, sem margem residual.

A barra não deve se tornar menu flutuante, gaveta, modal ou controle sobreposto. Isso evita colisão com títulos, controles, número do slide, progresso e áreas clicáveis do Reveal.

## Acessibilidade e teclado

### Estrutura semântica do catálogo

- `html` declara `lang="pt-BR"`;
- existe um único `h1` para “Aprendizagem de Máquina”;
- “Unidades disponíveis” identifica uma região `nav`;
- as unidades formam uma lista semântica;
- cada unidade usa uma âncora com destino real e nome acessível completo;
- a sequência dos títulos não salta níveis sem necessidade.

### Operação por teclado

- `Tab` percorre cada cartão uma vez, na ordem das unidades;
- `Shift+Tab` percorre em ordem inversa;
- `Enter` abre a unidade focalizada;
- não há `tabindex` positivo nem atalhos de uma só tecla no catálogo;
- dentro da apresentação, a barra adiciona somente um link nativo à ordem de foco;
- nenhuma implementação da barra escuta `keydown`, `keyup`, setas, espaço, `F`, `S`, `O`, `Esc` ou gestos; os eventos continuam pertencendo ao navegador e ao Reveal.js (**AC-002**, **AC-008**, **AC-014**).

### Percepção

- contraste de texto normal é de pelo menos 4,5:1; texto grande, pelo menos 3:1;
- foco e componentes gráficos essenciais têm contraste de pelo menos 3:1;
- foco nunca depende somente de mudança de cor;
- nenhuma informação depende apenas de cor, posição ou ícone (**AC-026**, **AC-027**);
- zoom de texto a 200% não oculta unidade, título, ação ou foco;
- o texto visível e o nome acessível identificam o mesmo destino, evitando rótulos divergentes.

## Contrato de preservação do Reveal.js

A navegação complementar atende aos seguintes limites de Design:

1. fica fora de `.reveal .slides` e não muda a ordem, quantidade ou marcação das seções;
2. não redefine estilos globais usados pelas apresentações; seus seletores e recursos visuais são isolados;
3. não adiciona listeners globais de teclado, toque, ponteiro ou histórico;
4. não bloqueia controles, progresso, número do slide, links, quiz ou notas;
5. não altera ou remove query string e fragmento Reveal da URL durante o uso da unidade;
6. desaparece completamente em `?print-pdf`, impressão e tela cheia;
7. não usa `iframe`, pois isso acrescentaria fronteiras de foco, histórico, fragmento e impressão à experiência;
8. qualquer ajuste indispensável no HTML protegido limita-se ao ponto de integração externo ao conteúdo, conforme justificativa exigida por **AC-005** e **AC-010**.

O Tech Lead deve definir o mecanismo técnico exato. A implementação é aceitável visualmente somente se o canvas não ficar encoberto e as apresentações continuarem funcionais em modo normal, tela cheia e impressão.

## Regras de URL e subcaminho

- cartões e retorno usam referências relativas; nenhum `href` interno começa por `/`;
- cada cartão aponta para a rota própria e previsível definida pelo Tech Lead;
- o retorno de qualquer unidade aponta para a raiz relativa do catálogo, sem codificar domínio, usuário GitHub ou nome do repositório;
- a URL de uma unidade aceita recarga com query string e fragmento Reveal, mantendo a mesma unidade e o mesmo slide (**AC-021**, **AC-023**);
- abrir uma unidade substitui a página atual; não se usa `target="_blank"` como comportamento padrão;
- a evolução do catálogo altera um único ponto central de dados ou marcação, sem editar apresentações anteriores (**AC-016**, **AC-018**).

Exemplo conceitual, sem fixar a decisão de rotas:

```text
/<subcaminho-do-projeto>/                  catálogo
/<subcaminho-do-projeto>/<rota-unidade>/   apresentação
```

## Critérios verificáveis de Design

| ID | Verificação | Rastreabilidade |
|---|---|---|
| DES-001 | A raiz exibe os dois rótulos integrais e somente unidades publicadas. | REQ-003; AC-011, AC-015 |
| DES-002 | Unidade 1 e Unidade 2 são links únicos acionáveis por clique, toque e teclado. | REQ-003, REQ-006; AC-012, AC-025, AC-026 |
| DES-003 | De qualquer unidade, “Todas as unidades” leva ao catálogo; o próximo acionamento abre a outra unidade. | REQ-003; AC-013 |
| DES-004 | Barra e espaço reservado são inexistentes na impressão/PDF. | REQ-001, REQ-002, REQ-003; AC-004, AC-009, AC-014 |
| DES-005 | Barra é inexistente em tela cheia e reaparece ao sair dela. | REQ-001, REQ-002, REQ-003; AC-002, AC-008, AC-014 |
| DES-006 | A navegação complementar não escuta teclas/gestos e fica fora da árvore de slides. | REQ-001, REQ-002, REQ-003; AC-002, AC-008, AC-014 |
| DES-007 | Catálogo não produz rolagem horizontal nem truncamento entre 320 px e 1440 px. | REQ-006; AC-024 |
| DES-008 | O foco é visível, não cortado e segue Unidade 1, Unidade 2 e unidades posteriores. | REQ-006; AC-025, AC-026 |
| DES-009 | Ação, disponibilidade e destino são compreensíveis sem depender de cor. | REQ-003, REQ-006; AC-015, AC-027 |
| DES-010 | Links funcionam no subcaminho de projeto e em servidor local, sem origem absoluta. | REQ-003, REQ-005; AC-012, AC-021 |
| DES-011 | Nova unidade acrescenta um cartão na lista central e não muda páginas já publicadas. | REQ-004; AC-016, AC-018 |

## Cenários mínimos para validação visual e de interação

1. Catálogo em 320 × 568, 390 × 844, 768 × 1024 e 1440 × 900.
2. Navegação completa por teclado com foco visível e zoom do navegador em 200%.
3. Entrada e saída de tela cheia nas duas apresentações.
4. Primeiro slide, slide com conteúdo denso, quiz da Unidade 1 e slide final em modo normal, garantindo que a barra não encubra o canvas.
5. `?print-pdf` e pré-visualização de impressão das duas unidades, confirmando ausência total da barra.
6. Acesso local e acesso em subcaminho equivalente a `/ml-ia-unimar-2026/`.
7. Recarga de cada unidade com fragmento Reveal válido.
8. Simulação de uma terceira unidade no ponto central para confirmar ordem, quebra responsiva e ausência de edição nas unidades anteriores.

## Decisões para o Tech Lead

- Definir as rotas finais das unidades e a estratégia de compatibilidade para links antigos da raiz com fragmento Reveal, risco já apontado em `research.md`.
- Escolher uma integração externa ao canvas que preserve os arquivos gerados ao máximo e documentar qualquer divergência de hash.
- Isolar os estilos do catálogo e da barra para que não vazem para seletores Reveal.
- Definir a fonte central e documentada das unidades, mantendo o site estático e sem build obrigatório.
- Garantir que a barra tenha altura contabilizada apenas no modo normal e seja removida antes do layout de impressão e durante tela cheia.

## Handoff

- **Papel:** Design
- **Status:** READY
- **Resumo:** experiência atual analisada e especificação do catálogo raiz, cartões responsivos e barra externa de retorno consolidada; estados, teclado, acessibilidade, impressão, tela cheia, subcaminho e expansão para futuras unidades estão cobertos sem reescrever slides.
- **Arquivo de propriedade:** `docs/features/github-pages-unit-navigation/design.md`
- **IDs relacionados:** REQ-001 a REQ-006; AC-002, AC-004, AC-008, AC-009 e AC-011 a AC-027; DES-001 a DES-011.
- **Evidências de inspeção:** catálogo com duas opções publicadas; retorno explícito presente nas duas unidades; 53 seções na Unidade 1 e 67 na Unidade 2; estilos externos separados em `assets/catalog.css` e `assets/unit-shell.css`.
- **Pendências:** decisões técnicas de rotas, compatibilidade da antiga raiz, fonte central e mecanismo de integração.
- **Próximo responsável:** Tech Lead, para produzir `technical-plan.md` e `tasks.md` com tarefas READY.
