# Event Management System 🎉

## Description 📝
The Event Management System is an application designed to facilitate the creation, management, and monitoring of events. The app will be built using Python, integrating different frameworks: **Typer**, **FastAPI**, and **Django**.

## How to Run
poetry run python src/project_module/app.py "**NAME**" "**DATE**" "**LOCATION**" --description "epa ya"

## Key Features 🚀
1. **CLI (Command Line Interface) with Typer:**
   - ➕ **Add events** with name, date, location, and description.
   - 📋 **List all registered events**.
   - ✏️ **Update the details** of existing events.
   - ❌ **Delete specific events**.
   - 🗂️ **Generate summaries** of upcoming events.

2. **RESTful API with FastAPI:**
   - 🌐 **Endpoints** for:
     - 🔍 Retrieving the list of events.
     - 🆕 Creating new events.
     - ♻️ Updating existing events.
     - ✂️ Performing partial updates.
     - 🗑️ Deleting events.
   - 📜 **Automatically generated documentation** using OpenAPI (Swagger).

3. **SaaS Application with Django:**
   - 🗂️ **Models**:
     - 🗓️ Event: Name, description, date, location.
     - 👤 Guest: Name, email, RSVP status.
   - 🖊️ **Forms**:
     - Form for creating or editing events.
   - 👀 **Views**:
     - 📃 Event list.
     - 🔍 Event details.
     - 🆕 New event creation.
     - ✏️ Editing existing events.
   - 🔑 **Admin**:
     - Admin panel for managing events and guests.

## Technologies Used 🛠️
- **Programming Language**: Python 🐍
- **Frameworks**:
  - **Typer**: To create the command-line interface.
  - **FastAPI**: To build the RESTful API.
  - **Django**: For the SaaS web application.
- **Database**: SQLite (or another option like PostgreSQL, if preferred).
- **Additional Tools**:
  - Poetry for dependency management.

## Project Structure 🏗️
```plaintext
event-management-system/
├── cli/
│   ├── main.py          # Typer CLI with commands
├── api/
│   ├── main.py          # FastAPI application
├── saas/
│   ├── manage.py        # Django manage file
│   ├── events/
│   │   ├── models.py    # Event and Guest models
│   │   ├── views.py     # Views for events
│   │   ├── forms.py     # Forms for events
│   │   ├── admin.py     # Admin panel configurations
├── README.md            # Project documentation