from  django import forms
from .models import ItemCategory
from parsley.decorators import parsleyfy
# from parsley.decorators import parsleyfy
from django.forms  import ModelForm

@parsleyfy
class ItemCategoryForm(ModelForm):
    
    class Meta:
        model = ItemCategory
        
        labels = {
            'itemcategory_title': "Title:",
            'itemcategory_title_bangla': "Title (Bangla): ",
            'isactive':'Status :'
           
        }
        fields = ['itemcategory_title','itemcategory_title_bangla','isactive','created_by','created_date','updated_by','updated_date','deleted_by','deleted_date' ]
        exclude = ('created_by','created_date','updated_by','updated_date','deleted_by','deleted_date')
        widgets = {
            'itemcategory_title': forms.TextInput(),
            'itemcategory_title_bangla': forms.TextInput(),
            'isactive': forms.CheckboxInput(),
            
        }
        parsley_extras = {
            "itemcategory_title": {
                "required-message": "Item Category Title Required",
            }            
        }
    def __init__(self, *args, **kwargs):
        super(ItemCategoryForm, self).__init__(*args, **kwargs)
        self.fields['itemcategory_title'].widget.attrs['class'] = 'form-control'
        self.fields['itemcategory_title_bangla'].widget.attrs['class'] = 'form-control'
        self.fields['isactive'].widget.attrs['class'] = 'iCheck'
            




    
    

