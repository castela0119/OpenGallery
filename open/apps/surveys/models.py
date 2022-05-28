from django.db import models


class Survey(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "설문조사"
        db_table = "survey"

    def __str__(self):
        return self.title


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.PROTECT)
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    class Meta:
        verbose_name_plural = "질문"
        db_table = "question"

    def __str__(self):
        return self.text

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE)
    text = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name_plural = "선택사항"
        db_table = "choice"

    def __str__(self):
        return f"{self.question.text}:{self.text}"


class Submission(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.PROTECT)
    participant_email = models.EmailField(max_length=255)
    answer = models.ManyToManyField(Choice)
    status = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "제출"
        db_table = "submission"
