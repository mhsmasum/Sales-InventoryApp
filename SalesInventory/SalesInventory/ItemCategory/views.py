"""
Definition of views.
"""
from datetime import datetime
from django.shortcuts import render,get_object_or_404
from django.template.loader import render_to_string

from django.http import HttpRequest,JsonResponse
from django import forms
from django.forms import ModelForm

from .models import ItemCategory
from .forms import ItemCategoryForm

""" Item Category """

def itemcategory_list(request):
    assert isinstance(request, HttpRequest)
    objs = ItemCategory.objects.all().filter(DeletedBy=None)
    # print(ItemCategory.objects.all().filter(DeletedBy=None).count())
    return render(request, 'itemcategory/itemcategory_list.html', {'objs': objs})

def itemcategory_create(request):
    if request.method == 'POST':
        form = ItemCategoryForm(request.POST)
        form.instance.CreatedBy=request.user.username #'Admin'
        form.instance.CreatedDate = datetime.now()
    else:
        form = ItemCategoryForm()
    return save_itemcategory_form(request, form, 'itemcategory/includes/partial_itemcategory_create.html','Save')

def save_itemcategory_form(request, form, template_name, operation_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['data_operation'] = operation_name
            data['form_is_valid'] = True
            objs = ItemCategory.objects.all().filter(DeletedBy=None)
            data['html_list'] = render_to_string('itemcategory/includes/partial_itemcategory_list.html', {
                'objs': objs
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def itemcategory_update(request, pk):
    obj = get_object_or_404(ItemCategory, pk=pk)
    if request.method == 'POST':
        obj.UpdatedBy=request.user.username #'Admin'
        obj.UpdatedDate = datetime.now()
        form = ItemCategoryForm(request.POST, instance=obj)        
    else:
        form = ItemCategoryForm(instance=obj)
    return save_itemcategory_form(request, form, 'itemcategory/includes/partial_itemcategory_update.html','Update')

def itemcategory_delete(request, pk):
    obj = get_object_or_404(ItemCategory, pk=pk)
    data = dict()
    if request.method == 'POST':
        ItemCategory.objects.filter(pk=pk).update(DeletedBy=request.user.username,DeletedDate = datetime.now())
        data['data_operation'] = 'Delete'
        data['form_is_valid'] = True  # This is just to play along with the existing code
        objs = ItemCategory.objects.all().filter(DeletedBy=None)
        data['html_list'] = render_to_string('itemcategory/includes/partial_itemcategory_list.html', {
            'objs': objs
        })
    else:
        context = {'obj': obj}
        data['html_form'] = render_to_string('itemcategory/includes/partial_itemcategory_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)