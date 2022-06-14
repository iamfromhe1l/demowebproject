from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=10)
    str = models.IntegerField()
    value = models.IntegerField()