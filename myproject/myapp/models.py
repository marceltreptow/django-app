from django.db import models

# Create your models here.

class Dog(models.Model):
    LAPRADUDEL_CHOICE = 'L'
    RACE_CHOICES = [
        (LAPRADUDEL_CHOICE, 'Lapradudel'),
    ]
    name = models.CharField(max_length=255)
    race = models.CharField(max_length=1, choices=RACE_CHOICES, default=LAPRADUDEL_CHOICE)
    age = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to='dog_images/', null=True)
