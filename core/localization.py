from __future__ import annotations

from copy import deepcopy
from typing import Any


SUPPORTED_LANGUAGES = ("ru", "en")
DEFAULT_LANGUAGE = "ru"


BASE_TRANSLATIONS: dict[str, dict[str, Any]] = {
    "ru": {
        "site": {
            "lang": "ru",
            "language_label": "Язык",
            "brand_name": "Kirill",
            "brand_role": "Backend Portfolio",
            "nav": {
                "home": "Главная",
                "projects": "Проекты",
                "research": "Работы",
                "presentations": "Презентации",
                "youtube": "YouTube",
                "employers": "Работодателям",
            },
            "footer_name": "Кирилл",
            "footer_role": "Junior Backend Developer · Python, Django, FastAPI",
            "links": {
                "github": "GitHub",
                "telegram": "Telegram",
                "email": "Email",
            },
            "contact": {
                "github_url": "https://github.com/yourusername",
                "telegram_url": "https://t.me/yourusername",
                "email": "kirill@example.com",
            },
            "error": {
                "back_home": "На главную",
                "to_projects": "К проектам",
            },
        },
        "pages": {
            "home": {
                "title": "Главная | Портфолио",
                "eyebrow": "Junior Backend Developer",
                "heading": "Кирилл. Python, Django, FastAPI.",
                "description": "Собираю аккуратные backend-проекты, изучаю архитектуру приложений и оформляю технические материалы так, чтобы их было удобно читать и обсуждать. Этот сайт объединяет код, исследования, презентации и публичные объяснения.",
                "buttons": {
                    "projects": "Проекты",
                    "employers": "Работодателям",
                },
                "focus_eyebrow": "Focus",
                "focus_heading": "Текущий стек и интересы",
                "focus_items": [
                    "Python, Django, FastAPI",
                    "REST API и backend-логика",
                    "Структура проектов и качество кода",
                    "Аналитические и учебные материалы",
                ],
                "metrics": [
                    {"value": "6", "label": "Разделов сайта"},
                    {"value": "3", "label": "Ключевых технологии"},
                    {"value": "1", "label": "Точка входа для работодателя"},
                ],
                "section": {
                    "eyebrow": "Navigation",
                    "heading": "Что есть на сайте",
                    "description": "Каждый раздел оформлен как отдельный слой портфолио: от практики разработки до материалов, которые показывают способ мышления.",
                },
                "cards": [
                    {
                        "tag": "Projects",
                        "title": "Проекты",
                        "description": "Pet-проекты, backend-сервисы и учебные разработки с упором на архитектуру, API и понятную структуру.",
                        "link_label": "Открыть раздел",
                        "link_url_name": "projects",
                    },
                    {
                        "tag": "Research",
                        "title": "Научные и аналитические работы",
                        "description": "Материалы, где важны анализ, аргументация, ясная структура и умение делать выводы по теме.",
                        "link_label": "Смотреть работы",
                        "link_url_name": "research",
                    },
                    {
                        "tag": "Slides",
                        "title": "Презентации",
                        "description": "Слайды и объясняющие материалы, которые можно использовать и как часть учебного, и как часть профессионального портфолио.",
                        "link_label": "Перейти к презентациям",
                        "link_url_name": "presentations",
                    },
                    {
                        "tag": "Video",
                        "title": "YouTube",
                        "description": "Видео с лекциями и объяснениями, где можно увидеть подачу материала, темп мышления и работу с аудиторией.",
                        "link_label": "Открыть видео",
                        "link_url_name": "youtube",
                    },
                    {
                        "tag": "Employers",
                        "title": "Работодателям",
                        "description": "Страница с кратким и деловым описанием стека, навыков, подхода к работе и причины, почему этот сайт полезен при найме.",
                        "link_label": "Открыть страницу",
                        "link_url_name": "employers",
                    },
                    {
                        "tag": "Contact",
                        "title": "Контакты",
                        "description": "GitHub, Telegram, email и дополнительные материалы, чтобы быстро перейти от просмотра портфолио к диалогу.",
                        "link_label": "Связаться",
                        "link_url_name": "employers",
                    },
                ],
            },
            "projects": {
                "title": "Проекты | Портфолио",
                "eyebrow": "Projects",
                "heading": "Проекты",
                "description": "Подборка практических работ, через которые видно мой подход к backend-разработке: работа с API, организация структуры, чистота логики и внимание к деталям.",
                "items": [
                    {
                        "tag": "Backend",
                        "meta": "Python / FastAPI / APIs",
                        "title": "AirTrace",
                        "description": "Сервис анализа качества воздуха с запросами к внешним API, обработкой ошибок, валидацией входных данных и продуманной backend-логикой для выдачи итоговой информации пользователю.",
                        "links": [
                            {"label": "GitHub", "url": "https://github.com/yourusername/airtrace"},
                            {"label": "Подробнее", "url": "https://github.com/yourusername/airtrace#readme"},
                        ],
                    },
                    {
                        "tag": "Web",
                        "meta": "Django / Templates / CSS",
                        "title": "Personal Portfolio",
                        "description": "Личный сайт-портфолио на Django с отдельными разделами под проекты, исследования, презентации, YouTube-материалы и деловую страницу для работодателей.",
                        "links": [
                            {"label": "GitHub", "url": "https://github.com/yourusername/aquarium-resume"},
                            {"label": "Подробнее", "url": "https://github.com/yourusername/aquarium-resume#readme"},
                        ],
                    },
                    {
                        "tag": "Tooling",
                        "meta": "Python / CLI / Automation",
                        "title": "Study Assistant",
                        "description": "Набор утилит для учебных задач: заметки, структурирование материалов, мелкая автоматизация и упрощение повседневной работы с информацией.",
                        "links": [
                            {"label": "GitHub", "url": "https://github.com/yourusername/study-assistant"},
                            {"label": "Подробнее", "url": "https://github.com/yourusername/study-assistant#readme"},
                        ],
                    },
                    {
                        "tag": "Data",
                        "meta": "Python / SQLite / Analytics",
                        "title": "Research Archive",
                        "description": "Архив аналитических материалов с удобной структурой, карточками описаний и подготовкой данных для публикации в формате, понятном и преподавателю, и работодателю.",
                        "links": [
                            {"label": "GitHub", "url": "https://github.com/yourusername/research-archive"},
                            {"label": "Подробнее", "url": "https://github.com/yourusername/research-archive#readme"},
                        ],
                    },
                ],
            },
            "research": {
                "title": "Работы | Портфолио",
                "eyebrow": "Research",
                "heading": "Научные и аналитические работы",
                "description": "Здесь собраны материалы, в которых важны не только факты, но и способ их подачи: структура, аргументация, ясность выводов и аккуратное оформление.",
                "items": [
                    {
                        "tag": "Analytics",
                        "meta": "AI / Education",
                        "title": "Влияние ИИ на образование",
                        "description": "Аналитическая работа о роли искусственного интеллекта в образовательной среде: от пользы и ускорения обучения до рисков, связанных с зависимостью от цифровых инструментов.",
                        "links": [
                            {"label": "PDF", "url": "https://example.com/research/ai-education.pdf"},
                            {"label": "Подробнее", "url": "https://example.com/research/ai-education"},
                        ],
                    },
                    {
                        "tag": "Research",
                        "meta": "Digital Tools",
                        "title": "Исследование цифровых инструментов",
                        "description": "Материал о применении современных цифровых сервисов и ИИ-инструментов в учебной и профессиональной деятельности с акцентом на практическую пользу.",
                        "links": [
                            {"label": "PDF", "url": "https://example.com/research/digital-tools.pdf"},
                            {"label": "Подробнее", "url": "https://example.com/research/digital-tools"},
                        ],
                    },
                    {
                        "tag": "Review",
                        "meta": "Technology / Society",
                        "title": "Технологии и повседневная эффективность",
                        "description": "Краткий аналитический обзор о том, как цифровые инструменты меняют организацию работы, принятие решений и скорость доступа к знаниям.",
                        "links": [
                            {"label": "PDF", "url": "https://example.com/research/technology-efficiency.pdf"},
                            {"label": "Подробнее", "url": "https://example.com/research/technology-efficiency"},
                        ],
                    },
                    {
                        "tag": "Academic",
                        "meta": "Structured Writing",
                        "title": "Пример исследовательской статьи",
                        "description": "Демонстрационный материал, показывающий умение работать с темой последовательно: от постановки вопроса до вывода и аккуратной подачи результатов.",
                        "links": [
                            {"label": "PDF", "url": "https://example.com/research/sample-article.pdf"},
                            {"label": "Подробнее", "url": "https://example.com/research/sample-article"},
                        ],
                    },
                ],
            },
            "presentations": {
                "title": "Презентации | Портфолио",
                "eyebrow": "Presentations",
                "heading": "Презентации",
                "description": "Слайды и визуально собранные материалы, где важны структура выступления, логика переходов и умение объяснять сложные темы спокойным и понятным языком.",
                "items": [
                    {
                        "tag": "Lecture",
                        "meta": "AI / Intro",
                        "title": "Лекция: как работает ИИ",
                        "description": "Презентация простым языком о происхождении ИИ, его базовых принципах, практической пользе и ограничениях, которые важно понимать начинающим.",
                        "links": [
                            {"label": "PDF", "url": "https://example.com/presentations/ai-intro.pdf"},
                            {"label": "Google Slides", "url": "https://docs.google.com/presentation/d/your-presentation-id/edit"},
                        ],
                    },
                    {
                        "tag": "Analytics",
                        "meta": "Clean Slides",
                        "title": "Аналитическая презентация",
                        "description": "Пример структурированной подачи материала с аккуратной типографикой, ясной последовательностью тезисов и акцентом на понятную аргументацию.",
                        "links": [
                            {"label": "PDF", "url": "https://example.com/presentations/analytics-deck.pdf"},
                            {"label": "Подробнее", "url": "https://example.com/presentations/analytics-deck"},
                        ],
                    },
                    {
                        "tag": "Education",
                        "meta": "Slides / Notes",
                        "title": "Учебные слайды по цифровым инструментам",
                        "description": "Материал о современных сервисах и цифровой среде, оформленный как компактная презентация для объяснения темы без перегрузки визуальными деталями.",
                        "links": [
                            {"label": "PDF", "url": "https://example.com/presentations/digital-tools.pdf"},
                            {"label": "Google Slides", "url": "https://docs.google.com/presentation/d/your-digital-tools-id/edit"},
                        ],
                    },
                    {
                        "tag": "Public Talk",
                        "meta": "Visual Storytelling",
                        "title": "Выступление с технологической темой",
                        "description": "Шаблон презентации для публичного выступления: компактные блоки, визуальная дисциплина и подача, которая поддерживает речь, а не спорит с ней.",
                        "links": [
                            {"label": "PDF", "url": "https://example.com/presentations/public-talk.pdf"},
                            {"label": "Подробнее", "url": "https://example.com/presentations/public-talk"},
                        ],
                    },
                ],
            },
            "youtube": {
                "title": "YouTube | Портфолио",
                "eyebrow": "YouTube",
                "heading": "YouTube и видео-материалы",
                "description": "Видеоформат показывает не только содержание, но и подачу: как я структурирую тему, объясняю сложные вещи и удерживаю фокус на сути.",
                "video": {
                    "tag": "Video",
                    "meta": "Lecture / Demo",
                    "title": "Демонстрационное видео YouTube",
                    "description": "Сейчас здесь стоит рабочий demo-ролик, чтобы блок точно открывался без ошибок. Позже его можно заменить на собственное видео, просто подставив нужный YouTube ID.",
                    "embed_url": "https://www.youtube.com/embed/M7lc1UVf-VE",
                    "title_attr": "YouTube demo video",
                },
                "why": {
                    "tag": "Why Video",
                    "meta": "Communication",
                    "title": "Зачем этот раздел",
                    "description": "Для работодателя и зрителя это быстрый способ оценить навык объяснения, публичную подачу, дисциплину мысли и способность ясно говорить о технических или аналитических темах.",
                },
            },
            "employers": {
                "title": "Работодателям | Портфолио",
                "eyebrow": "For Employers",
                "heading": "Информация для работодателей",
                "description": "Кратко и по делу: кто я, с каким стеком работаю, что уже умею и почему этот сайт полезен как единая точка просмотра моего профессионального профиля.",
                "intro": {
                    "tag": "Profile",
                    "meta": "Junior Backend Developer",
                    "title": "Кто я",
                    "description": "Я Junior Backend Developer. Работаю с Python, Django и FastAPI, интересуюсь архитектурой приложений, качеством кода, структурой backend-части и аккуратной подачей технических материалов.",
                },
                "stack_title": "Мой стек",
                "stack_items": ["Python", "Django", "FastAPI", "SQLite / PostgreSQL", "Git", "HTML / CSS"],
                "skills_title": "Что умею",
                "skills_items": [
                    "Разработка backend-логики",
                    "Проектирование API",
                    "Работа с базами данных",
                    "Структурирование и анализ информации",
                    "Подготовка технических и аналитических материалов",
                ],
                "approach_title": "Подход к работе",
                "approach_items": [
                    "Пишу код так, чтобы его было удобно читать и поддерживать",
                    "Стараюсь понимать систему глубже, а не только закрывать задачу локально",
                    "Ценю ясную структуру, дисциплину и аккуратную реализацию",
                ],
                "why_title": "Почему этот сайт полезен работодателю",
                "why_description": "Здесь собраны не только проекты, но и презентации, аналитические материалы и видео. Это помогает увидеть не только стек, но и способ мышления, качество подачи и ширину интересов.",
                "contacts": {
                    "tag": "Contacts",
                    "meta": "Open to communication",
                    "title": "Контакты",
                    "resume_label": "Резюме PDF",
                    "resume_url": "https://example.com/resume/kirill-resume.pdf",
                },
            },
            "errors": {
                "error_404": {
                    "title": "Страница не найдена | Портфолио",
                    "code": "404",
                    "eyebrow": "Navigation Lost",
                    "heading": "Похоже, этой страницы здесь нет.",
                    "description": "Ссылка могла устареть, либо адрес был введён с ошибкой. Вернись на главную или открой проекты, чтобы продолжить просмотр портфолио.",
                },
                "error_500": {
                    "title": "Ошибка сервера | Портфолио",
                    "code": "500",
                    "eyebrow": "System Fault",
                    "heading": "Что-то пошло не так на стороне сервера.",
                    "description": "Страница временно недоступна. Попробуй открыть сайт позже или перейди на главную, чтобы начать заново.",
                },
            },
        },
    },
    "en": {
        "site": {
            "lang": "en",
            "language_label": "Language",
            "brand_name": "Kirill",
            "brand_role": "Backend Portfolio",
            "nav": {
                "home": "Home",
                "projects": "Projects",
                "research": "Research",
                "presentations": "Presentations",
                "youtube": "YouTube",
                "employers": "For Employers",
            },
            "footer_name": "Kirill",
            "footer_role": "Junior Backend Developer · Python, Django, FastAPI",
            "links": {
                "github": "GitHub",
                "telegram": "Telegram",
                "email": "Email",
            },
            "contact": {
                "github_url": "https://github.com/yourusername",
                "telegram_url": "https://t.me/yourusername",
                "email": "kirill@example.com",
            },
            "error": {
                "back_home": "Back Home",
                "to_projects": "View Projects",
            },
        },
        "pages": {
            "home": {
                "title": "Home | Portfolio",
                "eyebrow": "Junior Backend Developer",
                "heading": "Kirill. Python, Django, FastAPI.",
                "description": "I build clean backend projects, study application architecture, and package technical materials so they are easy to read and discuss. This site brings together code, research, presentations, and public explainers.",
                "buttons": {
                    "projects": "Projects",
                    "employers": "For Employers",
                },
                "focus_eyebrow": "Focus",
                "focus_heading": "Current stack and interests",
                "focus_items": [
                    "Python, Django, FastAPI",
                    "REST APIs and backend logic",
                    "Project structure and code quality",
                    "Analytical and educational materials",
                ],
                "metrics": [
                    {"value": "6", "label": "Site sections"},
                    {"value": "3", "label": "Core technologies"},
                    {"value": "1", "label": "Employer entry point"},
                ],
                "section": {
                    "eyebrow": "Navigation",
                    "heading": "What is on this site",
                    "description": "Each section is a separate layer of the portfolio, from hands-on development to materials that show how I think.",
                },
                "cards": [
                    {
                        "tag": "Projects",
                        "title": "Projects",
                        "description": "Pet projects, backend services, and study builds focused on architecture, APIs, and clear structure.",
                        "link_label": "Open section",
                        "link_url_name": "projects",
                    },
                    {
                        "tag": "Research",
                        "title": "Research and analytical work",
                        "description": "Materials where analysis, argumentation, clear structure, and thoughtful conclusions matter.",
                        "link_label": "View research",
                        "link_url_name": "research",
                    },
                    {
                        "tag": "Slides",
                        "title": "Presentations",
                        "description": "Slides and explainers that work both as academic materials and as part of a professional portfolio.",
                        "link_label": "Go to presentations",
                        "link_url_name": "presentations",
                    },
                    {
                        "tag": "Video",
                        "title": "YouTube",
                        "description": "Videos and lectures that show delivery, pacing, and audience communication.",
                        "link_label": "Open video",
                        "link_url_name": "youtube",
                    },
                    {
                        "tag": "Employers",
                        "title": "For Employers",
                        "description": "A concise business-facing page about my stack, skills, working style, and why this site is useful during hiring.",
                        "link_label": "Open page",
                        "link_url_name": "employers",
                    },
                    {
                        "tag": "Contact",
                        "title": "Contacts",
                        "description": "GitHub, Telegram, email, and supporting materials to move from browsing the portfolio to an actual conversation.",
                        "link_label": "Get in touch",
                        "link_url_name": "employers",
                    },
                ],
            },
            "projects": {
                "title": "Projects | Portfolio",
                "eyebrow": "Projects",
                "heading": "Projects",
                "description": "A selection of practical work that shows my approach to backend development: APIs, structure, logic clarity, and attention to detail.",
                "items": [
                    {
                        "tag": "Backend",
                        "meta": "Python / FastAPI / APIs",
                        "title": "AirTrace",
                        "description": "An air quality analytics service with external API requests, error handling, input validation, and solid backend logic for user-facing results.",
                        "links": [
                            {"label": "GitHub", "url": "https://github.com/yourusername/airtrace"},
                            {"label": "Read more", "url": "https://github.com/yourusername/airtrace#readme"},
                        ],
                    },
                    {
                        "tag": "Web",
                        "meta": "Django / Templates / CSS",
                        "title": "Personal Portfolio",
                        "description": "A Django portfolio site with separate sections for projects, research, presentations, YouTube materials, and an employer-facing page.",
                        "links": [
                            {"label": "GitHub", "url": "https://github.com/yourusername/aquarium-resume"},
                            {"label": "Read more", "url": "https://github.com/yourusername/aquarium-resume#readme"},
                        ],
                    },
                    {
                        "tag": "Tooling",
                        "meta": "Python / CLI / Automation",
                        "title": "Study Assistant",
                        "description": "A set of utilities for study workflows: notes, material organization, small automation, and day-to-day information handling.",
                        "links": [
                            {"label": "GitHub", "url": "https://github.com/yourusername/study-assistant"},
                            {"label": "Read more", "url": "https://github.com/yourusername/study-assistant#readme"},
                        ],
                    },
                    {
                        "tag": "Data",
                        "meta": "Python / SQLite / Analytics",
                        "title": "Research Archive",
                        "description": "An archive of analytical materials with a clean structure, descriptive cards, and data prepared for clear publication.",
                        "links": [
                            {"label": "GitHub", "url": "https://github.com/yourusername/research-archive"},
                            {"label": "Read more", "url": "https://github.com/yourusername/research-archive#readme"},
                        ],
                    },
                ],
            },
            "research": {
                "title": "Research | Portfolio",
                "eyebrow": "Research",
                "heading": "Research and analytical work",
                "description": "These materials are not only about facts, but also about how they are presented: structure, argumentation, clear conclusions, and careful formatting.",
                "items": [
                    {
                        "tag": "Analytics",
                        "meta": "AI / Education",
                        "title": "The impact of AI on education",
                        "description": "An analytical paper on the role of artificial intelligence in education, from accelerating learning to the risks of growing dependence on digital tools.",
                        "links": [
                            {"label": "PDF", "url": "https://example.com/research/ai-education.pdf"},
                            {"label": "Read more", "url": "https://example.com/research/ai-education"},
                        ],
                    },
                    {
                        "tag": "Research",
                        "meta": "Digital Tools",
                        "title": "A study of digital tools",
                        "description": "A paper about modern digital services and AI tools in educational and professional settings with a focus on practical value.",
                        "links": [
                            {"label": "PDF", "url": "https://example.com/research/digital-tools.pdf"},
                            {"label": "Read more", "url": "https://example.com/research/digital-tools"},
                        ],
                    },
                    {
                        "tag": "Review",
                        "meta": "Technology / Society",
                        "title": "Technology and everyday efficiency",
                        "description": "A short analytical review of how digital tools reshape work organization, decision-making, and the speed of access to knowledge.",
                        "links": [
                            {"label": "PDF", "url": "https://example.com/research/technology-efficiency.pdf"},
                            {"label": "Read more", "url": "https://example.com/research/technology-efficiency"},
                        ],
                    },
                    {
                        "tag": "Academic",
                        "meta": "Structured Writing",
                        "title": "Sample research article",
                        "description": "A demonstration piece showing the ability to work through a topic consistently, from the initial question to the final conclusion and polished presentation.",
                        "links": [
                            {"label": "PDF", "url": "https://example.com/research/sample-article.pdf"},
                            {"label": "Read more", "url": "https://example.com/research/sample-article"},
                        ],
                    },
                ],
            },
            "presentations": {
                "title": "Presentations | Portfolio",
                "eyebrow": "Presentations",
                "heading": "Presentations",
                "description": "Slides and visual materials where structure, sequencing, and the ability to explain complex topics in a calm and clear way matter.",
                "items": [
                    {
                        "tag": "Lecture",
                        "meta": "AI / Intro",
                        "title": "Lecture: how AI works",
                        "description": "A presentation that explains the origins of AI, its basic principles, practical benefits, and limitations in simple language.",
                        "links": [
                            {"label": "PDF", "url": "https://example.com/presentations/ai-intro.pdf"},
                            {"label": "Google Slides", "url": "https://docs.google.com/presentation/d/your-presentation-id/edit"},
                        ],
                    },
                    {
                        "tag": "Analytics",
                        "meta": "Clean Slides",
                        "title": "Analytical presentation",
                        "description": "An example of structured material delivery with clean typography, a clear thesis flow, and emphasis on understandable argumentation.",
                        "links": [
                            {"label": "PDF", "url": "https://example.com/presentations/analytics-deck.pdf"},
                            {"label": "Read more", "url": "https://example.com/presentations/analytics-deck"},
                        ],
                    },
                    {
                        "tag": "Education",
                        "meta": "Slides / Notes",
                        "title": "Study slides on digital tools",
                        "description": "Material about modern services and digital environments designed as a compact slide deck without visual overload.",
                        "links": [
                            {"label": "PDF", "url": "https://example.com/presentations/digital-tools.pdf"},
                            {"label": "Google Slides", "url": "https://docs.google.com/presentation/d/your-digital-tools-id/edit"},
                        ],
                    },
                    {
                        "tag": "Public Talk",
                        "meta": "Visual Storytelling",
                        "title": "A talk on a technology topic",
                        "description": "A presentation template for public speaking with compact blocks, visual discipline, and slides that support the talk instead of competing with it.",
                        "links": [
                            {"label": "PDF", "url": "https://example.com/presentations/public-talk.pdf"},
                            {"label": "Read more", "url": "https://example.com/presentations/public-talk"},
                        ],
                    },
                ],
            },
            "youtube": {
                "title": "YouTube | Portfolio",
                "eyebrow": "YouTube",
                "heading": "YouTube and video materials",
                "description": "Video shows not only the content itself, but also the way I structure a topic, explain complex ideas, and keep attention on the core message.",
                "video": {
                    "tag": "Video",
                    "meta": "Lecture / Demo",
                    "title": "Demo YouTube video",
                    "description": "A working demo video is embedded here so the block always renders correctly. Later you can replace it with your own video by changing the YouTube ID.",
                    "embed_url": "https://www.youtube.com/embed/M7lc1UVf-VE",
                    "title_attr": "YouTube demo video",
                },
                "why": {
                    "tag": "Why Video",
                    "meta": "Communication",
                    "title": "Why this section exists",
                    "description": "For employers and viewers, this is a quick way to assess explanation skills, public delivery, disciplined thinking, and the ability to speak clearly about technical or analytical topics.",
                },
            },
            "employers": {
                "title": "For Employers | Portfolio",
                "eyebrow": "For Employers",
                "heading": "Information for employers",
                "description": "A concise overview of who I am, which stack I use, what I can already do, and why this site is useful as a single point of access to my professional profile.",
                "intro": {
                    "tag": "Profile",
                    "meta": "Junior Backend Developer",
                    "title": "Who I am",
                    "description": "I am a Junior Backend Developer. I work with Python, Django, and FastAPI, and I am interested in application architecture, code quality, backend structure, and clear technical communication.",
                },
                "stack_title": "My stack",
                "stack_items": ["Python", "Django", "FastAPI", "SQLite / PostgreSQL", "Git", "HTML / CSS"],
                "skills_title": "What I can do",
                "skills_items": [
                    "Backend logic development",
                    "API design",
                    "Database work",
                    "Information structuring and analysis",
                    "Technical and analytical writing",
                ],
                "approach_title": "How I work",
                "approach_items": [
                    "I write code so it is easy to read and maintain",
                    "I try to understand the system deeply instead of solving tasks only locally",
                    "I value clear structure, discipline, and careful implementation",
                ],
                "why_title": "Why this site is useful for employers",
                "why_description": "This site includes not only projects, but also presentations, analytical materials, and video. It helps reveal not just the stack, but also the way I think, communicate, and learn.",
                "contacts": {
                    "tag": "Contacts",
                    "meta": "Open to communication",
                    "title": "Contacts",
                    "resume_label": "Resume PDF",
                    "resume_url": "https://example.com/resume/kirill-resume.pdf",
                },
            },
            "errors": {
                "error_404": {
                    "title": "Page not found | Portfolio",
                    "code": "404",
                    "eyebrow": "Navigation Lost",
                    "heading": "This page does not seem to exist.",
                    "description": "The link may be outdated, or the address was entered incorrectly. Return to the home page or open the projects section to continue browsing the portfolio.",
                },
                "error_500": {
                    "title": "Server error | Portfolio",
                    "code": "500",
                    "eyebrow": "System Fault",
                    "heading": "Something went wrong on the server side.",
                    "description": "The page is temporarily unavailable. Try again later or return to the home page to start over.",
                },
            },
        },
    },
}


def get_language(request: Any | None) -> str:
    if request is None:
        return DEFAULT_LANGUAGE

    lang = getattr(request, "site_language", None)
    if lang in SUPPORTED_LANGUAGES:
        return lang

    session = getattr(request, "session", None)
    if session is not None:
        session_lang = session.get("site_language")
        if session_lang in SUPPORTED_LANGUAGES:
            return session_lang

    return DEFAULT_LANGUAGE


def get_translations(lang: str) -> dict[str, Any]:
    return deepcopy(BASE_TRANSLATIONS.get(lang, BASE_TRANSLATIONS[DEFAULT_LANGUAGE]))


def build_site_context(request: Any | None, page_key: str | None = None) -> dict[str, Any]:
    lang = get_language(request)
    translations = get_translations(lang)

    context = {
        "lang": lang,
        "supported_languages": SUPPORTED_LANGUAGES,
        "site": translations["site"],
        "page_key": page_key,
    }

    if page_key:
        context["page"] = translations["pages"][page_key]

    return context
