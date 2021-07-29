import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.URLField(max_length=20000,unique=True)
    link=models.URLField(max_length=200)
    # pub_date=models.DateField(default=2222-2-22)
    def __str__(self):
        return self.question_text
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now()-datetime.timedelta(days=1)    

class Choice(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.URLField(max_length=200)
    votes = models.IntegerField(default=0)
    types =models.URLField()
    def __str__(self):
        return self.choice_text