from pyexpat import model
from django.db import models

# Create your models here.
class Survey(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Question(model.Model):
    surveys = models.ForeignKey("Survey", related_name="survey", on_delete=models.CASCADE)
    subject = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


class Choice(model.Model):
    questions = models.ForeignKey("Question", related_name="question", on_delete=models.CASCADE)
    num = models.IntegerField()
    value = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.questions


class Reply(model.Model):
    surveys = models.ForeignKey("Survey", related_name="survey", on_delete=models.CASCADE)
    applicants = models.ForeignKey("User", related_name="user", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.surveys
    
