# Aquarium Resume

Личный сайт-портфолио на Django в стиле aquarium / glassmorphism / deep blue tech.

## Стек

- Python
- Django
- WhiteNoise
- SQLite
- Django Templates
- CSS

## Структура

```text
aquarium-resume/
├─ config/
├─ core/
│  ├─ static/css/style.css
│  ├─ templates/
│  ├─ urls.py
│  └─ views.py
├─ db.sqlite3
├─ manage.py
└─ requirements.txt
```

## Запуск

1. Создать и активировать виртуальное окружение.
2. Установить зависимости:

```bash
pip install -r requirements.txt
```

3. Создать `.env` на основе `.env.example`.

4. Применить миграции:

```bash
python manage.py migrate
```

5. Запустить сервер:

```bash
python manage.py runserver
```

6. Открыть в браузере:

```text
http://127.0.0.1:8000/
```

## Маршруты

- `/`
- `/projects/`
- `/research/`
- `/presentations/`
- `/youtube/`
- `/employers/`

## Что заменить под себя

- Ссылки `github.com/yourusername`
- Ссылки `t.me/yourusername`
- `kirill@example.com`
- PDF и Google Slides ссылки в шаблонах
- YouTube iframe на свой `video_id`
- `SECRET_KEY`, `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS` перед деплоем

## Переменные окружения

Основные переменные:

```env
SECRET_KEY=change-me
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
CSRF_TRUSTED_ORIGINS=http://127.0.0.1:8000,http://localhost:8000
DATABASE_URL=sqlite:///db.sqlite3
```

Для production:

- `DEBUG=False`
- `SECRET_KEY` только из env
- `ALLOWED_HOSTS` должен содержать домен Render
- `CSRF_TRUSTED_ORIGINS` должен содержать `https://<your-app>.onrender.com`
- можно использовать Render PostgreSQL через `DATABASE_URL`

## Render

В проект добавлен [render.yaml](/home/nande/aquarium-resume/render.yaml) для деплоя на Render.

Что важно:

- build command ставит зависимости, применяет миграции и собирает статику
- start command запускает `gunicorn`
- статика обслуживается через WhiteNoise
- для продакшна `SECRET_KEY` берётся из env, `DEBUG=False`

Если будешь деплоить на домен вида `https://aquarium-resume.onrender.com`, добавь:

```env
ALLOWED_HOSTS=aquarium-resume.onrender.com
CSRF_TRUSTED_ORIGINS=https://aquarium-resume.onrender.com
```

## Проверка

```bash
python manage.py check
```
