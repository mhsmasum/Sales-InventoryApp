from django.db import models

# Create your models here.

class Supplier(models.Model):
    SupplierName = models.CharField(max_length=200 , null=False , blank=False)
    SupplierPhone= models.CharField(max_length=50 , null=True , blank=True)
    SupplierEmail= models.CharField(max_length=150 , null=True , blank=True)
    SupplierWebsite= models.URLField(max_length=500 , null=True , blank=True)
    SupplierCountry= models.CharField(max_length=200 , null=True , blank=True)
    SupplierAddress= models.CharField(max_length=500 , null=False , blank=False)
    IsActive = models.BooleanField(default=True)
    CreatedBy= models.CharField(max_length=200,null=True,blank=True)
    CreatedDate= models.DateTimeField(null=True,blank=True)
    UpdatedBy= models.CharField(max_length=200,null=True,blank=True)
    UpdatedDate= models.DateTimeField(null=True,blank=True)
    DeletedBy= models.CharField(max_length=200,null=True,blank=True)
    DeletedDate= models.DateTimeField(null=True,blank=True)