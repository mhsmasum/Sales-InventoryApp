from  django import forms
from .models import ItemColor
from parsley.decorators import parsleyfy
# from parsley.decorators import parsleyfy
from django.forms  import ModelForm

@parsleyfy
class ItemColorForm(ModelForm):
    
    class Meta:
        model = ItemColor
        
        labels = {
            'itemcolor_name': 'Name : ',
            'itemcolor_name_bangla': 'Name (Bangla) : ',
            'itemcolor_remarks': 'Remarks : ',
            'itemcolor_code': 'Code : ',
            'IsActive':'Status : '
           
        }
        fields = ['itemcolor_name','itemcolor_name_bangla','itemcolor_remarks','itemcolor_code','IsActive','CreatedBy','CreatedDate','UpdatedBy','UpdatedDate','DeletedBy','DeletedDate']
        exclude = ('CreatedBy','CreatedDate','UpdatedBy','UpdatedDate','DeletedBy','DeletedDate')
        widgets = {
            'itemcolor_name': forms.TextInput(),
            'itemcolor_name_bangla': forms.TextInput(),
            'itemcolor_remarks': forms.Textarea(attrs={'rows':2}),
            'itemcolor_code': forms.TextInput(),
            'IsActive': forms.CheckboxInput(),
            
        }
        parsley_extras = {
            "itemcolor_name": {
                "required-message": "Item color Name Required",
            }            
        }
    def __init__(self, *args, **kwargs):
        super(ItemColorForm, self).__init__(*args, **kwargs)
        self.fields['itemcolor_name'].widget.attrs['class'] = 'form-control'
        self.fields['itemcolor_name_bangla'].widget.attrs['class'] = 'form-control'
        self.fields['itemcolor_remarks'].widget.attrs['class'] = 'form-control'
        self.fields['itemcolor_code'].widget.attrs['class'] = 'form-control'
        self.fields['IsActive'].widget.attrs['class'] = 'iCheck'
            




    
    

