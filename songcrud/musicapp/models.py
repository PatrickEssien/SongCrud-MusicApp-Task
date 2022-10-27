from datetime import datetime
from email.policy import default
from importlib.resources import contents
from msilib.schema import Class
from unittest.util import _MAX_LENGTH
from django.db import models
# I cretaed the models and attributes for nmy music app

# Create your models here.
class Artiste(models.Model):
    # creating the attributes for the artiste
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)

    def _str_(self) -> str:
      return self.name

class Songs(models.Model):
    # creating the attributes for the songs
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    Title = models.CharField(max_length=100)
    Date_Released = models.DateField(default=datetime.today)
    Likes = models.IntegerField(max_length=50)
    artiste_id = models.IntegerField(max_length=50)
    
    def _str_(self) -> str:
      return self.name
class lyrics(models.Model):
    Songs = models.ForeignKey(Songs, on_delete=models.CASCADE)
    contents = models.CharField(_max_length=1000)
