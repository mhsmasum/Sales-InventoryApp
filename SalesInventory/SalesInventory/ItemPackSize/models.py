from django.db import models

# Create your models here.

class ItemPackSize(models.Model):
    ItemPackSizeName =  models.CharField(max_length=120,null = False,blank=False)
    ItemPackSizeDesc =  models.CharField(max_length=500,null = True,blank=True)
    IsActive = models.BooleanField(default=True)
    CreatedBy= models.CharField(max_length=200,null=True,blank=True)
    CreatedDate= models.DateTimeField(null=True,blank=True)
    UpdatedBy= models.CharField(max_length=200,null=True,blank=True)
    UpdatedDate= models.DateTimeField(null=True,blank=True)
    DeletedBy= models.CharField(max_length=200,null=True,blank=True)
    DeletedDate= models.DateTimeField(null=True,blank=True)

