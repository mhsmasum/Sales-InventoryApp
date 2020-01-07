"""
Definition of views.
"""
from datetime import datetime
from django.shortcuts import render,get_object_or_404
from django.template.loader import render_to_string

from django.http import HttpRequest,JsonResponse
from django import forms
from django.forms import ModelForm

from .models import UnitofMeasure,UnitofMeasureDetails
from .forms import UnitofMeasureForm,UnitofMeasureDetailsForm
import json
""" Unit of Measure """

def uom_list(request):
    assert isinstance(request, HttpRequest)
    objs = UnitofMeasure.objects.all().filter(DeletedBy=None)
    # print(uom.objects.all().filter(DeletedBy=None).count())
    return render(request, 'uom/uom_list.html', {'objs': objs})

def uom_create(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body.decode("utf-8"))
        form = UnitofMeasureForm(received_json_data['obj'])
        details= received_json_data['obj'].get('UomDetails')
        formdetails = details
    else:
        form = UnitofMeasureForm()
        formdetails = UnitofMeasureDetailsForm()
    return save_uom_form(request, form,formdetails, 'uom/includes/partial_uom_create.html','Save')

def save_uom_form(request, form,formdetails, template_name, operation_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            new_form =form.save(commit=False)
            new_form.CreatedBy = request.user.username
            new_form.CreatedDate=datetime.now()
            new_form.save()
            if operation_name == 'Save':
                for theDetails in formdetails:
                    uomDetails = UnitofMeasureDetails.objects.create(
                        uomid = new_form , 
                        uomdetails_name =theDetails['uomdetails_name'], 
                        uomdetails_shortname = theDetails['uomdetails_shortname'] ,
                        convertionvalue = theDetails['convertionvalue'] ,
                        isbaseuom = theDetails['isbaseuom'] ,
                        CreatedBy=request.user.username,
                        CreatedDate = datetime.now()
                        )
                    uomDetails.save()
            data['data_operation'] = operation_name
            data['form_is_valid'] = True
            objs = UnitofMeasure.objects.all().filter(DeletedBy=None)
            data['html_list'] = render_to_string('uom/includes/partial_uom_list.html', {
                'objs': objs
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form,'formdetails':formdetails}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def uom_update(request, pk):    
    obj = get_object_or_404(UnitofMeasure, pk=pk)
    objDetails = UnitofMeasureDetails.objects.all().filter(uomid=pk)
    if request.method == 'POST':
        data = dict()
        received_json_data = json.loads(request.body.decode("utf-8"))
        json_obj=received_json_data['obj']
        form = UnitofMeasureForm(json_obj)
        unitbasisname = json_obj.get('unitbasisname')
        uom_name = json_obj.get('uom_name')
        uomid = pk #json_obj.get('id')
        uom_shortname = json_obj.get('uom_shortname')
        IsActive = json_obj.get('IsActive')
        UnitofMeasure.objects.filter(pk=int(uomid)).update(
            unitbasisname=unitbasisname,
            uom_name=uom_name,
            uom_shortname=uom_shortname,
            IsActive=IsActive,
            UpdatedBy=request.user.username,
            UpdatedDate = datetime.now())
        uomMaster = UnitofMeasure.objects.get(pk=pk)
        UnitofMeasureDetails.objects.filter(uomid=int(uomid)).delete()
        details= json_obj.get('UomDetails')
        for theDetails in details:
            print(theDetails)
            uomDetails = UnitofMeasureDetails.objects.create(
                uomid = uomMaster , 
                uomdetails_name =theDetails['uomdetails_name'], 
                uomdetails_shortname = theDetails['uomdetails_shortname'] ,
                convertionvalue = theDetails['convertionvalue'] ,
                isbaseuom = theDetails['isbaseuom'] ,
                CreatedBy=request.user.username,
                CreatedDate = datetime.now()
                )
        data['data_operation'] = 'Update'
        data['form_is_valid'] = True
        objs = UnitofMeasure.objects.all().filter(DeletedBy=None)
        data['html_list'] = render_to_string('uom/includes/partial_uom_list.html', {            
            'objs': objs
        })
        context = {'form': form}
        data['html_form'] = render_to_string('uom/uom_list.html', context, request=request)
        return JsonResponse(data)
    else:
        form = UnitofMeasureForm(instance=obj)  
        formdetails= []
        for theDetails in objDetails:
            formdetails+=UnitofMeasureDetailsForm(instance=theDetails)
        return save_uom_form(request, form,formdetails, 'uom/includes/partial_uom_update.html','Update')

def uom_delete(request, pk):
    obj = get_object_or_404(UnitofMeasure, pk=pk)
    data = dict()
    if request.method == 'POST':
        UnitofMeasure.objects.filter(pk=pk).update(
            DeletedBy=request.user.username,
            DeletedDate = datetime.now()
            )
        # objDetails = UnitofMeasureDetails.objects.all().filter(uomid=pk)
        # for theDetails in objDetails:
        #     UnitofMeasureDetails.objects.filter(pk=theDetails.id).update(DeletedBy=request.user.username,deleted_date = datetime.now())
        
        data['data_operation'] = 'Delete'
        data['form_is_valid'] = True  # This is just to play along with the existing code
        objs = UnitofMeasure.objects.all().filter(DeletedBy=None)
        data['html_list'] = render_to_string('uom/includes/partial_uom_list.html', {
            'objs': objs
        })
    else:
        context = {'obj': obj}
        data['html_form'] = render_to_string('uom/includes/partial_uom_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

def uom_delete_details(request):
    received_json_data = json.loads(request.body.decode("utf-8"))
    json_obj=received_json_data['obj']
    details= json_obj.get('UomDetails')[0]
    uomid = details.get('uomid')
    uomdetails_name = details.get('uomdetails_name')
    uomdetails_shortname = details.get('uomdetails_shortname')
    convertionvalue = details.get('convertionvalue')
    isbaseuom = details.get('isbaseuom')
    UnitofMeasureDetails.objects.filter(
        uomid = uomid,
        uomdetails_name =uomdetails_name,
        uomdetails_shortname=uomdetails_shortname,
        convertionvalue=convertionvalue,
        isbaseuom=isbaseuom
        ).update(
            DeletedBy=request.user.username,
            DeletedDate = datetime.now()
            )
    data = dict()
    data['form_is_valid'] = True
    data['data_operation'] = ' Delete '
    return JsonResponse(data)