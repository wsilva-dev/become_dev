# Guia de estilos do mural

O CSS compartilhado fica em `board/static/board/css/styles.css`. O template
`board/base.html` carrega esse arquivo com a tag `static` do Django e define idioma,
viewport e fonte. Não é necessário adicionar dependências ou configurar outro diretório estático.

## Criar uma página

```django
{% extends "board/base.html" %}
{% block title %}Minha página | Mural{% endblock %}
{% block content %}
<main class="page-shell">
    <h1 class="page-title">Minha página</h1>
    <section class="surface message-card">Conteúdo</section>
</main>
{% endblock %}
```

## Paleta e medidas

As variáveis em `:root` centralizam fundo lilás (`--color-background`), superfícies
brancas (`--color-surface`), botão violeta (`--color-accent`), texto e foco roxos
(`--color-accent-strong`), campos cinza e bordas. As cores dos rótulos e placeholders
são mais escuras que a referência para facilitar a leitura. Ajuste os tokens para
alterar todas as páginas que usam a folha. `--page-width` limita a largura do mural.

## Classes disponíveis

| Classe | Aplicação |
| --- | --- |
| `page-shell` | Contêiner central com largura máxima e margem lateral responsiva. |
| `page-header`, `page-nav` | Cabeçalho e navegação; empilham no celular. |
| `eyebrow`, `page-title`, `page-description` | Texto auxiliar, título e descrição. |
| `surface` | Fundo branco e cantos arredondados; combine com classe de espaçamento. |
| `button` | Ação principal em `<button>` ou `<a>`. Use `type="submit"` para enviar. |
| `text-link` | Link textual com sublinhado e cor de destaque. |
| `form-page`, `message-form` | Centralização e espaçamento do formulário da referência. |
| `form-field`, `form-label` | Agrupamento e rótulo de um campo. |
| `form-control` | Aparência compartilhada de `<input>` e `<textarea>`. |
| `form-control--message` | Modificador para textarea alto, redimensionável na vertical. |
| `form-actions` | Alinha a ação à direita; botão ocupa a largura no celular. |
| `form-alert` | Erro de validação; use também `role="alert"`. |
| `form-back` | Centraliza a ação de retorno abaixo do cartão. Combine com `button button--small`. |
| `message-grid` | Grade de recados: 1 coluna abaixo de 960px, 3 a partir de 960px. |
| `message-card` | Cartão com espaçamento, data no rodapé e quebra de textos longos. |
| `message-author`, `message-content`, `message-date` | Autor, texto com quebras de linha e data. |
| `empty-state` | Mensagem para coleção vazia; ocupa toda a grade. |
| `visually-hidden` | Oculta visualmente sem remover o conteúdo de leitores de tela. |

## Formulários e acessibilidade

```html
<div class="form-field">
    <label class="form-label" for="campo">Rótulo</label>
    <input class="form-control" id="campo" name="campo" required>
</div>
```

Mantenha `for` e `id` iguais; `name` identifica o dado enviado. Dentro de formulários
POST, mantenha `{% csrf_token %}`. Preserve os valores retornados pela view quando
houver erro. Os estilos não substituem a validação do servidor. Há foco visível para
teclado; placeholders complementam os rótulos e não devem substituí-los.

## Conferência visual

Teste `/novo/` e `/` em 390px e 1280px de largura. No celular, confira que os campos
não ultrapassam a tela e os recados têm uma coluna. No desktop, confira três colunas.
Teste também o mural vazio, mensagens longas, envio válido e erro de validação.

## Formulário adaptado à altura da janela

`form-page` centraliza verticalmente o conjunto cartão + botão de retorno, com a mesma
área livre acima e abaixo. Usa `height: 100dvh` (altura visível dinâmica) e padding
vertical simétrico de 3,5dvh. O conjunto ocupa 93% da altura visível; o cartão e
a área de texto crescem para preencher o espaço disponível. A largura máxima é 600px.
O navegador usa `vh` como alternativa se não suportar `dvh`.

Fontes, espaçamentos e botão de envio variam com a altura da janela por `clamp()`.
`form-control--message` ajusta a altura entre 100px e 300px, reservando espaço para
os demais elementos. `button--small` cria uma ação de 44px de altura mínima, menor
que Enviar, preservando fundo, formato arredondado e foco do botão padrão.

Em janelas muito baixas, com teclado virtual aberto, mensagens de erro extensas ou
textarea ampliado manualmente, o conteúdo pode rolar naturalmente: os elementos mantêm sua altura mínima, sem corte de campos ou botões. As margens simétricas envolvem o conjunto
completo, incluindo o botão de retorno. Teste também em 1366x768, 1920x1080,
390x844 e modo paisagem baixo.