from django.db import models


class HealthInsaurenceData(models.Model):
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    bmi = models.FloatField()
    children = models.IntegerField()
    smoker = models.CharField(max_length=3)
    region = models.CharField(max_length=15)
    charges = models.FloatField()
