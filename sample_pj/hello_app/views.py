from ast import If, Param
from unittest import result
from django.shortcuts import render
from django.http import HttpResponse

from hello_app.forms import helloAppForm

def index(request):
    params = {
        'name':'',
        'password':'',
        'form':helloAppForm()
    }
    if(request.method == 'POST'):
        params['name'] = 'name:' + request.POST.get('name')
        params['password'] = 'password:' + request.POST.get('password')
        params['form'] = helloAppForm(request.POST)

    return render(request, "hello_app/index.html",params)

def form(request):

    params = {
        'name':'',
        'password':'',
        'form':helloAppForm()
    }
    return render(request, "hello_app/index.html",params)

def message(request,msg):
    result = "message: " + msg
    return HttpResponse(result)