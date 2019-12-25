from  django import forms
from .models import *
from parsley.decorators import parsleyfy
# from parsley.decorators import parsleyfy
from django.forms  import ModelForm

@parsleyfy
class RegistrationForm(ModelForm):
    
    class Meta:
        model = AppUser
        
        labels = {
            'AppUserName': "User Name:",
            'AppUserPassword': "Password: "
           
        }
        fields = ['AppUserName','AppUserPassword' ]
        widgets = {
            'AppUserName': forms.TextInput(),
            'AppUserPassword': forms.TextInput(),
            
        }
        parsley_extras = {
            "AppUserName": {
                "required-message": "User Name Required",
            },
            "AppUserPassword": {
                "required-message": "Password Required",
            }
        }
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['AppUserName'].widget.attrs['class'] = 'form-control'
        self.fields['AppUserPassword'].widget.attrs['class'] = 'form-control'
            




    
    
