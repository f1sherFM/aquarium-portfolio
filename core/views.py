from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .localization import DEFAULT_LANGUAGE, SUPPORTED_LANGUAGES, build_site_context
from .models import Project


def render_page(request: HttpRequest, template_name: str, page_key: str, status: int = 200) -> HttpResponse:
    return render(request, template_name, build_site_context(request, page_key), status=status)


def load_published_items(model, lang: str) -> list[dict[str, object]]:
    queryset = model.objects.filter(is_published=True).order_by("sort_order", "-created_at")
    return [item.as_card_data(lang) for item in queryset]


def home(request: HttpRequest) -> HttpResponse:
    return render_page(request, "home.html", "home")


def projects(request: HttpRequest) -> HttpResponse:
    context = build_site_context(request, "projects")
    items = load_published_items(Project, context["lang"])
    if items:
        context["page"]["items"] = items
    return render(request, "projects.html", context)


def research(request: HttpRequest) -> HttpResponse:
    context = build_site_context(request, "research")
    context["page"]["items"] = []
    return render(request, "research.html", context)


def presentations(request: HttpRequest) -> HttpResponse:
    context = build_site_context(request, "presentations")
    if context["lang"] == "en":
        context["page"]["items"] = [
            {
                "tag": "Presentation",
                "meta": "AI / Intro",
                "title": "Artificial intelligence: complex ideas made simple",
                "description": "A presentation that explains artificial intelligence in a simple and accessible way.",
                "links": [
                    {"label": "PPTX", "url": "/static/files/ai-explained-simple.pptx"},
                ],
            }
        ]
    else:
        context["page"]["items"] = [
            {
                "tag": "Презентация",
                "meta": "AI / Intro",
                "title": "Искусственный интеллект: просто о сложном",
                "description": "Презентация, в которой искусственный интеллект объясняется простым и понятным языком.",
                "links": [
                    {"label": "PPTX", "url": "/static/files/ai-explained-simple.pptx"},
                ],
            }
        ]
    return render(request, "presentations.html", context)


def youtube(request: HttpRequest) -> HttpResponse:
    context = build_site_context(request, "youtube")
    context["page"]["videos"] = []
    return render(request, "youtube.html", context)


def employers(request: HttpRequest) -> HttpResponse:
    return render_page(request, "employers.html", "employers")


def set_language(request: HttpRequest, lang_code: str) -> HttpResponse:
    if lang_code in SUPPORTED_LANGUAGES:
        request.session["site_language"] = lang_code
    else:
        request.session["site_language"] = DEFAULT_LANGUAGE

    next_url = request.POST.get("next") or request.GET.get("next") or reverse("home")
    return redirect(next_url)


def error_404(request: HttpRequest, exception) -> HttpResponse:
    return render_page(request, "404.html", "errors", status=404)


def error_500(request: HttpRequest) -> HttpResponse:
    return render_page(request, "500.html", "errors", status=500)
