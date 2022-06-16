from django.db import models


# Create your models here.

class Verb(models.Model):
    Infinitive = models.CharField(max_length=30)
    order = models.IntegerField
    group = models.IntegerField
    lang = models.CharField(max_length=2, default='fr')
