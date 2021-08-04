import uuid

from django.db import models
from shortuuidfield import ShortUUIDField

# Create your models here.
class Localisation(models.Model):
      lat=models.CharField(max_length=30,null=True)
      lng=models.CharField(max_length=30,null=True)


class TrashCan(models.Model):
      id = ShortUUIDField(primary_key=True,max_length=4, editable=False)
      size = models.EmailField(max_length=255, unique=True)
      quantity = models.CharField(max_length=30)
      is_active = models.BooleanField(default=False)
      position= models.ForeignKey(Localisation,on_delete=models.CASCADE,null=True)