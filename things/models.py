from django.db import models
from models import Model

# Create your models here.
class Thing(Model):
    name = models.TextField(unique=True, max_length=30)
    description = models.TextField(unique=False, max_length=120, blank=False)
    quantity = models.IntegerField(unique=False, max_length=100)
