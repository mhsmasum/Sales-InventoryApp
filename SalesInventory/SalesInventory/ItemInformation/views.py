"""
Definition of views.
"""
from datetime import datetime
from django.shortcuts import render,get_object_or_404
from django.template.loader import render_to_string

from django.http import HttpRequest,JsonResponse
from django import forms
from django.forms import ModelForm

from .models import ItemInformation
from .forms import ItemInformationForm

""" Item Category """

def ItemInformation_list(request):
    assert isinstance(request, HttpRequest)
    objs = ItemInformation.objects.all().filter(DeletedBy=None)
    # print(ItemInformation.objects.all().filter(DeletedBy=None).count())
    return render(request, 'ItemInformation/ItemInformation_list.html', {'objs': objs})

def ItemInformation_create(request):
    if request.method == 'POST':
        form = ItemInformationForm(request.POST)
        form.instance.CreatedBy=request.user.username #'Admin'
        form.instance.CreatedDate = datetime.now()
    else:
        form = ItemInformationForm()
    return save_ItemInformation_form(request, form, 'ItemInformation/includes/partial_ItemInformation_create.html','Save')

def save_ItemInformation_form(request, form, template_name, operation_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['data_operation'] = operation_name
            data['form_is_valid'] = True
            objs = ItemInformation.objects.all().filter(DeletedBy=None)
            data['html_list'] = render_to_string('ItemInformation/includes/partial_ItemInformation_list.html', {
                'objs': objs
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def ItemInformation_update(request, pk):
    obj = get_object_or_404(ItemInformation, pk=pk)
    if request.method == 'POST':
        obj.UpdatedBy=request.user.username #'Admin'
        obj.UpdatedDate = datetime.now()
        form = ItemInformationForm(request.POST, instance=obj)        
    else:
        form = ItemInformationForm(instance=obj)
    return save_ItemInformation_form(request, form, 'ItemInformation/includes/partial_ItemInformation_update.html','Update')

def ItemInformation_delete(request, pk):
    obj = get_object_or_404(ItemInformation, pk=pk)
    data = dict()
    if request.method == 'POST':
        ItemInformation.objects.filter(pk=pk).update(DeletedBy=request.user.username,DeletedDate = datetime.now())
        data['data_operation'] = 'Delete'
        data['form_is_valid'] = True  # This is just to play along with the existing code
        objs = ItemInformation.objects.all().filter(DeletedBy=None)
        data['html_list'] = render_to_string('ItemInformation/includes/partial_ItemInformation_list.html', {
            'objs': objs
        })
    else:
        context = {'obj': obj}
        data['html_form'] = render_to_string('ItemInformation/includes/partial_ItemInformation_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)