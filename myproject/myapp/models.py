from django.db import models

# Create your models here.
class features(models.Model):
    # id: int
    # name:str
    # details: str
    # is_true :bool
    name= models.CharField(max_length=100)
    details = models.CharField(max_length=500)
        