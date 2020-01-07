from django.db import models

UNITBASISNAME_CHOICES = (
    ('Length (Measurable)','Length (Measurable)'),
    ('Mass & Weight (Weightable)', 'Mass & Weight (Weightable)'),
    ('Capacity & Volume (Weightable)','Capacity & Volume (Weightable)'),
    ('Countable','Countable'),
)
# Create your models here.
class UnitofMeasure(models.Model):
    unitbasisname = models.CharField(max_length=100,choices=UNITBASISNAME_CHOICES)
    uom_name= models.CharField(max_length=200)
    uom_shortname= models.CharField(max_length=50)
    IsActive= models.BooleanField(default=True)
    
    CreatedBy= models.CharField(max_length=200,null=True,blank=True)
    CreatedDate= models.DateTimeField(null=True,blank=True)
    UpdatedBy= models.CharField(max_length=200,null=True,blank=True)
    UpdatedDate= models.DateTimeField(null=True,blank=True)
    DeletedBy= models.CharField(max_length=200,null=True,blank=True)
    DeletedDate= models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.uom_name

class UnitofMeasureDetails(models.Model):    
    uomid = models.ForeignKey(UnitofMeasure, on_delete=models.CASCADE)
    uomdetails_name= models.CharField(max_length=200)
    uomdetails_shortname= models.CharField(max_length=50,null=True,blank=True)
    isbaseuom= models.BooleanField(default=False)
    convertionvalue= models.DecimalField(decimal_places=2,max_digits=10)

    CreatedBy= models.CharField(max_length=200,null=True,blank=True)
    CreatedDate= models.DateTimeField(null=True,blank=True)
    UpdatedBy= models.CharField(max_length=200,null=True,blank=True)
    UpdatedDate= models.DateTimeField(null=True,blank=True)
    DeletedBy= models.CharField(max_length=200,null=True,blank=True)
    DeletedDate= models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.uomdetails_name        