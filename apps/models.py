from django.contrib.admin import models
from django.db import models

# Create your models here.

class Biodata(models.Model):
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    profession = models.CharField(max_length=45)

    def __str__(self):
        return self.name