# Mural de Recados

Projeto de estudo desenvolvido com Python e Django.

Permite consultar recados e publicar novas mensagens com autor e
conteúdo. Os dados são armazenados em SQLite.

## Funcionalidades

- Listagem de recados do mais recente para o mais antigo.
- Publicação de recados por formulário.
- Validação de campos obrigatórios e limite do autor.
- Página Sobre.
- Administração pelo Django Admin.
- Interface responsiva para desktop e celular.

## Tecnologias

- Python
- Django
- SQLite
- HTML e CSS
- Git e GitHub

## Instalação local

As instruções abaixo usam Windows e PowerShell. O projeto foi desenvolvido com
Python 3.13; as versões dos pacotes estão registradas em
`message_board/requirements.txt`.

### 1. Pré-requisitos

Instale Python e Git e confira se estão disponíveis no terminal:

```powershell
python --version
git --version
```

### 2. Obter o código

Em uma pasta onde deseja guardar o projeto:

```powershell
git clone https://github.com/wsilva-dev/become_dev.git
cd become_dev
cd message_board
```

O clone copia o código e o histórico do repositório. Os próximos comandos devem
ser executados dentro de `message_board`, onde está o arquivo `manage.py`.
Se você já possui o projeto no computador, entre nessa pasta e continue a partir
da etapa necessária; não é preciso cloná-lo novamente.

### 3. Criar o ambiente virtual e instalar as dependências

Em uma instalação nova:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

A `.venv` isola os pacotes deste projeto. `python -m pip` executa o instalador do
Python ativo, e `-r requirements.txt` instala as versões registradas no arquivo.
O indicador `(.venv)` no prompt normalmente confirma a ativação.

Se o ambiente já existe, basta ativá-lo. Para conferir o interpretador selecionado:

```powershell
python -c "import sys; print(sys.executable)"
```

O caminho deve terminar em `.venv\Scripts\python.exe`. Se o PowerShell bloquear o
script de ativação, é possível usar o Python do ambiente diretamente, sem mudar a
política de execução do sistema:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Nesse caso, substitua `python` por `.\.venv\Scripts\python.exe` nos comandos
seguintes.

## Configuração do ambiente

### 4. Criar o arquivo .env

Crie um arquivo chamado `.env` dentro de `message_board`, ao lado de `manage.py`.
Ele deve conter uma variável com uma chave própria:

```dotenv
DJANGO_SECRET_KEY=SUBSTITUA_POR_UMA_CHAVE_GERADA
```

O valor acima é apenas um marcador. Para gerar uma chave, execute:

```powershell
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

Copie o resultado para o lugar de `SUBSTITUA_POR_UMA_CHAVE_GERADA`. Não acrescente
espaços ao nome da variável. Se você já tem um `.env` funcionando, preserve seu
conteúdo; não precisa gerar outra chave a cada execução.

O projeto usa `python-dotenv` para carregar esse arquivo a partir de `BASE_DIR`,
e lê a chave com `os.environ["DJANGO_SECRET_KEY"]`. Se a variável não existir, a
inicialização falhará. A chave é uma configuração privada do Django, diferente
da senha do usuário administrativo.

O `.env` está no `.gitignore` e não deve ser enviado ao GitHub. Para conferir,
ainda dentro de `message_board`:

```powershell
git check-ignore .env
git ls-files -- .env
```

O primeiro comando deve identificar `.env` como ignorado; o segundo não deve
listar o arquivo. Uma regra no `.gitignore` não remove arquivos que já eram
rastreados.

### 5. Preparar o banco de dados

```powershell
python manage.py migrate
python manage.py check
```

`migrate` cria o banco SQLite e aplica as migrações, preparando as tabelas do
Django e do app `board`. `check` verifica problemas de configuração e models.
Não é necessário executar `makemigrations` apenas para instalar o projeto:
as migrações existentes já estão no repositório.

O arquivo `db.sqlite3` é local e não é versionado. Uma instalação nova começa
sem os recados de outros computadores. As migrações reproduzem a estrutura das
tabelas, não os registros locais.

## Execução local

### 6. Iniciar o servidor

Com o ambiente ativo e o terminal na pasta `message_board`:

```powershell
python manage.py runserver
```

Acesse:

| Página | Endereço |
| --- | --- |
| Mural | [http://127.0.0.1:8000/](http://127.0.0.1:8000/) |
| Novo recado | [http://127.0.0.1:8000/novo/](http://127.0.0.1:8000/novo/) |
| Sobre | [http://127.0.0.1:8000/sobre/](http://127.0.0.1:8000/sobre/) |
| Administração | [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) |

Use `Ctrl+C` no terminal para parar o servidor. `runserver` é destinado ao
desenvolvimento local. A configuração atual usa `DEBUG=True`; o deploy e os
ajustes de produção ainda serão realizados.

### 7. Acesso administrativo opcional

Para criar uma conta administrativa, execute antes de iniciar o servidor, ou
em outro terminal com o mesmo ambiente ativo:

```powershell
python manage.py createsuperuser
```

Siga as instruções do terminal e use a conta em `/admin/`. Durante a digitação,
a senha pode não aparecer na tela. Esse usuário é armazenado no banco local;
um clone novo não inclui as contas administrativas de outro computador.
Não é necessário criar um superusuário para publicar recados pelo formulário.

### Retomar em outra sessão

Não é preciso recriar o projeto, reinstalar os pacotes ou refazer o `.env` a cada
sessão. Entre na pasta do projeto, ative o ambiente e inicie o servidor:

```powershell
cd C:\Users\wjrad\Documents\become_dev\message_board
.\.venv\Scripts\Activate.ps1
python manage.py runserver
```

Adapte o caminho se você clonou em outro local. Execute `migrate` novamente
quando houver novas migrações; instale `requirements.txt` novamente quando as
dependências mudarem.

## Verificação rápida

- Publique um recado e confira o redirecionamento ao mural.
- Confira o recado no topo e o aumento do total em uma unidade.
- Atualize o mural: o registro deve permanecer sem duplicar nessa atualização.
- Envie autor ou conteúdo composto apenas por espaços: o formulário deve exibir
  um erro, preservar o outro campo e não criar um registro.
- Confira as páginas Sobre e Administração e o layout em desktop e celular.

Se uma alteração no CSS não aparecer, atualize com `Ctrl+F5`. Caso a pasta de
estáticos tenha sido criada com o servidor já em execução, reinicie-o. Para
conferir a descoberta da folha de estilos:

```powershell
python manage.py findstatic board/css/styles.css
```

O guia de classes e componentes visuais está em
[message_board/docs/estilos.md](message_board/docs/estilos.md).
