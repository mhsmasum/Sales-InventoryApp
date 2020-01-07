from django.db import models

# Create your models here.
class ItemColor(models.Model):
    itemcolor_name= models.CharField(max_length=200)
    itemcolor_name_bangla= models.CharField(max_length=200,null=True,blank=True)
    itemcolor_remarks= models.CharField(max_length=200,null=True,blank=True)
    itemcolor_code= models.CharField(max_length=200,null=True,blank=True)
    IsActive= models.BooleanField(default=True)

    CreatedBy= models.CharField(max_length=200,null=True,blank=True)
    CreatedDate= models.DateTimeField(null=True,blank=True)
    UpdatedBy= models.CharField(max_length=200,null=True,blank=True)
    UpdatedDate= models.DateTimeField(null=True,blank=True)
    DeletedBy= models.CharField(max_length=200,null=True,blank=True)
    DeletedDate= models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.itemcolor_name
