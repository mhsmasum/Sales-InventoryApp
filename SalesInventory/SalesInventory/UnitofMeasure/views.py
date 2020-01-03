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
""" Item color """

def uom_list(request):
    assert isinstance(request, HttpRequest)
    objs = UnitofMeasure.objects.all()
    # print(uom.objects.all().filter(deleted_by=None).count())
    return render(request, 'uom/uom_list.html', {'objs': objs})

def uom_create(request):
    
    
    if request.method == 'POST':
        #print(request.POST)
        #data = json.dumps(request.POST)
        received_json_data = json.loads(request.body.decode("utf-8"))
        # print(received_json_data)
        # print(received_json_data['obj'])
        # print(received_json_data['obj'].get('unitbasisname'))
        form = UnitofMeasureForm(received_json_data['obj'])
        #print(form)
        #print(data.obj)
        details= received_json_data['obj'].get('UomDetails')
        #print(details)
        formdetails = details
        
        
    else:
        form = UnitofMeasureForm()
        formdetails = UnitofMeasureDetailsForm()
        #print(formdetails)
    return save_uom_form(request, form,formdetails, 'uom/includes/partial_uom_create.html','Save')

def save_uom_form(request, form,formdetails, template_name, operation_name):
    data = dict()
    #print(request.method)
    if request.method == 'POST':
        #print('save post')
        if form.is_valid():
            new_form =form.save()
            if operation_name == 'Save':
                for theDetails in formdetails:
                    uomDetails = UnitofMeasureDetails.objects.create(
                        uomid = new_form , 
                        uomdetails_name =theDetails['uomdetails_name'], 
                        uomdetails_shortname = theDetails['uomdetails_shortname'] ,
                        convertionvalue = theDetails['convertionvalue'] ,
                        isbaseuom = theDetails['isbaseuom'] ,
                        created_by=request.user.username,
                        created_date = datetime.now()
                        )
                    uomDetails.save()
            elif operation_name == 'Update':
                for theDetails in formdetails:
                    uomDetails = UnitofMeasureDetails.objects.create(
                        uomid = new_form , 
                        uomdetails_name =theDetails['uomdetails_name'], 
                        uomdetails_shortname = theDetails['uomdetails_shortname'] ,
                        convertionvalue = theDetails['convertionvalue'] ,
                        isbaseuom = theDetails['isbaseuom'] ,
                        updated_by=request.user.username,
                        updated_date = datetime.now()
                        )
                    uomDetails.save()
            else :
                for theDetails in formdetails:
                    uomDetails = UnitofMeasureDetails.objects.create(
                        uomid = new_form , 
                        uomdetails_name =theDetails['uomdetails_name'], 
                        uomdetails_shortname = theDetails['uomdetails_shortname'] ,
                        convertionvalue = theDetails['convertionvalue'] ,
                        isbaseuom = theDetails['isbaseuom'] ,
                        deleted_by=request.user.username,
                        deleted_date = datetime.now()
                        )
                    uomDetails.save()       
            
            data['data_operation'] = operation_name
            data['form_is_valid'] = True
            objs = UnitofMeasure.objects.all()
            data['html_list'] = render_to_string('uom/includes/partial_uom_list.html', {
                'objs': objs
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form,'formdetails':formdetails}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def uom_update(request, pk):
    #print(pk)
    #place = UnitofMeasure.objects.filter(pk=int(pk))
    #print(place)
    #uomMaster = UnitofMeasure.objects.get(id=pk)    
    #obj = UnitofMeasureForm( instance = uomMaster)
    
    obj = get_object_or_404(UnitofMeasure, pk=pk)
    #print(obj)
    #print(uomMaster)
    #objDetails = get_object_or_404(UnitofMeasureDetails,uomid=obj)
    #objDetails=UnitofMeasureDetails.objects.get(uomid=pk)    
    objDetails = UnitofMeasureDetails.objects.all().filter(uomid=pk)
    
    # b = UnitofMeasureDetails.objects.all().filter(uomid_id=pk)
    
    #print(objDetails)
    # #objDetails = UnitofMeasure.objects.get(uomid=pk) #UnitofMeasureDetailsForm( instance = unitofMeasureDetails)
    # objDetails=UnitofMeasureDetails.objects.filter(uomid =pk)
    # queryset = UnitofMeasureDetails.objects.filter(uomid =pk)
    #objDetails=get_object_or_404(objDetails,uomid=pk)
    #print(objDetails)
    # bb = list(UnitofMeasureDetails.objects.filter(uomid =pk))
    # print(bb)
    if request.method == 'POST':
        data = dict()
        # obj.updated_by=request.user.username #'Admin'
        # obj.updated_date = datetime.now()
        received_json_data = json.loads(request.body.decode("utf-8"))
        json_obj=received_json_data['obj']
        #print(json_obj)
        form = UnitofMeasureForm(json_obj)
        #print(form)
        unitbasisname = json_obj.get('unitbasisname')
        uom_name = json_obj.get('uom_name')
        uomid = pk #json_obj.get('id')
        uom_shortname = json_obj.get('uom_shortname')
        isactive = json_obj.get('isactive')
        #print(uomid)
        save_master= UnitofMeasure.objects.filter(pk=int(uomid)).update(
            unitbasisname=unitbasisname,
            uom_name=uom_name,
            uom_shortname=uom_shortname,
            isactive=isactive)
        save_data=UnitofMeasure.objects.filter(pk=int(uomid))
        uomMaster = UnitofMeasure.objects.get(pk=pk)    
        obj = UnitofMeasureForm(instance = uomMaster)
        #print(received_json_data)
        # print(received_json_data['obj'])
        #print(received_json_data['obj'].get('id'))
        #form = UnitofMeasureForm(received_json_data['obj'])
        #print(form)
        #print(data.obj)
        UnitofMeasureDetails.objects.filter(uomid=int(uomid)).delete()
        details= json_obj.get('UomDetails')
        #print(details)
        for theDetails in details:
            uomDetails = UnitofMeasureDetails.objects.create(
                uomid = uomMaster , 
                uomdetails_name =theDetails['uomdetails_name'], 
                uomdetails_shortname = theDetails['uomdetails_shortname'] ,
                convertionvalue = theDetails['convertionvalue'] ,
                isbaseuom = theDetails['isbaseuom'] ,
                updated_by=request.user.username,
                updated_date = datetime.now()
                )
            uomDetails.save()
        data['data_operation'] = 'Update'
        data['form_is_valid'] = True
        objs = UnitofMeasure.objects.all()
        data['html_list'] = render_to_string('uom/includes/partial_uom_list.html', {            
            'objs': objs
        })
        context = {'form': form}
        data['html_form'] = render_to_string('uom/uom_list.html', context, request=request)
        return JsonResponse(data)
        #print(formdetails)
        #print('Update post',details)
        #print(get_object_or_404(UnitofMeasure, pk=received_json_data['obj'].get('id'))   )
        #id = received_json_data['obj'].get('id')
        #print(id)
        #obj2 = get_object_or_404(UnitofMeasure, pk=id)    
        # print(obj)
        # form = UnitofMeasureForm(request.POST, instance=obj)
        #print(form)
        # formdetails=UnitofMeasureDetailsForm()
    else:
        #print(objDetails)
        form = UnitofMeasureForm(instance=obj)  
        formdetails= []
        for theDetails in objDetails:
            formdetails+=UnitofMeasureDetailsForm(instance=theDetails)
        #     uomDetails = UnitofMeasureDetails.objects.create(
        #         uomid = save_master , 
        #         uomdetails_name =theDetails['uomdetails_name'], 
        #         uomdetails_shortname = theDetails['uomdetails_shortname'] ,
        #         convertionvalue = theDetails['convertionvalue'] ,
        #         isbaseuom = theDetails['isbaseuom'] ,
        #         updated_by=request.user.username,
        #         updated_date = datetime.now()
        #         )
        #     uomDetails.save()      
            # print(formdetails)
        
        return save_uom_form(request, form,formdetails, 'uom/includes/partial_uom_update.html','Update')

def uom_delete(request, pk):
    obj = get_object_or_404(UnitofMeasureDetails, pk=pk)
    data = dict()
    if request.method == 'POST':
        UnitofMeasureDetails.objects.filter(pk=pk).update(deleted_by=request.user.username,deleted_date = datetime.now())
        data['data_operation'] = 'Delete'
        data['form_is_valid'] = True  # This is just to play along with the existing code
        objs = UnitofMeasure.objects.all().filter(deleted_by=None)
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