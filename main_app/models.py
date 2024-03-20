from django.db import models
from django.urls import reverse

#Tuple of 2-tuples - options for drop down menus
TYPES = (
    ('W', 'Watered'),
    ('F', 'Fertilized'),
    ('P', 'Pruned'),
    ('R', 'Repotted'),
    ('PC', 'Pest Control'),
)

# Create your models here.
class Plant(models.Model):
    name = models.TextField()
    species = models.TextField()
    botanical_name = models.TextField()
    notes = models.TextField()

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})

class Plant_Care(models.Model):
    date = models.DateField()
    type = models.CharField(
        max_length=1,
        choices=TYPES,
        default=TYPES[0][0]
        )


class Quiz(models.Model):
    question1 = models.TextField()
    question2 = models.TextField()
    question3 = models.TextField()
    question4 = models.TextField()

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('detail', kwargs={'quiz_id': self.id})

class QuizSubmit(models.Model):
    HARDINESS_ZONE_CHOICES = [(str(i), str(i)) for i in range(1, 13)]
    SUN_CHOICES = [
        ('full_sun', 'Full Sun'),
        ('partial_sun', 'Partial Sun'),
        ('partial_shade', 'Partial Shade'),
        ('full_shade', 'Full Shade'),
    ]
    WATER_FREQUENCY_CHOICES = [
        ('frequent', 'Frequent'),
        ('average', 'Average'),
        ('minimal', 'Minimal'),
    ]
    MAINTENANCE_LEVEL_CHOICES = [
        ('low', 'Low'),
        ('moderate', 'Moderate'),
        ('high', 'High'),
    ]