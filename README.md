# Django Task Management Application

This is a Django-based task management application that allows users to create, update, delete, and search tasks. Users must be authenticated to manage their tasks.

## Features

- User authentication (login, logout, registration)
- Create, update, and delete tasks
- View task details
- Search tasks with instant results
- Mark tasks as done or pending

## Requirements

- Python 3.x
- Django 3.x or higher

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/task-management-app.git
    cd task-management-app
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Open your browser and navigate to `http://127.0.0.1:8000/` to access the application.

## Usage

### User Authentication

- Navigate to `/account/login/` to log in.
- Navigate to `/account/register/` to create a new account.
- Navigate to `/account/logout/` to log out.

### Task Management

- Once logged in, you can create a new task by navigating to `/task-create/`.
- You can view details of a task by clicking on it from the task list.
- To update a task, navigate to `/task-update/<task_id>/`.
- To delete a task, navigate to `/task-delete/<task_id>/`.

### Instant Search

- Use the search bar at the top of the task list to filter tasks by their title instantly.

## Project Structure

```plaintext
task-management-app/
│
├── base/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── templates/
│   │   └── base/
│   │       ├── login.html
│   │       ├── register.html
│   │       └── tasks.html
│   ├── urls.py
│   ├── views.py
│   └── ...
│
├── task_management_app/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
│
├── manage.py
├── requirements.txt
└── README.md
