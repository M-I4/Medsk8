from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    city_choises = models.TextChoices("city", ["Riyadh", "Jeddah", "Dammam", "Medina"])
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    avatar = models.ImageField(upload_to="images/")
    city  = models.CharField(max_length=64, choices = city_choises.choices, default=city_choises.Riyadh)
    gender = models.TextField()
    age = models.IntegerField()
    is_skater = models.BooleanField()
    phoneNumber = models.IntegerField()





