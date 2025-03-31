# Sistema de Gestão de Restaurantes

Este é um sistema de gestão de restaurantes e pedidos, desenvolvido em Django. Ele permite que administradores criem e gerenciem restaurantes, enquanto os restaurantes podem gerenciar seus pedidos.

## Como Executar o Programa

Siga os passos abaixo para configurar e executar o projeto:

### 1. Verificar se está no DevContainer
Certifique-se de que está dentro do DevContainer no Visual Studio Code. O DevContainer é configurado automaticamente ao abrir o projeto no VS Code, caso você tenha o Docker instalado e configurado.

- Se o DevContainer não iniciar automaticamente, clique no canto inferior esquerdo do VS Code e selecione **"Reabrir no DevContainer"**.

### 2. Iniciar o Projeto
No terminal, execute o seguinte comando para iniciar o projeto, aplicar as migrações e configurar o ambiente:

```bash
make compose.setup
```

### 3. Criar um Superusuário
Abra um novo terminal e execute o comando abaixo para criar um superusuário para acessar o painel administrativo:

```bash
make compose.createsuperuser
```

Siga as instruções no terminal para definir o nome de usuário, e-mail e senha do superusuário.

### 4. Acessar o Sistema
Após os passos acima, o sistema estará disponível em http://127.0.0.1:8000. Use as credenciais do superusuário para acessar o painel administrativo.

## Dependências do Projeto
As dependências do projeto estão listadas no arquivo pyproject.toml. Aqui estão as principais:

- Django: Framework web para desenvolvimento rápido e limpo.
- Uvicorn: Servidor ASGI para rodar o projeto.
- Psycopg2-binary: Driver para conexão com o banco de dados PostgreSQL.
- Whitenoise: Para servir arquivos estáticos.

Certifique-se de que o Docker e o Docker Compose estão instalados no seu sistema para executar o projeto.

## Funcionalidades
### Para Administradores:
- Fazer login como administrador.
- Criar e apagar restaurantes.
- Visualizar os restaurantes criados e suas encomendas.

### Para Restaurantes:
- Fazer login como restaurante.
- Visualizar suas encomendas.
- Criar novas encomendas (funcionalidade pendente).

## Comandos Úteis no Makefile
- `make compose.setup`: Inicia o projeto, aplica as migrações e configura o ambiente.
- `make compose.start`: Inicia os contêineres Docker.
- `make compose.migrate`: Aplica as migrações do banco de dados.
- `make compose.createsuperuser`: Cria um superusuário para o Django Admin.
- `make compose.collectstatic`: Coleta os arquivos estáticos.
