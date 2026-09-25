# Workflow — Navegação de unidades no GitHub Pages

## Estado atual

- Fase: concluída
- Rodada de QA: 2
- Bloqueios recorrentes: nenhum ativo; o bloqueio HTTP da rodada 1 foi resolvido por DevOps
- Próxima ação: publicar a árvore aprovada no GitHub Pages quando desejado

## Responsáveis e artefatos

| Papel | Estado | Artefato |
|---|---|---|
| Product | READY | `prd.md`, `research.md` |
| Design | READY | `design.md` |
| Tech Lead | READY | `technical-plan.md`, `tasks.md` |
| Coder | IMPLEMENTED | `implementation.md` |
| QA | APPROVED (RODADA 2) | `qa-report.md` |
| DevOps | VALIDATED | `devops.md` |

## Escopo rastreado

- REQ-001 a REQ-006
- AC-001 a AC-027
- DES-001 a DES-011

## Pendências

- Nenhuma pendência obrigatória da funcionalidade.
- A publicação no GitHub Pages permanece uma ação operacional posterior.

## Histórico

- Product analisou as duas apresentações e registrou requisitos, critérios e hashes de referência.
- Design especificou catálogo responsivo e barra utilitária externa ao Reveal, sem interferência em teclado, gestos, tela cheia ou impressão/PDF.
- Tech Lead confirmou `technical-plan.md` e TASK-001 a TASK-005 como READY após inspecionar a implementação parcial.
- O verificador de integridade confirmou 8 arquivos imutáveis, 53 seções na Unidade 1 e 67 na Unidade 2; a evidência final ainda deve ser registrada pelo Coder e repetida pelo QA.
- Coder concluiu TASK-001 a TASK-005, removeu o diretório-fonte residual vazio e registrou o handoff em `implementation.md`; testes reais de navegador ficaram pendentes para QA por limitação ambiental declarada.
- QA rodada 1 confirmou integridade, diff mínimo, semântica e caminhos relativos, mas marcou `BLOCKED` por falta de evidência conclusiva de HTTP e navegador; nenhum defeito foi confirmado.
- DevOps resolveu o bloqueio HTTP: 9/9 recursos na raiz e 9/9 no subcaminho `/ml-ia-unimar-2026/` responderam 200 com tipos MIME coerentes; nenhum arquivo da aplicação foi alterado.
- QA rodada 2 revalidou a mesma árvore e emitiu `APPROVED` para AC-001 a AC-027; nenhum `BUG-NNN` foi aberto. A indisponibilidade de uma sessão visual CUA foi registrada como limitação não bloqueante diante da preservação criptográfica, integração mínima e evidência HTTP real.
