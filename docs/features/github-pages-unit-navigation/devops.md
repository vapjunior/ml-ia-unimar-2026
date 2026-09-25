# DevOps — validação HTTP da navegação de unidades

## Handoff

- **Papel:** DevOps
- **Status:** **VALIDATED — HTTP na raiz e no subcaminho**
- **Data:** 25/09/2026
- **Versão de referência:** árvore de trabalho não commitada sobre `fa10de1cad96ca5f4fb0a365b6c417cfb885e520`
- **Escopo:** suporte ambiental para a validação HTTP de AC-012 e AC-021, sem alteração do código da aplicação ou do conteúdo das apresentações
- **Arquivos sob responsabilidade:** somente este `devops.md`
- **Próximo destinatário:** QA

## Resumo

Foi definido um smoke HTTP reproduzível que serve e consulta a mesma árvore no mesmo processo, usando uma porta efêmera escolhida pelo sistema operacional. O procedimento cobre os dois modos exigidos pelo plano:

1. repositório como document root, com catálogo em `/`;
2. diretório pai como document root, com catálogo em `/ml-ia-unimar-2026/`, simulando o subcaminho de um GitHub Pages de projeto.

O procedimento consulta catálogo, páginas das duas unidades, CSS compartilhados e CSS/JS próprios das duas apresentações. O servidor é encerrado no bloco `finally`, sem processo persistente e sem artefato temporário.

A execução dentro do sandbox não chegou ao HTTP: a criação do socket falhou em `bind()` com `PermissionError: [Errno 1] Operation not permitted`. Em uma segunda rodada ambiental, o comando aprovado `python3 -m http.server` foi executado fora do sandbox, a partir do diretório pai. Um cliente `curl` também executado fora do sandbox confirmou HTTP 200 para os nove recursos sob `/ml-ia-unimar-2026/`. O servidor foi encerrado normalmente com `Ctrl+C` após a coleta.

O acesso pelo navegador não foi necessário nas rodadas ambientais porque a alternativa autorizada por `curl` produziu evidência HTTP completa. Em seguida, o mesmo método foi repetido com o próprio repositório como document root: os nove recursos equivalentes na raiz também responderam 200. Assim, a cobertura HTTP prevista no plano está concluída nos dois modos; os testes comportamentais de navegador continuam com QA.

## Diagnóstico de porta, processo e isolamento

O inventário de listeners encontrou, além de processos do sistema, um processo Python em `127.0.0.1:8877`:

```text
Python 60492 macbook 4u IPv4 ... TCP 127.0.0.1:8877 (LISTEN)
```

Esse listener não ficou acessível a partir do sandbox:

```text
curl: (7) Failed to connect to 127.0.0.1 port 8877 after 0 ms: Couldn't connect to server
```

A inspeção do processo com `ps` também foi negada pelo ambiente:

```text
zsh:1: operation not permitted: ps
```

Em seguida, o smoke tentou abrir seu próprio servidor em `127.0.0.1` com porta `0`, eliminando conflito de porta. A falha ocorreu antes de qualquer requisição:

```text
PermissionError: [Errno 1] Operation not permitted
```

Conclusão ambiental: o sandbox desta execução bloqueia a abertura do socket local e também isola o cliente de um listener iniciado fora dele. Fora do sandbox, a porta explícita 8766 funcionou e não houve conflito ou resposta 404 nos recursos verificados.

O processo preexistente na porta 8877 não foi encerrado porque sua origem não pôde ser confirmada e a remoção não era necessária para o método com porta efêmera.

## Evidência HTTP real — subcaminho do GitHub Pages

Servidor executado a partir de `/Users/macbook/Workspace`:

```bash
python3 -m http.server 8766 --bind 127.0.0.1
```

URL de catálogo para navegador: `http://127.0.0.1:8766/ml-ia-unimar-2026/`.

Resultados coletados pelo cliente externo:

| URL | Status | Content-Type |
|---|---:|---|
| `/ml-ia-unimar-2026/` | 200 | `text/html` |
| `/ml-ia-unimar-2026/assets/catalog.css` | 200 | `text/css` |
| `/ml-ia-unimar-2026/assets/unit-shell.css` | 200 | `text/css` |
| `/ml-ia-unimar-2026/unidade-1/` | 200 | `text/html` |
| `/ml-ia-unimar-2026/unidade-1/css/custom.css` | 200 | `text/css` |
| `/ml-ia-unimar-2026/unidade-1/js/slides.js` | 200 | `text/javascript` |
| `/ml-ia-unimar-2026/unidade-2/` | 200 | `text/html` |
| `/ml-ia-unimar-2026/unidade-2/css/custom.css` | 200 | `text/css` |
| `/ml-ia-unimar-2026/unidade-2/js/slides.js` | 200 | `text/javascript` |

O log do `http.server` registrou `GET ... HTTP/1.1" 200` para os nove caminhos. O processo encerrou com código 0 após `Keyboard interrupt received, exiting.`. Não permaneceu servidor criado por esta rodada.

## Evidência HTTP real — raiz do site

Servidor executado a partir de `/Users/macbook/Workspace/ml-ia-unimar-2026`:

```bash
python3 -m http.server 8768 --bind 127.0.0.1
```

URL de catálogo: `http://127.0.0.1:8768/`.

| URL | Status | Content-Type |
|---|---:|---|
| `/` | 200 | `text/html` |
| `/assets/catalog.css` | 200 | `text/css` |
| `/assets/unit-shell.css` | 200 | `text/css` |
| `/unidade-1/` | 200 | `text/html` |
| `/unidade-1/css/custom.css` | 200 | `text/css` |
| `/unidade-1/js/slides.js` | 200 | `text/javascript` |
| `/unidade-2/` | 200 | `text/html` |
| `/unidade-2/css/custom.css` | 200 | `text/css` |
| `/unidade-2/js/slides.js` | 200 | `text/javascript` |

O log do servidor confirmou nove requisições `GET` com status 200. A sessão foi encerrada com `Ctrl+C` e código 0; nenhum servidor desta validação permaneceu ativo.

## Recursos abrangidos pelo smoke

Para cada modo de publicação, devem retornar HTTP 200:

| Recurso | Caminho relativo |
|---|---|
| Catálogo | `./` |
| CSS do catálogo | `assets/catalog.css` |
| CSS compartilhado da barra | `assets/unit-shell.css` |
| Unidade 1 | `unidade-1/` |
| CSS da Unidade 1 | `unidade-1/css/custom.css` |
| JavaScript da Unidade 1 | `unidade-1/js/slides.js` |
| Unidade 2 | `unidade-2/` |
| CSS da Unidade 2 | `unidade-2/css/custom.css` |
| JavaScript da Unidade 2 | `unidade-2/js/slides.js` |

O inventário estático confirmou que esses são os recursos locais referenciados pelos três HTMLs. Dependências Reveal.js e plugins permanecem em CDN e não são objeto deste smoke local.

## Procedimento reproduzível recomendado

Executar o script abaixo **fora do sandbox que bloqueia sockets**, a partir de `/Users/macbook/Workspace/ml-ia-unimar-2026`. O processo imprime a URL de navegador e o status, tipo de conteúdo e URL final de cada recurso. Ele usa somente a biblioteca padrão do Python e não altera arquivos.

```bash
python3 -c '
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from threading import Thread
from urllib.request import urlopen

repo = Path.cwd().resolve()
checks = [
    ("catalogo", ""),
    ("catalog-css", "assets/catalog.css"),
    ("unit-shell-css", "assets/unit-shell.css"),
    ("unidade-1", "unidade-1/"),
    ("unidade-1-css", "unidade-1/css/custom.css"),
    ("unidade-1-js", "unidade-1/js/slides.js"),
    ("unidade-2", "unidade-2/"),
    ("unidade-2-css", "unidade-2/css/custom.css"),
    ("unidade-2-js", "unidade-2/js/slides.js"),
]

class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

def smoke(label, document_root, prefix):
    handler = partial(Quiet, directory=str(document_root))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{server.server_port}/{prefix}"
    print(f"[{label}] navegador={base}")
    try:
        for name, relative in checks:
            with urlopen(base + relative, timeout=5) as response:
                print(name, response.status,
                      response.headers.get_content_type(), response.geturl())
    finally:
        server.shutdown()
        server.server_close()
        thread.join()

smoke("raiz", repo, "")
smoke("prefixo", repo.parent, repo.name + "/")
'
```

Para inspeção manual persistente no navegador, usar uma porta livre conhecida em um terminal fora do sandbox:

```bash
cd /Users/macbook/Workspace/ml-ia-unimar-2026
python3 -m http.server 8765 --bind 127.0.0.1
```

Abrir `http://127.0.0.1:8765/`.

Para simular o GitHub Pages sob prefixo:

```bash
cd /Users/macbook/Workspace
python3 -m http.server 8766 --bind 127.0.0.1
```

Abrir `http://127.0.0.1:8766/ml-ia-unimar-2026/`.

## Comandos executados e resultados reais

| Comando | Resultado real |
|---|---|
| leitura de `technical-plan.md`, `implementation.md`, `qa-report.md` e `workflow.md` | artefatos e bloqueio ambiental compreendidos; nenhum arquivo de outro papel alterado |
| `lsof -nP -iTCP -sTCP:LISTEN` | listener Python preexistente observado em `127.0.0.1:8877`; nenhuma decisão de encerrá-lo |
| inventário de `href`/`src` nos três HTMLs com `rg` | recursos locais do catálogo, shell e duas unidades identificados; CDNs mantidas fora do smoke local |
| `ps -p 60492 ...` | negado pelo ambiente com `operation not permitted` |
| `curl --fail --silent --show-error --include --max-time 3 http://127.0.0.1:8877/` | falha de conexão; nenhuma resposta HTTP recebida |
| smoke de servidor e cliente no mesmo processo, em porta efêmera | falhou em `socket.bind()` com `PermissionError: [Errno 1] Operation not permitted` |
| primeira repetição do smoke monolítico fora do sandbox | interrompida durante a solicitação/execução de autorização; sem status HTTP produzido |
| `python3 -m http.server 8766 --bind 127.0.0.1`, a partir de `/Users/macbook/Workspace`, fora do sandbox | servidor iniciado em `127.0.0.1:8766`; sessão persistente criada |
| `curl --fail --silent --show-error ...` para os nove recursos sob `/ml-ia-unimar-2026/`, fora do sandbox | código 0; nove respostas 200 com `text/html`, `text/css` ou `text/javascript` coerentes |
| leitura da saída da sessão do servidor | dezoito entradas 200 observadas: nove da coleta inicial e nove da coleta compacta |
| `Ctrl+C` na sessão persistente | servidor encerrou normalmente com código 0 |
| `python3 -m http.server 8768 --bind 127.0.0.1`, a partir do repositório, fora do sandbox | servidor do modo raiz iniciado em `127.0.0.1:8768` |
| `curl --fail --silent --show-error ...` para os nove recursos na raiz, fora do sandbox | código 0; nove respostas 200 com tipos MIME coerentes |
| leitura da saída e `Ctrl+C` na sessão da porta 8768 | nove entradas 200; servidor encerrado normalmente com código 0 |

## Condição objetiva para revalidação do QA

QA já dispõe de evidência real suficiente para o carregamento HTTP dos nove recursos tanto na raiz quanto no subcaminho de projeto. A condição HTTP foi atendida:

- nove recursos retornaram `200` no modo `raiz`;
- os mesmos nove recursos retornaram `200` no modo `prefixo`;
- a árvore/diff validado permanecer a mesma; qualquer mudança posterior exige identificar a nova versão e repetir as verificações pertinentes.

Permanece com QA abrir o catálogo em navegador e executar os cenários comportamentais já definidos. Essa pendência não invalida a evidência HTTP deste relatório.

Os testes comportamentais de redirecionamento legado, interação Reveal, teclado, viewports, fullscreen e impressão continuam sob responsabilidade de QA em navegador real. Este relatório não os declara executados nem aprovados.

## Pendências e próximo responsável

- **Concluído nesta rodada:** nove respostas HTTP 200 sob `/ml-ia-unimar-2026/`, incluindo catálogo, unidades, CSS e JavaScript locais.
- **Concluído nesta rodada:** nove respostas HTTP 200 com o repositório como document root e catálogo em `/`.
- **Pendência:** QA executar os cenários obrigatórios de navegador já listados em `qa-report.md`.
- **Próximo destinatário:** QA, para a validação comportamental em navegador.
