from django.db import models
from django.utils import timezone
# Create your models here.

class Event(models.Model):
    id = models.IntegerField(primary_key=True)
    event_name = models.CharField(max_length=2000)
    #email = models.CharField(max_length=200,default='SOME STRING')
    #decription = models.CharField(max_length= 1000)
    #start_time = models.DateTimeField(auto_now_add=False, blank=True)
    #end_time = models.DateTimeField(auto_now_add=False, blank=True)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now) 
    
