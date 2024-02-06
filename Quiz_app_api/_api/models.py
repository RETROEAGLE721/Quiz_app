from email.policy import default
from pickle import TRUE
from django.db import models
from datetime import datetime

class mcqs(models.Model):
    number = models.IntegerField(editable=False)
    question = models.CharField(max_length = 1000)
    option_A = models.CharField(max_length=100)
    option_B = models.CharField(max_length=100)
    option_C = models.CharField(max_length=100)
    option_D = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    
    def save(self, *args, **kwargs):
        total = mcqs.objects.all().count()
        self.number = total + 1
        super().save(*args,**kwargs)


    def __str__(self):
        return str(self.number)


class Users(models.Model):

    name = models.CharField(max_length=50)
    passw = models.CharField(max_length=50)
    data_resgister = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.name)


class user_output(models.Model):
    
    id = models.BigAutoField(editable=True,primary_key=True, blank=False,null=False)
    name = models.CharField(max_length=50)
    total_score = models.IntegerField()
    Completion_time = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return str(self.name)