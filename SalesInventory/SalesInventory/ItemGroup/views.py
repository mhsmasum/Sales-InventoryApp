from django.shortcuts import render
from .forms import ItemGroupForm
from django.views.generic import View
from django.views.generic import ListView
from .models import ItemGroup

from django.shortcuts import redirect
# Create your views here.



class ItemGroupList(ListView):
    
    queryset = ItemGroup.objects.all()
    template_name = "ItemGroup/list.html"
    def get_context_data(self,*args ,**kwargs):
       
        pk = self.kwargs.get('pk')
        
        context = super(ItemGroupList,self).get_context_data(*args , **kwargs)
        masterForm = ItemGroupForm(None)
        context['masterForm'] = masterForm
        return  context
        
    def post(self, request):
        masterForm = ItemGroupForm(request.POST)
        name = request.POST.get('ItemGroupName')
        shortname = request.POST.get('GroupShortName')
        auser = ItemGroup(ItemGroupName = name ,GroupShortName = shortname,IsActive = True,IsDelete = False ,CreateBy="Admin"  )
        auser.save()
        masterForm = ItemGroupForm(None)
        queryset = ItemGroup.objects.all()
        context={
            'object_list':queryset,
            'masterForm':masterForm,
        }
        test_view = ItemGroupList.as_view()
        return redirect('/ItemGroup/list')
        


