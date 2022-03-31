import uuid

from django.db import models
from shortuuidfield import ShortUUIDField
from account.models import Company

# Create your models here.

class Localisation(models.Model):
      lat=models.CharField(max_length=30,null=True)
      lng=models.CharField(max_length=30,null=True)


class TrashCan(models.Model):
      id= ShortUUIDField(primary_key=True,max_length=4, editable=False)
      size= models.IntegerField(default=0)
      quantity= models.IntegerField(max_length=30, default=0)
      is_active= models.BooleanField(default=False)
      position= models.ForeignKey(Localisation,on_delete=models.CASCADE,related_name="TrashCans",null=True,blank=True,default=None)
      company= models.ForeignKey(Company, on_delete=models.CASCADE, null=True)