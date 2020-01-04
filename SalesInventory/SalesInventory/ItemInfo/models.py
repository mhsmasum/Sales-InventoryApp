from django.db import models

# Create your models here.


class ItemInfo(models.Model):
    ItemName =  models.CharField(max_length=500,null = False,blank=False)
    ItemDescription =  models.CharField(max_length=500,null = False,blank=False)
    