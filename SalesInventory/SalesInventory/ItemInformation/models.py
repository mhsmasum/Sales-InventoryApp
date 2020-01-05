from django.db import models
from ItemPackSize.models import ItemPackSize
from ItemBrand.models import ItemBrand
from ItemCategory.models import ItemCategory
from UnitofMeasure.models import UnitofMeasure

# Create your models here.


class ItemInformation(models.Model):
    ItemName =  models.CharField(max_length=150)
    ItemDescription =  models.CharField(max_length=500)
    ItemCode = models.CharField(max_length=100)
    IsActive = models.BooleanField(default=True)
    Remarks =  models.CharField(max_length=500,null=True,blank=True)
    ItemPackSize = models.ForeignKey(ItemPackSize,on_delete=models.CASCADE,null=True,blank=True)
    ItemBrand = models.ForeignKey(ItemBrand,on_delete=models.CASCADE,null=True,blank=True)
    ItemCategory = models.ForeignKey(ItemCategory,on_delete=models.CASCADE,null=True,blank=True)
    Uom = models.ForeignKey(UnitofMeasure,on_delete=models.CASCADE,null=True,blank=True)
    
    CreatedBy= models.CharField(max_length=200,null=True,blank=True)
    CreatedDate= models.DateTimeField(null=True,blank=True)
    UpdatedBy= models.CharField(max_length=200,null=True,blank=True)
    UpdatedDate= models.DateTimeField(null=True,blank=True)
    DeletedBy= models.CharField(max_length=200,null=True,blank=True)
    DeletedDate= models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.ItemName
    