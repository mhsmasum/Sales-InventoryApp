from  django import forms
from .models import ItemInformation,ItemCategory,ItemPackSize,ItemBrand,UnitofMeasure
from parsley.decorators import parsleyfy
from django.forms  import ModelForm

@parsleyfy
class ItemInformationForm(ModelForm):    
    class Meta:
        model = ItemInformation
        
        labels = {
            'ItemName': 'Item Name : ',
            'ItemDescription': 'Item Description : ',
            'ItemCode': 'Item Code : ',
            'IsActive':'Status : ',
            'Remarks': 'Remarks : ',
            'ItemPackSize': 'Item Size : ',
            'ItemBrand': 'Brand Name : ',
            'ItemCategory': 'Item Category : ',
            'Uom': 'UOM : ' 
        }
        fields = ['ItemName','ItemCode','ItemPackSize','ItemBrand','ItemCategory','Uom','ItemDescription','Remarks','IsActive','CreatedBy','CreatedDate','UpdatedBy','UpdatedDate','DeletedBy','DeletedDate' ]
        exclude = ('CreatedBy','CreatedDate','UpdatedBy','UpdatedDate','DeletedBy','DeletedDate')
        widgets = {
            'ItemName': forms.TextInput(),
            'ItemDescription': forms.Textarea(attrs={'rows':2}),
            'ItemCode': forms.TextInput(),
            'IsActive': forms.CheckboxInput(),
            'Remarks': forms.Textarea(attrs={'rows':2}),
            'ItemPackSize': forms.Select(),
            'ItemBrand': forms.Select(),
            'ItemCategory': forms.Select(),
            'Uom': forms.Select()
        }
        parsley_extras = {
            "ItemName": {
                "required-message": "Item Name Required",
            },
            "ItemDescription":{
                "required-message":"Item Description Required"
            },
            "ItemCode":{
                "required-message":"Item Code Required"
            }
        }
    def __init__(self, *args, **kwargs):
        super(ItemInformationForm, self).__init__(*args, **kwargs)        
        self.fields['ItemName'].widget.attrs['class'] = 'form-control description'
        self.fields['ItemDescription'].widget.attrs['class'] = 'form-control ItemDescription'
        self.fields['ItemDescription'].widget.attrs['readonly'] = True # text input
        #myform.fields['status'].widget.attrs['disabled'] = True # radio / checkbox
        self.fields['ItemCode'].widget.attrs['class'] = 'form-control description'
        self.fields['IsActive'].widget.attrs['class'] = 'iCheck'
        self.fields['Remarks'].widget.attrs['class'] = 'form-control'
        self.fields['ItemPackSize'].widget.attrs['class'] = 'form-control select2 description'
        self.fields['ItemPackSize'].queryset = ItemPackSize.objects.values_list('ItemPackSizeName', flat=True).filter(IsActive = True,DeletedBy=None).distinct()
        self.fields['ItemBrand'].widget.attrs['class'] = 'form-control select2'
        self.fields['ItemBrand'].queryset = ItemBrand.objects.values_list('itembrand_name', flat=True).filter(IsActive = True,DeletedBy=None)
        self.fields['ItemCategory'].widget.attrs['class'] = 'form-control select2'
        self.fields['ItemCategory'].queryset = ItemCategory.objects.values_list('itemcategory_title', flat=True).filter(IsActive = True,DeletedBy=None)
        self.fields['Uom'].widget.attrs['class'] = 'form-control select2'
        self.fields['Uom'].queryset = UnitofMeasure.objects.values_list('uom_name', flat=True).filter(IsActive = True,DeletedBy=None)
        # self.fields['Uom'].queryset = UnitofMeasure.objects.filter(IsActive = True,DeletedBy=None)