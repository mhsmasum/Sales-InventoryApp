from django.db import models
from ItemGroup.models import ItemGroup
# Create your models here.
class ItemCategory(models.Model):
    itemcategory_title= models.CharField(max_length=200)
    itemcategory_title_bangla= models.CharField(max_length=200,null=True,blank=True)
    itemcategory_code= models.CharField(max_length=200,null=True,blank=True)
    isactive= models.BooleanField(default=True)
    ItemGroup = models.ForeignKey(ItemGroup, on_delete=models.CASCADE)
    created_by= models.CharField(max_length=200,null=True,blank=True)
    created_date= models.DateTimeField(null=True,blank=True)
    updated_by= models.CharField(max_length=200,null=True,blank=True)
    updated_date= models.DateTimeField(null=True,blank=True)
    deleted_by= models.CharField(max_length=200,null=True,blank=True)
    deleted_date= models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.itemcategory_title
