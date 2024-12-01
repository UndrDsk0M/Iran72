from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.finding_word, name='search_words')
]
