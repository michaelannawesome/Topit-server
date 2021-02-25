from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.name


class Data(models.Model):
    title = models.CharField(max_length=100)
    source = models.CharField(max_length=200)
    props = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    video_url = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="data")

    def __str__(self):
        return self.name