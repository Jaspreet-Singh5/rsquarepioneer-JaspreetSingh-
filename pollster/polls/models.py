from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text



class Bus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    
    model_name = models.CharField(max_length=30)
    bus_no = models.IntegerField(default=0)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip = models.IntegerField(default=0)
    
    last_used_date = models.DateTimeField('last date used')
    diesel_daily_consumption = models.IntegerField(default=0)
    diesel_daily_rate = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text