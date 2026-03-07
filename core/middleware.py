from __future__ import annotations

from .localization import DEFAULT_LANGUAGE, SUPPORTED_LANGUAGES


class SiteLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        lang = request.session.get("site_language", DEFAULT_LANGUAGE)
        if lang not in SUPPORTED_LANGUAGES:
            lang = DEFAULT_LANGUAGE

        request.site_language = lang
        response = self.get_response(request)
        return response
