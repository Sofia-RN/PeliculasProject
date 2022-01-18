from model_utils.models import TimeStampedModel
from django.db import models

# Create your models here.

class User(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=40, unique=True)
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    edad = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return self.nombre