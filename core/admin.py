from django.contrib import admin

from .models import Presentation, Project, ResearchWork, Video


class LocalizedCardAdmin(admin.ModelAdmin):
    list_display = ("title_ru", "title_en", "tag_ru", "is_published", "sort_order", "updated_at")
    list_filter = ("is_published",)
    search_fields = ("title_ru", "title_en", "description_ru", "description_en")
    list_editable = ("is_published", "sort_order")
    ordering = ("sort_order", "title_ru")


@admin.register(Project)
class ProjectAdmin(LocalizedCardAdmin):
    pass


@admin.register(ResearchWork)
class ResearchWorkAdmin(LocalizedCardAdmin):
    pass


@admin.register(Presentation)
class PresentationAdmin(LocalizedCardAdmin):
    pass


@admin.register(Video)
class VideoAdmin(LocalizedCardAdmin):
    pass
