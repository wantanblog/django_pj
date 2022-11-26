from ast import If, Param
from unittest import result
from django.shortcuts import render
from django.http import HttpResponse

from form_app.forms import formAppForm
# Create your views here.

def index(request):
    f = formAppForm()
    param = {
        'sub_title':'',
        'name':'',
        'password':''
    }
    return render(request, "form_apps/index.html" ,{'formAppForm': f,'param':param})

def form(request):
    name = request.POST['name']
    password = request.POST['password']
    f = formAppForm({
        'name':name,
        'password':password,
        })
    param = {
        'sub_title':'form_date',
        'name':'name:' + name,
        'password':'password:' + password
    }
    return render(request, "form_apps/index.html",{'formAppForm': f,'param':param})


