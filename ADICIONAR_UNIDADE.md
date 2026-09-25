# Adicionar uma unidade

O catálogo usa pastas previsíveis no formato `unidade-N/`. Nomes, ordem, disponibilidade e rotas públicas são mantidos em um único ponto: a lista de unidades do `index.html` na raiz.

## 1. Preparar a pasta

Crie a nova pasta sem alterar as apresentações já publicadas:

```text
unidade-3/
├── index.html
├── css/
│   └── custom.css
├── js/
│   └── slides.js
├── README.md
└── REFERENCIAS.md
```

Os arquivos mínimos são `index.html` e todos os recursos locais referenciados por ele. Preserve os caminhos relativos e as dependências recebidas com a apresentação.

Para oferecer o retorno ao catálogo, siga a mesma integração externa das unidades existentes: carregue `../assets/unit-shell.css` depois dos estilos da apresentação e adicione, antes do elemento `.reveal`, a barra com uma única âncora `href="../"`. Não coloque navegação dentro de `.reveal .slides` e não edite apresentações anteriores.

## 2. Adicionar um item ao catálogo

Edite somente a lista `.catalog-list` do `index.html` raiz e acrescente um item na ordem pedagógica. Exemplo:

```html
<li>
  <a class="catalog-card" href="./unidade-3/" aria-label="Abrir Unidade 3 — Título da unidade">
    <span class="catalog-unit">Unidade 3</span>
    <span class="catalog-title">Título da unidade</span>
    <span class="catalog-action">Abrir apresentação <span aria-hidden="true">→</span></span>
  </a>
</li>
```

Não adicione cartões para unidades sem arquivos publicados. Não crie registro duplicado em CSS, JavaScript ou nas unidades existentes.

## 3. Validar em servidor local

Na raiz do repositório:

```bash
python3 -m http.server 8000
```

Abra `http://localhost:8000/`, acione o novo cartão e confirme que o HTML, o CSS, o JavaScript e demais recursos próprios não retornam 404. Teste também o retorno “Todas as unidades”, a navegação por teclado, um fragmento Reveal válido e `?print-pdf`.

## 4. Validar o subcaminho do GitHub Pages

Encerre o servidor anterior. No diretório pai do repositório, execute:

```bash
python3 -m http.server 8000
```

Acesse:

```text
http://localhost:8000/ml-ia-unimar-2026/
http://localhost:8000/ml-ia-unimar-2026/unidade-3/
```

Repita a verificação dos recursos próprios e confirme no painel de rede do navegador que nenhum deles retorna 404. Não use `file://` como evidência de funcionamento sob subcaminho.

## 5. Conferir antes de publicar

- a nova rota segue `unidade-N/` e usa links relativos;
- o catálogo contém um único item novo e nenhuma unidade indisponível;
- nenhuma apresentação anterior foi editada;
- barra, slides, fullscreen e impressão funcionam sem sobreposição;
- `.nojekyll` continua na raiz;
- a publicação continua configurada como branch `main` e pasta `/ (root)`.

O verificador `scripts/verify-presentation-integrity.py` protege as linhas de base das Unidades 1 e 2. Uma unidade futura não precisa alterar esse script para aparecer no catálogo.
