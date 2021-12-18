from django.db import models

# Create your models here.

class Question(models.Model):
    question_post = models.CharField(max_length=250)


    def __str__(self):
        return self.question

class Choice(models.Model):
    question_post = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_field = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)
   

    def __str__(self):
        return f'{self.choice_field}, {self.question}'

    


