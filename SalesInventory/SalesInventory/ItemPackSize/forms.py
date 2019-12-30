from  django import forms
from .models import *
from parsley.decorators import parsleyfy
from django.forms  import ModelForm
@parsleyfy
class ItemPackSizeForm(ModelForm):

    class Meta:
        model = ItemPackSize
        
        labels = {
            'ItemPackSizeName': "Pack size name:",
            'ItemPackSizeDesc': "Description:",
            'IsActive': "Is Active:"
           
        }
        fields = ['ItemPackSizeName','ItemPackSizeDesc' , 'IsActive' ,'CreatedBy','CreatedDate','UpdatedBy','UpdatedDate','DeletedBy','DeletedDate']
        exclude = ('CreatedBy','CreatedDate','UpdatedBy','UpdatedDate','DeletedBy','DeletedDate')
        widgets = {
            'ItemPackSizeName': forms.TextInput(),
            'ItemPackSizeDesc': forms.TextInput(),
            'IsActive':forms.CheckboxInput(),
            
        }
        parsley_extras = {
            "ItemPackSizeName": {
                "required-message": "Name required",
            }
            
        }
    def __init__(self, *args, **kwargs):
        super(ItemPackSizeForm, self).__init__(*args, **kwargs)
        self.fields['ItemPackSizeName'].widget.attrs['class'] = 'form-control'
        self.fields['ItemPackSizeDesc'].widget.attrs['class'] = 'form-control'
        self.fields['IsActive'].widget.attrs['class'] = 'iCheck'