import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    # id는 장고에서 알아서 만들어줌
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    # 이 필드를 중심으로 하겠다
    was_published_recently.boolean = True
    # true false를 이모티콘으로 하겠다
    was_published_recently.short_description = 'Published recently?'
    # 설명으로 변경

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # Question이라는 모델을 참조하겠다
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
