from  django import forms
from .models import ItemBrand
from parsley.decorators import parsleyfy
# from parsley.decorators import parsleyfy
from django.forms  import ModelForm

@parsleyfy
class ItemBrandForm(ModelForm):
    
    class Meta:
        model = ItemBrand
        
        labels = {
            'itembrand_name': 'Name : ',
            'itembrand_name_bangla': 'Name (Bangla) : ',
            'itembrand_remarks': 'Remarks : ',
            'itembrand_code': 'Code : ',
            'IsActive':'Status : '
           
        }
        fields = ['itembrand_name','itembrand_name_bangla','itembrand_remarks','itembrand_code','IsActive','CreatedBy','CreatedDate','UpdatedBy','UpdatedDate','DeletedBy','DeletedDate']
        exclude = ('CreatedBy','CreatedDate','UpdatedBy','UpdatedDate','DeletedBy','DeletedDate')
        widgets = {
            'itembrand_name': forms.TextInput(),
            'itembrand_name_bangla': forms.TextInput(),
            'itembrand_remarks': forms.Textarea(attrs={'rows':2}),
            'itembrand_code': forms.TextInput(),
            'IsActive': forms.CheckboxInput(),
            
        }
        parsley_extras = {
            "itembrand_name": {
                "required-message": "Item Brand Name Required",
            }            
        }
    def __init__(self, *args, **kwargs):
        super(ItemBrandForm, self).__init__(*args, **kwargs)
        self.fields['itembrand_name'].widget.attrs['class'] = 'form-control'
        self.fields['itembrand_name_bangla'].widget.attrs['class'] = 'form-control'
        self.fields['itembrand_remarks'].widget.attrs['class'] = 'form-control'
        self.fields['itembrand_code'].widget.attrs['class'] = 'form-control'
        self.fields['IsActive'].widget.attrs['class'] = 'iCheck'
            




    
    

