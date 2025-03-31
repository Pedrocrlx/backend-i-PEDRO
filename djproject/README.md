# 🍴 Restaurant Management System

This is a restaurant and order management system developed in Django. It allows an administrator to create and manage restaurants, products, and orders, while restaurants can manage their own orders.

## 🚀 How to Run the Program

Follow the steps below to set up and run the project:

### 1. Verify You Are in the DevContainer 🐳
Make sure you are inside the DevContainer in Visual Studio Code. The DevContainer is automatically configured when you open the project in VS Code, provided you have Docker installed and set up.

- If the DevContainer does not start automatically, click on the bottom-left corner of VS Code and select **"Reopen in DevContainer"**.

### 2. Start the Project ▶️
In the terminal, run the following command to start the project and set up the environment:

```bash
make compose.setup
```

Then, apply the migrations:

```bash
make compose.migrate
```

### 3. Create a Superuser and `.env` File 🔑
Open a new terminal and run the command below to create a superuser to access the admin panel:

```bash
make compose.createsuperuser
```

Follow the instructions in the terminal to set the username, email, and password for the superuser.

After that, create a file named `.env` in the root of the project.

This file should have the following structure:

#### 🌐 `.env` Structure
```env
POSTGRES_HOST = "database"
POSTGRES_USERNAME = "postgres"
POSTGRES_PASSWORD = "qwerty"
POSTGRES_PORT = "5432"
POSTGRES_DB = "dj_db"
```

### 4. Access the System 🌍
After completing the steps above, the system will be available at [http://localhost:8000](http://localhost:8000). Use the superuser credentials to access the admin panel.

## 📦 Project Dependencies
The project dependencies are listed in the `pyproject.toml` file. Here are the main ones:

- **Django**: Web framework for rapid and clean development.
- **Uvicorn**: ASGI server to run the project.
- **Psycopg2-binary**: Driver for connecting to the PostgreSQL database.
- **Whitenoise**: To serve static files.

Make sure Docker is installed on your system to run the project.

## ✨ Features
### For Administrators:
- Log in as an administrator (superuser login).
- Create restaurants.
- Create products.
- View created restaurants and their orders.

### For Restaurants:
- Log in as a restaurant (only the admin creates restaurant logins, as each restaurant will have its own manager responsible for orders).
- View their orders.
- Create new orders.

## 🛠️ Useful Makefile Commands
- `make compose.setup`: Starts the project, applies migrations, and sets up the environment.
- `make compose.start`: Starts the Docker containers.
- `make compose.migrate`: Applies database migrations.
- `make compose.createsuperuser`: Creates a superuser for the Django Admin.
- `make compose.collectstatic`: Collects static files.

