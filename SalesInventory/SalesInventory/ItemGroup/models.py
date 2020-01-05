from django.db import models
# Create your models here.
class ItemGroup(models.Model):
    ItemGroupName = models.CharField(max_length=120,null = False,blank=False)
    GroupShortName = models.CharField(max_length=2 ,null = False,blank=False )
    IsActive = models.BooleanField(default=True)
    CreatedBy= models.CharField(max_length=200,null=True,blank=True)
    CreatedDate= models.DateTimeField(null=True,blank=True)
    UpdatedBy= models.CharField(max_length=200,null=True,blank=True)
    UpdatedDate= models.DateTimeField(null=True,blank=True)
    DeletedBy= models.CharField(max_length=200,null=True,blank=True)
    DeletedDate= models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.ItemGroupName