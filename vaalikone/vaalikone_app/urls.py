from django.contrib import admin
from django.urls import path, include
from .views import QuestionForm, Sek
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path("<id>", QuestionForm),
    path("vaalikone/vastaa", Sek)
]