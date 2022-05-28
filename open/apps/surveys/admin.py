from django.contrib import admin

# Register your models here.
from apps.surveys.models import Survey, Question, Choice, Reply, Results

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Reply)
admin.site.register(Results)