# Aquarium Portfolio

Персональный сайт-портфолио на Django с акцентом на backend-подачу, структурированный контент и визуальный стиль в эстетике aquarium / glassmorphism / deep blue.

Проект объединяет несколько типов материалов в одном сайте: проекты, исследовательские работы, презентации, видео и отдельную страницу для работодателей. Контент поддерживает две локали (`ru` и `en`) и управляется через Django Admin.

## Возможности

- многостраничное портфолио на Django
- поддержка русского и английского языков
- управление контентом через Django Admin
- отдельные разделы для проектов, исследований, презентаций и видео
- страница для работодателей с краткой профессиональной подачей
- кастомные страницы ошибок `404` и `500`
- готовая конфигурация для деплоя на Render
- раздача статики через WhiteNoise
- поддержка SQLite локально и PostgreSQL в продакшне через `DATABASE_URL`

## Стек

- Python 3
- Django 5
- SQLite
- PostgreSQL
- Django Templates
- WhiteNoise
- Gunicorn
- dj-database-url
- CSS

## Структура проекта

```text
aquarium-portfolio/
├─ config/
├─ core/
│  ├─ admin.py
│  ├─ localization.py
│  ├─ models.py
│  ├─ templates/
│  ├─ static/
│  ├─ urls.py
│  └─ views.py
├─ db.sqlite3
├─ manage.py
├─ requirements.txt
└─ render.yaml
```
###Данная версия README сделана как временный костыль и полность сгенерена ЛЛМ
