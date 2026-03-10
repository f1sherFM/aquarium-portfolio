# Aquarium Portfolio

Backend-focused personal portfolio built with Django.

The project combines a portfolio website, presentation showcase, and employer-facing profile into a single multi-page application with RU/EN support, custom styling, and production-ready deployment on Render.

## Highlights

- Multi-page Django portfolio with dedicated sections for projects, presentations, and employers
- RU/EN localization with session-based language switching
- Backend-oriented content structure with project cards and curated portfolio materials
- Custom UI with aquarium / glassmorphism / deep blue visual direction
- Static asset delivery through WhiteNoise
- Local SQLite setup and PostgreSQL support in production via `DATABASE_URL`
- Ready-to-deploy Render configuration
- Core test coverage for the main user flows

## Tech Stack

- Python 3.13
- Django 5
- Django Templates
- SQLite
- PostgreSQL
- WhiteNoise
- Gunicorn
- dj-database-url
- psycopg

## Current Sections

- Home
- Projects
- Presentations
- Research
- YouTube
- For Employers

## Project Structure

```text
aquarium-portfolio/
|-- config/
|   |-- settings.py
|   |-- urls.py
|   |-- asgi.py
|   `-- wsgi.py
|-- core/
|   |-- migrations/
|   |-- static/
|   |-- templates/
|   |-- admin.py
|   |-- context_processors.py
|   |-- localization.py
|   |-- middleware.py
|   |-- models.py
|   |-- tests.py
|   |-- urls.py
|   `-- views.py
|-- manage.py
|-- render.yaml
|-- requirements.txt
`-- README.md
```

## Local Development

### 1. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a local `.env` file in the project root:

```env
DEBUG=True
SECRET_KEY=django-insecure-local-dev-key
ALLOWED_HOSTS=127.0.0.1,localhost,testserver
CSRF_TRUSTED_ORIGINS=http://127.0.0.1:8000,http://localhost:8000
```

### 4. Apply migrations

```powershell
python manage.py migrate
```

### 5. Run the development server

```powershell
python manage.py runserver
```

Open:

- `http://127.0.0.1:8000/`

## Running Tests

```powershell
python manage.py test core
```

The current test suite covers the main pages, language switching, active portfolio content, empty-state sections, and employer contacts.

## Environment Variables

Production configuration relies on environment variables:

- `DEBUG`
- `SECRET_KEY`
- `ALLOWED_HOSTS`
- `CSRF_TRUSTED_ORIGINS`
- `DATABASE_URL`

If `DATABASE_URL` is not provided, the project falls back to local SQLite.

## Deployment on Render

The repository already includes a Render service definition in [`render.yaml`](render.yaml).

Current build flow:

```text
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
```

Start command:

```text
gunicorn config.wsgi:application
```

## Notes

- Local development uses SQLite by default.
- Production is expected to use PostgreSQL through `DATABASE_URL`.
- Static files are served with WhiteNoise.
- Some portfolio sections are intentionally curated in code to control what is shown publicly.

## License

This project is intended as a personal portfolio repository.
