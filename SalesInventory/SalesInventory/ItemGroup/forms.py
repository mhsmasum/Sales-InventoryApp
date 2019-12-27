from  django import forms
from .models import *
from parsley.decorators import parsleyfy
from django.forms  import ModelForm
@parsleyfy
class ItemGroupForm(ModelForm):

    class Meta:
        model = ItemGroup
        
        labels = {
            'ItemGroupName': "Group Name:",
            'GroupShortName': "Short Name:",
            'IsActive': "Is Active:"
           
        }
        fields = ['ItemGroupName','GroupShortName' , 'IsActive' ]
        widgets = {
            'ItemGroupName': forms.TextInput(),
            'GroupShortName': forms.TextInput(),
            'IsActive':forms.CheckboxInput(),
            
        }
        parsley_extras = {
            "ItemGroupName": {
                "required-message": "Group name required",
            },
            "GroupShortName": {
                "required-message": "Group short name required",
            }
        }
    def __init__(self, *args, **kwargs):
        super(ItemGroupForm, self).__init__(*args, **kwargs)
        self.fields['ItemGroupName'].widget.attrs['class'] = 'form-control'
        self.fields['GroupShortName'].widget.attrs['class'] = 'form-control'