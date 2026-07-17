# taskctl — Task Tracker with Django REST Framework

A developer-themed Kanban task tracker. Tasks show up like git commits, complete
with an auto-generated hash. Built with Django REST Framework on the backend and
a plain HTML/CSS/JS frontend that talks to it over a REST API.

## Project structure

```
taskctl_backend/
├── manage.py
├── requirements.txt
├── db.sqlite3              (created after migrate)
├── taskctl_backend/         # Django project settings
│   ├── settings.py
│   └── urls.py
├── tasks/                   # The main app
│   ├── models.py            # Task model
│   ├── serializers.py       # Converts Task <-> JSON
│   ├── views.py             # ModelViewSet = full CRUD
│   ├── urls.py               # /api/tasks/ routes
│   └── admin.py              # Django admin registration
└── frontend/
    └── index.html            # The UI — talks to the API via fetch()
```

## How to run it locally

1. **Install dependencies** (Python 3.10+ recommended):
   ```bash
   pip install -r requirements.txt
   ```

2. **Apply migrations** (creates the SQLite database):
   ```bash
   python manage.py migrate
   ```

3. **(Optional) Create an admin user** to use the Django admin panel:
   ```bash
   python manage.py createsuperuser
   ```

4. **Start the server**:
   ```bash
   python manage.py runserver 8000
   ```

5. **Open the frontend**: just open `frontend/index.html` directly in your
   browser (double-click it, or use the "Live Server" extension in VS Code).
   It will automatically connect to `http://127.0.0.1:8000/api`.

6. **(Optional) Check the admin panel**: visit `http://127.0.0.1:8000/admin/`
   and log in with the superuser you created.

## API Endpoints

| Method | Endpoint              | What it does              |
|--------|------------------------|----------------------------|
| GET    | `/api/tasks/`          | List all tasks             |
| POST   | `/api/tasks/`          | Create a new task           |
| GET    | `/api/tasks/<id>/`     | Get one task                |
| PATCH  | `/api/tasks/<id>/`     | Update part of a task (e.g. status) |
| DELETE | `/api/tasks/<id>/`     | Delete a task                |

## Notes for pushing this to GitHub

- Add a `.gitignore` with at least: `__pycache__/`, `*.pyc`, `db.sqlite3`, `.venv/`
- Don't commit `SECRET_KEY` as-is for a real deployment — move it to an
  environment variable.
- `CORS_ALLOW_ALL_ORIGINS = True` is fine for local development, but for a
  real deployment restrict it to your actual frontend domain using
  `CORS_ALLOWED_ORIGINS`.

## Possible next steps

- Add user accounts so each person has their own task board (Django's
  built-in auth + DRF token/session authentication)
- Deploy the backend (Render/Railway free tier) and the frontend (GitHub Pages)
  so it's live and linkable on your resume
- Add due dates and reminders
