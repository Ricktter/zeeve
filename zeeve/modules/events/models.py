from django.db import models
from django.contrib.postgres.fields import ArrayField

from modules.bands.models import Band
from modules.bars.models import Bar

# Create your models here.


class Events(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
    bandas = models.ManyToManyField(Band)
    bar  = models.ForeignKey(Bar, on_delete=models.CASCADE)
    photos =  models.ImageField(upload_to='/media/images')
    tags = ArrayField(models.CharField(max_length=200), blank=True)



