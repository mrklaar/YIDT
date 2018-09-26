from django.db import models
from django.contrib.auth.models import User

# Create your models here.

GEAR_CHOICES = (
    ('-','-'),
    ('Manual', 'Manual'),
    ('Automatic', 'Automatic')
    )

FUEL_CHOICES = (
    ('-','-'),
    ('Petrol','Petrol'),
    ('Diesel','Diesel'),
    ('Electric','Electric'),
    ('Hybrid','Hybrid'),
    ('Biofuel','Biofuel')
    )

class Car(models.Model):
    Make = models.CharField(max_length=264)
    Model = models.CharField(max_length=264)
    Owner = models.CharField(max_length=264)
    Color = models.CharField(max_length=264)
    Year = models.IntegerField()
    Gear = models.CharField(max_length = 20, choices= GEAR_CHOICES, default='-')
    Weight = models.IntegerField()
    Fuel = models.CharField(max_length = 20, choices= FUEL_CHOICES, default='-')
    Power = models.IntegerField()
    Plate = models.CharField(max_length=16)
    Img = models.ImageField(null=True, blank=True)
    #Image = models.ImageField()

    def __str__(self):
        return str(self.Year) + " - " + str(self.Make) + " " + str(self.Model)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)

    #additional classes
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __self__(self):
        return self.user.username
