[![Coverage Status](https://coveralls.io/repos/github/marcuxyz/spacedevs/badge.svg?branch=master)](https://coveralls.io/github/marcuxyz/spacedevs?branch=master) ![GitHub](https://img.shields.io/github/license/marcuxyz/spacedevs) ![GitHub top language](https://img.shields.io/github/languages/top/marcuxyz/spacedevs)

# Sobre
Este projeto corresponde ao site oficial da **Spacedevs**. Chamamos ele de Dark Hole, o que combina muito com a nossa logo marca criada pela artista/designer [@karlamagueta](https://github.com/karlamagueta). Este projeto foi feito em Python utilizando o micro-framework [Flask](https://palletsprojects.com/p/flask/).

## Começando
Para começar, você poderia fazer um clone do projeto:

```bash
git clone git@github.com:marcuxyz/spacedevs.git
```

Você pode rodar de **dois jeitos**. O primeiro seria usando Docker, mas para isso será necessário instalar o docker & docker-compose no seu pc. E quando os mesmos estiverem instalados você deve rodar o comando:

```bash
docker-compose up -d
```

Uma outra forma de rodar, é, **somente usando Python**. Para isso, não esqueça de setar a variável de ambiente **FLASK_ENV** como development e a **SECRET_KEY**:

```bash
export FLASK_ENV=development
export SECRET_KEY=secret
```

E agora precisamos configurar o banco de dados para receber as nossas migrações :)

## Configurando Banco de Dados
Antes de você rodar o comando `flask run` para já subir o servidor, você vai ter que acessar o `Shell do Flask` para criar as tabelas no banco **LOCAL/SQLITE**.

```bash
flask shell
```

Dentro do flask shell, execute cada linha por vez.

```python
from app.models import *
from app import db

db.create_all()
```

Agora saia do shell do flask e tente rodar o comando `flask run`

## Página adminstrativa
Se você gostaria de acessar a página administrativa, para criar cursos ou até mesmo criar outros tipos de dados, você deve configurar a variável de ambiente `ADMIN_URL`.

```bash
export ADMIN_URL="/admin"
```

Agora para acessar a página administrativa, você deve ta logado! Caso não esteja logado acesse a rota: https://localhost/login e logue com uma conta. Caso você ainda não tenha criado uma conta, pode fazer isso usando o ` flask shell`.

```bash
flask shell
```

### Criando usuário Marcus Pereira

```python
from app.models import User
from app import db
from werkzeug.security import generate_password_hash

user = User(
    first_name="Marcus",
    last_name="Pereira",
    email="contato@meuprovedor.com",
    password=generate_password_hash("12345"),
    is_admin=True,
)

db.session.add(user)
db.session.commit()
```

Volte para a página de `login` e tente acessar agora usando as credênciais.

## Rodando os testes
Para rodar os testes execute o comando:

```bash
make test
```

PS: uma outra forma de não precisar exportar as variáveis de ambiente uma por você é; Você pode criar um arquivo chamado .secrets.toml e colocar as variáveis de ambiente lá. Veja:

```toml
# .secrets.toml
[default]
ADMIN_URL="/admin"
SECRET_KEY="secret"
```