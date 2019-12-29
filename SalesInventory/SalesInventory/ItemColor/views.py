"""
Definition of views.
"""
from datetime import datetime
from django.shortcuts import render,get_object_or_404
from django.template.loader import render_to_string

from django.http import HttpRequest,JsonResponse
from django import forms
from django.forms import ModelForm

from .models import ItemColor
from .forms import ItemColorForm

""" Item color """

def itemcolor_list(request):
    assert isinstance(request, HttpRequest)
    objs = ItemColor.objects.all().filter(deleted_by=None)
    # print(Itemcolor.objects.all().filter(deleted_by=None).count())
    return render(request, 'itemcolor/itemcolor_list.html', {'objs': objs})

def itemcolor_create(request):
    if request.method == 'POST':
        form = ItemColorForm(request.POST)
        form.instance.created_by=request.user.username #'Admin'
        form.instance.created_date = datetime.now()
    else:
        form = ItemColorForm()
    return save_itemcolor_form(request, form, 'itemcolor/includes/partial_itemcolor_create.html','Save')

def save_itemcolor_form(request, form, template_name, operation_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['data_operation'] = operation_name
            data['form_is_valid'] = True
            objs = ItemColor.objects.all().filter(deleted_by=None)
            data['html_list'] = render_to_string('itemcolor/includes/partial_itemcolor_list.html', {
                'objs': objs
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def itemcolor_update(request, pk):
    obj = get_object_or_404(ItemColor, pk=pk)
    if request.method == 'POST':
        obj.updated_by=request.user.username #'Admin'
        obj.updated_date = datetime.now()
        form = ItemColorForm(request.POST, instance=obj)        
    else:
        form = ItemColorForm(instance=obj)
    return save_itemcolor_form(request, form, 'itemcolor/includes/partial_itemcolor_update.html','Update')

def itemcolor_delete(request, pk):
    obj = get_object_or_404(ItemColor, pk=pk)
    data = dict()
    if request.method == 'POST':
        ItemColor.objects.filter(pk=pk).update(deleted_by=request.user.username,deleted_date = datetime.now())
        data['data_operation'] = 'Delete'
        data['form_is_valid'] = True  # This is just to play along with the existing code
        objs = ItemColor.objects.all().filter(deleted_by=None)
        data['html_list'] = render_to_string('itemcolor/includes/partial_itemcolor_list.html', {
            'objs': objs
        })
    else:
        context = {'obj': obj}
        data['html_form'] = render_to_string('itemcolor/includes/partial_itemcolor_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)