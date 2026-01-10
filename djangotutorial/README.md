# Django Tutorial Project (djangotutorial)

This small Django project contains a simple `polls` app and a minimal project-level UI with authentication.

The repository implements the following features:

- Static files
  - `polls/static/polls/style.css` is used for simple page styling and is loaded via the `{% static %}` template tag.
- Project root index
  - The root URL `/` lists installed (non-Django) apps and links to `/<app>/` (e.g. `/polls/`).
- Authentication
  - Register (project-level view): `/accounts/register/` — creates a user with Django's `UserCreationForm` and logs them in.
  - Login: `/accounts/login/` — uses Django's built-in auth views with a custom template.
  - Logout: logout is implemented as a POST (form) to the logout view to avoid GET/405 issues.
  - After login the site root displays the username in the header.
- Access control
  - `polls` views (index/detail/results and vote) are protected so unauthenticated users are redirected to the login page.
  - `LOGIN_URL` and `LOGIN_REDIRECT_URL` are set in `mysite/settings.py`.

Files of interest
-----------------

- `manage.py` — Django management script.
- `mysite/settings.py` — project settings (including `STATIC_URL`, `LOGIN_URL`, and `TEMPLATES['DIRS']`).
- `mysite/urls.py` — project URL routing (`/`, `/polls/`, `accounts/`, `admin/`).
- `mysite/views.py` — contains the root index and a register view.
- `mysite/templates/base.html` — shared base template with header and auth links.
- `mysite/templates/index.html` — project root index (extends `base.html`).
- `mysite/templates/registration/` — custom login/register/logged_out templates.
- `polls/` — the example app (models, views, templates in `polls/templates/polls/`).

How to run (development)
------------------------

1. Create and activate a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install Django:

```bash
python3 -m pip install Django
```

3. Run migrations and create a superuser if you want the admin site:

```bash
cd /home/hariom/django/djangotutorial <Your directory where it is cloned>
python3 manage.py migrate
python3 manage.py createsuperuser
```

4. Run the development server:

```bash
python3 manage.py runserver
```

5. Open the site in your browser:

- Project root / index:  http://127.0.0.1:8000/
- Polls app:           http://127.0.0.1:8000/polls/
- Login:                http://127.0.0.1:8000/accounts/login/
- Register:             http://127.0.0.1:8000/accounts/register/
- Admin:                http://127.0.0.1:8000/admin/

Notes and troubleshooting
-------------------------

- Template not found (TemplateDoesNotExist): ensure `mysite/settings.py` contains the project templates directory in `TEMPLATES['DIRS']` — this project already sets `BASE_DIR / 'mysite' / 'templates'`.
- Static files not loading in development: ensure `DEBUG = True` in `mysite/settings.py`. Django's dev server serves app static files when `django.contrib.staticfiles` is in `INSTALLED_APPS` (this project includes it).
- If you see `405 Method Not Allowed` on logout: make sure you submit logout as a POST. The templates include an inline form that submits POST with CSRF token.
- If links to `/<app>/` 404: the project index lists all non-django apps by package name and assumes they are mounted at `/<app>/`. If an app is not mounted at that path it will 404 — you can either mount it explicitly in `mysite/urls.py` or improve the index view to test route resolution.


