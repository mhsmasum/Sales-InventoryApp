from django.db import models

# Create your models here.
class ItemColor(models.Model):
    itemcolor_name= models.CharField(max_length=200)
    itemcolor_name_bangla= models.CharField(max_length=200,null=True,blank=True)
    itemcolor_remarks= models.CharField(max_length=200,null=True,blank=True)
    itemcolor_code= models.CharField(max_length=200,null=True,blank=True)
    isactive= models.BooleanField(default=True)

    created_by= models.CharField(max_length=200,null=True,blank=True)
    created_date= models.DateTimeField(null=True,blank=True)
    updated_by= models.CharField(max_length=200,null=True,blank=True)
    updated_date= models.DateTimeField(null=True,blank=True)
    deleted_by= models.CharField(max_length=200,null=True,blank=True)
    deleted_date= models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.itemcolor_name
