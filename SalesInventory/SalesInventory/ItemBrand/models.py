from django.db import models

# Create your models here.
class ItemBrand(models.Model):
    itembrand_name= models.CharField(max_length=200)
    itembrand_name_bangla= models.CharField(max_length=200,null=True,blank=True)
    itembrand_remarks= models.CharField(max_length=200,null=True,blank=True)
    itembrand_code= models.CharField(max_length=200,null=True,blank=True)
    isactive= models.BooleanField(default=True)

    created_by= models.CharField(max_length=200,null=True,blank=True)
    created_date= models.DateTimeField(null=True,blank=True)
    updated_by= models.CharField(max_length=200,null=True,blank=True)
    updated_date= models.DateTimeField(null=True,blank=True)
    deleted_by= models.CharField(max_length=200,null=True,blank=True)
    deleted_date= models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.itembrand_name
