"""
Definition of views.
"""
from datetime import datetime
from django.shortcuts import render,get_object_or_404
from django.template.loader import render_to_string

from django.http import HttpRequest,JsonResponse
from django import forms
from django.forms import ModelForm

from .models import ItemBrand
from .forms import ItemBrandForm

""" Item Brand """

def itembrand_list(request):
    assert isinstance(request, HttpRequest)
    objs = ItemBrand.objects.all().filter(deleted_by=None)
    # print(ItemBrand.objects.all().filter(deleted_by=None).count())
    return render(request, 'itembrand/itembrand_list.html', {'objs': objs})

def itembrand_create(request):
    if request.method == 'POST':
        form = ItemBrandForm(request.POST)
        form.instance.created_by=request.user.username #'Admin'
        form.instance.created_date = datetime.now()
    else:
        form = ItemBrandForm()
    return save_itembrand_form(request, form, 'itembrand/includes/partial_itembrand_create.html','Save')

def save_itembrand_form(request, form, template_name, operation_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['data_operation'] = operation_name
            data['form_is_valid'] = True
            objs = ItemBrand.objects.all().filter(deleted_by=None)
            data['html_list'] = render_to_string('itembrand/includes/partial_itembrand_list.html', {
                'objs': objs
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def itembrand_update(request, pk):
    obj = get_object_or_404(ItemBrand, pk=pk)
    if request.method == 'POST':
        obj.updated_by=request.user.username #'Admin'
        obj.updated_date = datetime.now()
        form = ItemBrandForm(request.POST, instance=obj)        
    else:
        form = ItemBrandForm(instance=obj)
    return save_itembrand_form(request, form, 'itembrand/includes/partial_itembrand_update.html','Update')

def itembrand_delete(request, pk):
    obj = get_object_or_404(ItemBrand, pk=pk)
    data = dict()
    if request.method == 'POST':
        ItemBrand.objects.filter(pk=pk).update(deleted_by=request.user.username,deleted_date = datetime.now())
        data['data_operation'] = 'Delete'
        data['form_is_valid'] = True  # This is just to play along with the existing code
        objs = ItemBrand.objects.all().filter(deleted_by=None)
        data['html_list'] = render_to_string('itembrand/includes/partial_itembrand_list.html', {
            'objs': objs
        })
    else:
        context = {'obj': obj}
        data['html_form'] = render_to_string('itembrand/includes/partial_itembrand_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)