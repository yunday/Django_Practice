from django.db import models

# Create your models here.
class Question(models.Model):
    # id는 장고에서 알아서 만들어줌
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # Question이라는 모델을 참조하겠다
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
