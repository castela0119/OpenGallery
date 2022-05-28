from django.urls import path
from apps.surveys.views import index, show_survey

urlpatterns = [
    path("", index),
    path("<int:id>/", show_survey, name="show-survey"),
]