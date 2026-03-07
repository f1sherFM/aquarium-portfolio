from __future__ import annotations

from django.db import models


class PublishedOrderedModel(models.Model):
    is_published = models.BooleanField("Опубликовано", default=True)
    sort_order = models.PositiveIntegerField("Порядок", default=100)
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)

    class Meta:
        abstract = True
        ordering = ["sort_order", "-created_at"]


class LocalizedCardModel(PublishedOrderedModel):
    tag_ru = models.CharField("Тег (RU)", max_length=80)
    tag_en = models.CharField("Тег (EN)", max_length=80)
    meta_ru = models.CharField("Подзаголовок (RU)", max_length=120)
    meta_en = models.CharField("Подзаголовок (EN)", max_length=120)
    title_ru = models.CharField("Заголовок (RU)", max_length=200)
    title_en = models.CharField("Заголовок (EN)", max_length=200)
    description_ru = models.TextField("Описание (RU)")
    description_en = models.TextField("Описание (EN)")

    class Meta:
        abstract = True

    def get_localized_value(self, field_name: str, lang: str) -> str:
        if lang == "en":
            return getattr(self, f"{field_name}_en")
        return getattr(self, f"{field_name}_ru")

    def as_card_data(self, lang: str) -> dict[str, object]:
        return {
            "tag": self.get_localized_value("tag", lang),
            "meta": self.get_localized_value("meta", lang),
            "title": self.get_localized_value("title", lang),
            "description": self.get_localized_value("description", lang),
        }

    def __str__(self) -> str:
        return self.title_ru


class Project(LocalizedCardModel):
    github_url = models.URLField("GitHub URL")
    details_url = models.URLField("URL Подробнее", blank=True)

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ["sort_order", "-created_at"]

    def as_card_data(self, lang: str) -> dict[str, object]:
        data = super().as_card_data(lang)
        details_label = "Read more" if lang == "en" else "Подробнее"
        data["links"] = [{"label": "GitHub", "url": self.github_url}]
        if self.details_url:
            data["links"].append({"label": details_label, "url": self.details_url})
        return data


class ResearchWork(LocalizedCardModel):
    primary_url = models.URLField("Основная ссылка")
    secondary_url = models.URLField("Дополнительная ссылка", blank=True)
    primary_label_ru = models.CharField("Текст основной ссылки (RU)", max_length=80, default="PDF")
    primary_label_en = models.CharField("Текст основной ссылки (EN)", max_length=80, default="PDF")
    secondary_label_ru = models.CharField("Текст доп. ссылки (RU)", max_length=80, default="Подробнее")
    secondary_label_en = models.CharField("Текст доп. ссылки (EN)", max_length=80, default="Read more")

    class Meta:
        verbose_name = "Исследовательская работа"
        verbose_name_plural = "Исследовательские работы"
        ordering = ["sort_order", "-created_at"]

    def as_card_data(self, lang: str) -> dict[str, object]:
        data = super().as_card_data(lang)
        data["links"] = [
            {"label": self.get_localized_value("primary_label", lang), "url": self.primary_url},
        ]
        if self.secondary_url:
            data["links"].append(
                {"label": self.get_localized_value("secondary_label", lang), "url": self.secondary_url}
            )
        return data


class Presentation(LocalizedCardModel):
    primary_url = models.URLField("Основная ссылка")
    secondary_url = models.URLField("Дополнительная ссылка", blank=True)
    primary_label_ru = models.CharField("Текст основной ссылки (RU)", max_length=80, default="PDF")
    primary_label_en = models.CharField("Текст основной ссылки (EN)", max_length=80, default="PDF")
    secondary_label_ru = models.CharField("Текст доп. ссылки (RU)", max_length=80, default="Google Slides")
    secondary_label_en = models.CharField("Текст доп. ссылки (EN)", max_length=80, default="Google Slides")

    class Meta:
        verbose_name = "Презентация"
        verbose_name_plural = "Презентации"
        ordering = ["sort_order", "-created_at"]

    def as_card_data(self, lang: str) -> dict[str, object]:
        data = super().as_card_data(lang)
        data["links"] = [
            {"label": self.get_localized_value("primary_label", lang), "url": self.primary_url},
        ]
        if self.secondary_url:
            data["links"].append(
                {"label": self.get_localized_value("secondary_label", lang), "url": self.secondary_url}
            )
        return data


class Video(LocalizedCardModel):
    embed_url = models.URLField("YouTube embed URL")
    external_url = models.URLField("Внешняя ссылка", blank=True)
    external_label_ru = models.CharField("Текст внешней ссылки (RU)", max_length=80, default="Смотреть на YouTube")
    external_label_en = models.CharField("Текст внешней ссылки (EN)", max_length=80, default="Watch on YouTube")

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"
        ordering = ["sort_order", "-created_at"]

    def as_card_data(self, lang: str) -> dict[str, object]:
        data = super().as_card_data(lang)
        data["embed_url"] = self.embed_url
        data["title_attr"] = self.get_localized_value("title", lang)
        links: list[dict[str, str]] = []
        if self.external_url:
            links.append({"label": self.get_localized_value("external_label", lang), "url": self.external_url})
        data["links"] = links
        return data
