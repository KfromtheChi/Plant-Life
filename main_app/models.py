from django.db import models

# Create your models here.
class Plant(models.Model):
    name = models.TextField()
    species = models.TextField()
    botanical_name = models.TextField()
    notes = models.TextField()
