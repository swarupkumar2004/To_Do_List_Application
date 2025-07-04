# To_Do_List_Application
📝 To-Do List Application (Django + Channels + PostgreSQL + Redis)

A real-time to-do list web application with user authentication, task filtering, and REST API support.

---

## 🚀 Features

- ✅ User Registration & Login
- ✅ Add, Complete, Delete Tasks
- ✅ Filter by Priority, Category, Completion
- ✅ Real-time updates using Django Channels + Redis
- ✅ REST API support (via Django REST Framework)
- ✅ PostgreSQL database backend

---

## 🛠️ Tech Stack

- **Backend**: Django 5.2.4, Django REST Framework
- **WebSockets**: Django Channels, Redis
- **Database**: PostgreSQL
- **Frontend**: Django Templates (HTML + CSS)
- **API Testing**: Postman / cURL

---

## 📦 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
````

**requirements.txt**

```text
Django>=5.2
djangorestframework
channels
channels_redis
psycopg2
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/your-username/todo-list-django.git
cd todo-list-django
```

### 2. Setup PostgreSQL

Create a database named `todo_db` and set credentials in `todo_project/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'todo_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 3. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser

```bash
python manage.py createsuperuser
```

### 5. Run Redis (in separate terminal)

```bash
redis-server
```

> ✅ Redis must be running for WebSocket features to work.

### 6. Run Server

```bash
python manage.py runserver
```

---

## 🔌 WebSocket Support

* Uses Channels + Redis
* WebSocket route: `ws://localhost:8000/ws/tasks/`

---

## 🔐 Authentication

* Login: `/accounts/login/`
* Logout: `/accounts/logout/` (redirects to `logout_success`)
* Logout success page: `/accounts/logout_success/`

---

## 📬 API Endpoints

* List/Create Tasks: `GET/POST /tasks-api/`
* Retrieve/Update/Delete Task: `GET/PUT/DELETE /tasks-api/<id>/`

Authentication is required for all API routes.

---

## 📁 Project Structure

```
todo_project/
├── todo_app/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── consumers.py
│   ├── templates/
│   │   └── registration/
│   │   └── task_list.html
│   ├── routing.py
├── todo_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
├── manage.py
```

---

## 🧪 Testing

* Test the app on browser: [http://127.0.0.1:8000/tasks/](http://127.0.0.1:8000/tasks/)
* Use Postman to test API endpoints with token/session authentication.

---

## 📜 License

This project is open-source and free to use.

---

## ✨ Author

**Swarup Kumar** — *Feel free to reach out for contributions or feedback!*

```

---

Let me know if you want:
- A version with Markdown badges (pip, Django version, etc.)
- Deployment guide (Heroku or PythonAnywhere)
- Docker support setup

Would you also like me to generate a sample `README.pdf` version from this?
```
