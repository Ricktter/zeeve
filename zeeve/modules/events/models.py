from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Events(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
    bandas = models.ManyToManyField()
    bar  = models.ForeignKey()
    photos =  models.ImageField(upload_to='/media/images')
    tags = ArrayField(models.CharField(max_length=200), blank=True)



