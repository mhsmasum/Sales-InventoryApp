from django.db import models
from ItemPackSize.models import ItemPackSize
# Create your models here.


class ItemInfo(models.Model):
    ItemName =  models.CharField(max_length=500,null = False,blank=False)
    ItemDescription =  models.CharField(max_length=500,null = False,blank=False)
    ItemPackSize = models.ForeignKey(ItemPackSize,on_delete=models.CASCADE)
    