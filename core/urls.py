from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('research/', views.research, name='research'),
    path('presentations/', views.presentations, name='presentations'),
    path('youtube/', views.youtube, name='youtube'),
    path('employers/', views.employers, name='employers'),
    path("language/<str:lang_code>/", views.set_language, name="set_language"),
]
