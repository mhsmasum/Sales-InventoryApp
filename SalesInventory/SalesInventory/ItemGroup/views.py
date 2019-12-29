from django.shortcuts import render
from datetime import datetime
from .forms import ItemGroupForm
from django.views.generic import View
from django.views.generic import ListView
from .models import ItemGroup
from django.shortcuts import render,get_object_or_404
from django.template.loader import render_to_string

from django.http import HttpRequest,JsonResponse

from django.shortcuts import redirect


def itemGroup_list(request):
    assert isinstance(request, HttpRequest)
    objs = ItemGroup.objects.all().filter(DeletedBy=None)
        # print(ItemCategory.objects.all().filter(deleted_by=None).count())
    return render(request, 'ItemGroup/index.html', {'objs': objs})  

def itemGroup_create(request):
    if request.method == 'POST':
        form = ItemGroupForm(request.POST)
        form.instance.CreatedBy=request.user.username #'Admin'
        form.instance.CreatedDate = datetime.now()
    else:
        form = ItemGroupForm()
    return save_itemGroup_form(request, form, 'ItemGroup/includes/partial_itemGroup_create.html','Save')


def itemGroup_update(request, pk):
    obj = get_object_or_404(ItemGroup, pk=pk)
    if request.method == 'POST':
        obj.UpdatedBy=request.user.username #'Admin'
        obj.UpdatedDate = datetime.now()
        form = ItemGroupForm(request.POST, instance=obj)        
    else:
        form = ItemGroupForm(instance=obj)
    return save_itemGroup_form(request, form, 'ItemGroup/includes/partial_itemGroup_create.html','Update')



def save_itemGroup_form(request, form, template_name, operation_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['data_operation'] = operation_name
            data['form_is_valid'] = True
            objs = ItemGroup.objects.all().filter(DeletedBy=None)
            data['html_list'] = render_to_string('ItemGroup/includes/partial_itemGroup_list.html', {
                    'objs': objs
                })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def itemGroup_delete(request, pk):
    obj = get_object_or_404(ItemGroup, pk=pk)
    data = dict()
    if request.method == 'POST':
        ItemGroup.objects.filter(pk=pk).update(DeletedBy=request.user.username,DeletedDate = datetime.now())
        data['data_operation'] = 'Delete'
        data['form_is_valid'] = True  # This is just to play along with the existing code
        objs = ItemGroup.objects.all().filter(DeletedBy=None)
        data['html_list'] = render_to_string('ItemGroup/includes/partial_itemGroup_list.html', {
            'objs': objs
        })
    else:
        context = {'obj': obj}
        data['html_form'] = render_to_string('ItemGroup/includes/partial_itemGroup_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)
        


