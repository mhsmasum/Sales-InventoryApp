from django.shortcuts import render
from .forms import *
from django.views.generic import View
# Create your views here.

def index(request):
    return render(request , 'home/index.html',{'title':'Home Index'} )

def signup(request):

    masterForm = RegistrationForm( None)
    context = {
        'masterForm':masterForm,
        
    }
    
    return render(request, 'home/signup.html', context)

class SignupClass(View):

    def post(self, request):
        masterForm = RegistrationForm(request.POST)
        userName = request.POST.get('AppUserName')
        password = request.POST.get('AppUserPassword')
        print(request.POST)
        print(userName)

        auser = AppUser(AppUserName = userName ,AppUserPassword = password )
        auser.save()
        masterForm = RegistrationForm( None)
       
        return render(request,  'home/signup.html', {'masterForm': masterForm})
    def get(self, request):
        masterForm = RegistrationForm( None)
        return render(request,  'home/signup.html', {'masterForm': masterForm})
    