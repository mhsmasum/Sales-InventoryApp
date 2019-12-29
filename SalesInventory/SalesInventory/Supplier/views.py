from django.shortcuts import render
from datetime import datetime
from .forms import SupplierForm
from .models import Supplier
from django.shortcuts import render,get_object_or_404
from django.template.loader import render_to_string

from django.http import HttpRequest,JsonResponse

# Create your views here.

def supplier_list(request):
    assert isinstance(request, HttpRequest)
    objs = Supplier.objects.all().filter(DeletedBy=None)
        # print(ItemCategory.objects.all().filter(deleted_by=None).count())
    return render(request, 'Supplier/index.html', {'objs': objs})  

def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        form.instance.CreatedBy=request.user.username #'Admin'
        form.instance.CreatedDate = datetime.now()
    else:
        form = SupplierForm()
    return save_supplier_form(request, form, 'Supplier/includes/partial_supplier_create.html','Save')


def supplier_update(request, pk):
    obj = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        obj.UpdatedBy=request.user.username #'Admin'
        obj.UpdatedDate = datetime.now()
        form = SupplierForm(request.POST, instance=obj)        
    else:
        form = SupplierForm(instance=obj)
    return save_supplier_form(request, form, 'Supplier/includes/partial_supplier_create.html','Update')



def save_supplier_form(request, form, template_name, operation_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['data_operation'] = operation_name
            data['form_is_valid'] = True
            objs = Supplier.objects.all().filter(DeletedBy=None)
            data['html_list'] = render_to_string('Supplier/includes/partial_supplier_list.html', {
                    'objs': objs
                })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def supplier_delete(request, pk):
    obj = get_object_or_404(Supplier, pk=pk)
    data = dict()
    if request.method == 'POST':
        Supplier.objects.filter(pk=pk).update(DeletedBy=request.user.username,DeletedDate = datetime.now())
        data['data_operation'] = 'Delete'
        data['form_is_valid'] = True  # This is just to play along with the existing code
        objs = Supplier.objects.all().filter(DeletedBy=None)
        data['html_list'] = render_to_string('Supplier/includes/partial_supplier_list.html', {
            'objs': objs
        })
    else:
        context = {'obj': obj}
        data['html_form'] = render_to_string('Supplier/includes/partial_supplier_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)
        


