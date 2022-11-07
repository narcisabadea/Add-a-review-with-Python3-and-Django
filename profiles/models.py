from django.db import models

# Create your models here.

class UserProfile(models.Model):
    # using FileField
    # image = models.FileField(upload_to="images")

    # using ImageField
    image = models.ImageField(upload_to="images")