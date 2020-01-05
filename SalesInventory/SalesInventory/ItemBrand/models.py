from django.db import models

# Create your models here.
class ItemBrand(models.Model):
    itembrand_name= models.CharField(max_length=200)
    itembrand_name_bangla= models.CharField(max_length=200,null=True,blank=True)
    itembrand_remarks= models.CharField(max_length=200,null=True,blank=True)
    itembrand_code= models.CharField(max_length=200,null=True,blank=True)
    isactive= models.BooleanField(default=True)

    CreatedBy= models.CharField(max_length=200,null=True,blank=True)
    CreatedDate= models.DateTimeField(null=True,blank=True)
    UpdatedBy= models.CharField(max_length=200,null=True,blank=True)
    UpdatedDate= models.DateTimeField(null=True,blank=True)
    DeletedBy= models.CharField(max_length=200,null=True,blank=True)
    DeletedDate= models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.itembrand_name
