from django.db import models

# Create your models here.

class Pic(models.Model):
    # picture of class and say prays and every event has occure


    picture = models.ImageField(upload_to='/media')
    capture = models.CharField(max_length=128)

class Lessen(models.Model):
    # pdf, word and every thing what useful for gues
    pass