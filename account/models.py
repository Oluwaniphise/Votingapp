from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .choices import *
from ckeditor.fields import RichTextField
 
 


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='static/images')
    level = models.CharField(max_length=100,choices=Level, default="100")
    mat_no = models.CharField(max_length=50)
    dept = models.CharField(max_length=100, choices=COURSES_CHOICES, default='Computer Science')
    
    def __str__(self):
        return f'{self.user} - {self.mat_no}'

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()



class Course(models.Model):
    course = models.CharField(max_length=100)
    course_content = RichTextField()

    def __str__(self):
        return self.course


class Question(models.Model):
    question_post = models.CharField(max_length=250)


    def __str__(self):
        return self.question_post
    class Meta:
        ordering = ['question_post']

class Choice(models.Model):
    question_post = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_field = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)
    img = models.ImageField(upload_to='media/', default="/static/images/logo.svg")

   

    def __str__(self):
        return f'{self.choice_field}, {self.question_post}'

    


