from .localization import build_site_context


def site_translations(request):
    return build_site_context(request)
