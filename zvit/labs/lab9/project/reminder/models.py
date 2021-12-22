from django.db import models

# Create your models here.
class Note(models.Model):
    name = models.CharField(max_length=32, null=False) # назва
    text = models.TextField(max_length=128) # текст
    date_start = models.DateTimeField(auto_now_add=True)
    date_finish = models.DateTimeField(default=None) # запланований час
    complete = models.BooleanField(default=False)