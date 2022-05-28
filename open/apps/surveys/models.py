from pyexpat import model
from django.db import models
from apps.account.models import CustomUser

# Create your models here.
class Survey(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    surveys = models.ForeignKey("Survey", related_name="survey", on_delete=models.CASCADE)
    subject = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


class Choice(models.Model):
    questions = models.ForeignKey("Question", related_name="question", on_delete=models.CASCADE)
    num = models.IntegerField()
    value = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.value


class Reply(models.Model):
    reply_surveys = models.ForeignKey("Survey", related_name="reply_survey", on_delete=models.CASCADE)
    num = models.IntegerChoices
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.value


class Results(models.Model):
    result_reply = models.ForeignKey("Reply", related_name="result_reply", on_delete=models.CASCADE)
    result_applicant = models.ForeignKey("account.CustomUser", related_name="reply_user", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
