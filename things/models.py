from django.db import models

# Create your models here.
class Thing(models.Model):
    name = models.CharField(unique=True, max_length=30)
    description = models.TextField(unique=False, max_length=120, blank=False)
    quantity = models.IntegerField(unique=False)
