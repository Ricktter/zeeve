from django.db import models
from django.contrib.postgres.fields import ArrayField

class Band(models.Model):

    id = models.AutoField(primary_key=True)
    created_date = models.DateField()
    biography = models.TextField()
    logo = models.ImageField(upload_to='/media/images/')
    slogan = models.CharField(max_length=50)
    music =  ArrayField(models.CharField(max_length=200))
    tags =  ArrayField(models.CharField(max_length=200, blank=True))