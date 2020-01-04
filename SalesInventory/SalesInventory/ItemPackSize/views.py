from django.shortcuts import render
from datetime import datetime
from .forms import ItemPackSizeForm
from .models import ItemPackSize
from django.shortcuts import render,get_object_or_404
from django.template.loader import render_to_string

from django.http import HttpRequest,JsonResponse

from django.shortcuts import redirect


def packsize_list(request):
    assert isinstance(request, HttpRequest)
    objs = ItemPackSize.objects.all().filter(DeletedBy=None)
        # print(ItemCategory.objects.all().filter(deleted_by=None).count())
    return render(request, 'ItemPackSize/index.html', {'objs': objs})  

def packsize_create(request):
    if request.method == 'POST':
        form = ItemPackSizeForm(request.POST)
        form.instance.CreatedBy=request.user.username #'Admin'
        form.instance.CreatedDate = datetime.now()
    else:
        form = ItemPackSizeForm()
    return save_packsize_form(request, form, 'ItemPackSize/includes/partial_packSize_create.html','Save')


def packsize_update(request, pk):
    obj = get_object_or_404(ItemPackSize, pk=pk)
    if request.method == 'POST':
        obj.UpdatedBy=request.user.username #'Admin'
        obj.UpdatedDate = datetime.now()
        form = ItemPackSizeForm(request.POST, instance=obj)        
    else:
        form = ItemPackSizeForm(instance=obj)
    return save_packsize_form(request, form, 'ItemPackSize/includes/partial_packSize_create.html','Update')



def save_packsize_form(request, form, template_name, operation_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['data_operation'] = operation_name
            data['form_is_valid'] = True
            objs = ItemPackSize.objects.all().filter(DeletedBy=None)
            data['html_list'] = render_to_string('ItemPackSize/includes/partial_packSize_list.html', {
                    'objs': objs
                })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def packsize_delete(request, pk):
    obj = get_object_or_404(ItemGroup, pk=pk)
    data = dict()
    if request.method == 'POST':
        ItemGroup.objects.filter(pk=pk).update(DeletedBy=request.user.username,DeletedDate = datetime.now())
        data['data_operation'] = 'Delete'
        data['form_is_valid'] = True  # This is just to play along with the existing code
        objs = ItemGroup.objects.all().filter(DeletedBy=None)
        data['html_list'] = render_to_string('ItemPackSize/includes/partial_packSize_list.html', {
            'objs': objs
        })
    else:
        context = {'obj': obj}
        data['html_form'] = render_to_string('ItemPackSize/includes/partial_itemGroup_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)
        


