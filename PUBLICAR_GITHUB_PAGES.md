# Publicar no GitHub Pages

Este projeto é uma apresentação estática em Reveal.js. Não precisa de build, Node.js ou backend para ser publicada no GitHub Pages.

## Estrutura esperada

Mantenha estes arquivos na raiz do repositório:

```text
index.html
css/custom.css
js/slides.js
REFERENCIAS.md
README.md
.nojekyll
.gitignore
```

O arquivo `.nojekyll` evita que o GitHub Pages processe o site com Jekyll. Isso reduz o risco de alterações automáticas nos arquivos estáticos.

## 1. Criar o repositório no GitHub

1. Acesse https://github.com/new.
2. Defina o nome do repositório, por exemplo:

```text
ml-unidade1-fundamentos-teoricos
```

3. Escolha `Public` se quiser usar GitHub Pages gratuitamente em um repositório público.
4. Não é necessário marcar a opção de criar `README`, `.gitignore` ou licença, porque os arquivos já existem localmente.
5. Clique em `Create repository`.

## 2. Enviar os arquivos locais

No terminal, dentro desta pasta do projeto, execute:

```bash
git init
git add .
git commit -m "Publica apresentacao da unidade 1"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/ml-unidade1-fundamentos-teoricos.git
git push -u origin main
```

Troque `SEU_USUARIO` pelo seu usuário do GitHub. Se escolher outro nome para o repositório, ajuste também a URL.

## 3. Ativar o GitHub Pages

1. Abra o repositório no GitHub.
2. Acesse `Settings`.
3. No menu lateral, clique em `Pages`.
4. Em `Build and deployment`, escolha:

```text
Source: Deploy from a branch
Branch: main
Folder: / (root)
```

5. Clique em `Save`.

Depois de alguns minutos, o GitHub mostrará a URL publicada. O endereço normalmente fica neste formato:

```text
https://SEU_USUARIO.github.io/ml-unidade1-fundamentos-teoricos/
```

## 4. Conferir a publicação

Abra a URL do GitHub Pages e teste:

- navegação dos slides pelas setas do teclado;
- progresso e numeração dos slides;
- fórmulas matemáticas;
- blocos de código com destaque;
- quiz interativo;
- busca, zoom e notas do apresentador.

## 5. Atualizar depois de publicar

Sempre que alterar o conteúdo, envie uma nova versão:

```bash
git add .
git commit -m "Atualiza conteudo da apresentacao"
git push
```

O GitHub Pages republicará automaticamente a versão nova.

## 6. Exportar para PDF após publicar

Depois que o site estiver no ar, abra:

```text
https://SEU_USUARIO.github.io/ml-unidade1-fundamentos-teoricos/?print-pdf
```

Use a impressão do navegador e salve como PDF em modo paisagem, com gráficos de fundo habilitados.

## Observações

- A apresentação carrega Reveal.js, KaTeX e plugins pela CDN jsDelivr.
- Por isso, a versão publicada precisa de acesso à internet para carregar essas bibliotecas externas.
- Os arquivos próprios do projeto usam caminhos relativos, então funcionam tanto localmente quanto no GitHub Pages.
