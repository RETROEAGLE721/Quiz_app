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

