from django.db import models

# Create your models here.
class AppUser(models.Model):
    AppUserName = models.CharField(max_length=50)
    AppUserPassword = models.CharField(max_length=50  )
    CreateDate =  models.DateTimeField(auto_now=True,blank=True,null=True )