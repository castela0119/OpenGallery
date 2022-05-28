from django.contrib import admin

# Register your models here.
from apps.surveys.models import Survey, Question, Choice, Reply

admin.site.register(Survey, Question, Choice, Reply)
