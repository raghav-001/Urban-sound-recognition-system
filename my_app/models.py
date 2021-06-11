from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AudioFile(models.Model):
    name = models.CharField(max_length=30)
    audio = models.FileField(upload_to='my_app/static/my_app/upload/')

    def __str__(self):
        return self.name


