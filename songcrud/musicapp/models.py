from email.policy import default
from msilib.schema import Class
from unittest.util import _MAX_LENGTH
from django.db import models
# I cretaed the models and attributes for nmy music app

# Create your models here.
class artiste(models.Model):
    # creating the attributes for the artiste
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)

    def _str_(self) -> str:
      return self.name

class Songs(models.Model):
    # creating the attributes for the songs
    Title = models.CharField(max_length=50)
    Date_Released = models.CharField(max_length=50)
    Likes = models.CharField(max_length=50)
    artiste_id = models.CharField(max_length=50)
    User = models.ForeignKey( artiste, on_delete=models.CASCADE)
    def _str_(self) -> str:
      return self.name
