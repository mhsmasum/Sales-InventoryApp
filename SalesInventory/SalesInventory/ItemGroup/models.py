from django.db import models
from django.db import models
# Create your models here.
class ItemGroup(models.Model):
    ItemGroupName = models.CharField(max_length=120)
    GroupShortName = models.CharField(max_length=5  )
    IsActive = models.BooleanField(default=True)
    IsDelete = models.BooleanField(default=False)
    CreateBy = models.CharField(max_length=500  )
    CreateDate = models.DateTimeField(auto_now_add=True )
    UpdateBy = models.CharField(max_length=500 , blank=True,null=True )
    UpdateDate = models.DateTimeField(auto_now=True,blank=True,null=True )
    DeleteBy = models.CharField(max_length=500 , blank=True,null=True )