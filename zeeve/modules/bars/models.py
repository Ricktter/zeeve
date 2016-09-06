from django.db import models

# Create your models here.

class Bar (models.Model):
    id = models.AutoField(primary_key=True)
    name=  models.CharField(max_length=100)
    date_foundation = models.DateField();
    address = models.CharField(max_length=250)
    work_time = models.CharField(max_length=50)
    logo =  models.ImageField('/image/logo')
