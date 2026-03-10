from django.test import TestCase, override_settings
from django.urls import reverse


@override_settings(
    STORAGES={
        "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
        "staticfiles": {"BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"},
    }
)
class PortfolioViewsTests(TestCase):
    def set_language(self, language_code: str) -> None:
        session = self.client.session
        session["site_language"] = language_code
        session.save()

    def test_home_page_renders(self) -> None:
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Kirill")
        self.assertContains(response, "/projects/")
        self.assertContains(response, "/employers/")
        self.assertContains(response, ">7<")

    def test_language_switch_changes_session_and_content(self) -> None:
        response = self.client.post(
            reverse("set_language", args=["en"]),
            {"next": reverse("employers")},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.client.session["site_language"], "en")
        self.assertContains(response, "Information for employers")
        self.assertContains(response, "Resume PDF")

    def test_projects_page_shows_all_current_projects(self) -> None:
        self.set_language("en")
        response = self.client.get(reverse("projects"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "AirTrace RU")
        self.assertContains(response, "Habit Tracker")
        self.assertContains(response, "Bookstore API Course")
        self.assertContains(response, "Fishertools")
        self.assertContains(response, "Aquarium Portfolio")
        self.assertContains(response, "Knowledge Base")
        self.assertContains(response, "Skill Blog")
        self.assertContains(response, "https://github.com/f1sherFM/Airtrace-RU")
        self.assertContains(response, "https://github.com/f1sherFM/Habit-Tracker")
        self.assertContains(response, "https://github.com/f1sherFM/bookstore-api-course")
        self.assertContains(response, "https://github.com/f1sherFM/Fishertools")
        self.assertContains(response, "https://github.com/f1sherFM/aquarium-portfolio")
        self.assertContains(response, "https://github.com/f1sherFM/knowledge_base")
        self.assertContains(response, "https://github.com/f1sherFM/skill-blog-api")

    def test_presentations_page_shows_uploaded_presentation(self) -> None:
        self.set_language("en")
        response = self.client.get(reverse("presentations"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Artificial intelligence: complex ideas made simple")
        self.assertContains(response, "/static/files/ai-explained-simple.pptx")

    def test_research_page_shows_empty_state(self) -> None:
        self.set_language("en")
        response = self.client.get(reverse("research"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Section is empty for now")
        self.assertContains(response, "Research and analytical materials will be added later.")

    def test_youtube_page_shows_empty_state(self) -> None:
        self.set_language("en")
        response = self.client.get(reverse("youtube"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Section is empty for now")
        self.assertContains(response, "Video materials will be added later.")

    def test_employers_page_has_current_contacts(self) -> None:
        response = self.client.get(reverse("employers"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "https://github.com/f1sherFM")
        self.assertContains(response, "https://t.me/f1sherFM")
        self.assertContains(response, "mailto:c.balukov@yandex.ru")
        self.assertContains(response, "/static/files/kirill-resume.pdf")
