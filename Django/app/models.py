from django.db import models

# Create your models here. LATER THIS IS THE DATABASE
class Question(models.Model):
    #column name=datatype
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    #each choice is associated with 1 question.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
