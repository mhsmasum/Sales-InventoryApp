from django.db import models
from ItemGroup.models import ItemGroup

# Create your models here.
class ItemCategory(models.Model):
    itemcategory_title= models.CharField(max_length=200)
    itemcategory_title_bangla= models.CharField(max_length=200,null=True,blank=True)
    itemcategory_code= models.CharField(max_length=200,null=True,blank=True)
    isactive= models.BooleanField(default=True)
    ItemGroup =models.ForeignKey(ItemGroup, on_delete=models.CASCADE, null=True)

    CreatedBy= models.CharField(max_length=200,null=True,blank=True)
    CreatedDate= models.DateTimeField(null=True,blank=True)
    UpdatedBy= models.CharField(max_length=200,null=True,blank=True)
    UpdatedDate= models.DateTimeField(null=True,blank=True)
    DeletedBy= models.CharField(max_length=200,null=True,blank=True)
    DeletedDate= models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.itemcategory_title
