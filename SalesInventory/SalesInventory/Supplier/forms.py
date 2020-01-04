from  django import forms
from .models import Supplier
from parsley.decorators import parsleyfy
from django.forms  import ModelForm

@parsleyfy
class SupplierForm(ModelForm):
    
    class Meta:
        model = Supplier
        
        labels = {
            'SupplierName': "Name:",
            'SupplierPhone': "Cell/Phone No:",
            'SupplierEmail': "Email:",
            'SupplierWebsite': "Website:",
            'SupplierCountry': "Country:",
            'SupplierAddress': "Address:",
            'IsActive': "Is Active:",
           
        }
        fields = ['SupplierName','SupplierPhone' , 'SupplierEmail','SupplierWebsite','SupplierCountry','SupplierAddress' ,'IsActive' ,'CreatedBy','CreatedDate','UpdatedBy','UpdatedDate','DeletedBy','DeletedDate']
        exclude = ('CreatedBy','CreatedDate','UpdatedBy','UpdatedDate','DeletedBy','DeletedDate')
        widgets = {
            'SupplierName': forms.TextInput(),
            'SupplierPhone': forms.TextInput(),
            'SupplierEmail': forms.EmailInput(),
            'SupplierWebsite': forms.TextInput(),
            'SupplierCountry': forms.TextInput(),
            'SupplierAddress': forms.Textarea(),
            'IsActive':forms.CheckboxInput(),
            
        }
        parsley_extras = {
            "SupplierName": {
                "required-message": "Supplier name required.",
            },
            "SupplierCountry": {
                "required-message": "Country required.",
                
            },
            "SupplierAddress":{
                "required-message": "Address required.",
            },
            "SupplierWebsite":{
                "type":"url",
                
            },
            "SupplierEmail":{
                "type": "email",
                "error-message": "A valid email required."
            },
        }
    def __init__(self, *args, **kwargs):
        super(SupplierForm, self).__init__(*args, **kwargs)
        self.fields['SupplierName'].widget.attrs['class'] = 'form-control'
        self.fields['SupplierPhone'].widget.attrs['class'] = 'form-control'
        self.fields['SupplierEmail'].widget.attrs['class'] = 'form-control'
        self.fields['SupplierWebsite'].widget.attrs['class'] = 'form-control'
        self.fields['SupplierCountry'].widget.attrs['class'] = 'form-control'
        self.fields['SupplierAddress'].widget.attrs['class'] = 'form-control'
        self.fields['IsActive'].widget.attrs['class'] = 'iCheck'