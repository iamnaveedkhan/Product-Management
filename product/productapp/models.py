from django.db import models

# Create your models here.
class data(models.Model):
    name=models.CharField(max_length=100)
    quantity=models.IntegerField()
    type=models.CharField(max_length=100)
    batch=models.CharField(max_length=100)
    expire=models.DateField()
