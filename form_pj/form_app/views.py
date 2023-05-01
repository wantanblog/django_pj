from ast import If, Param
from unittest import result
from django.shortcuts import render
from django.http import HttpResponse
from .models import test_emps
from form_app.forms import formAppForm
from .forms import SearchForm
# Create your views here.

def index(request):
    return render(request, "form_apps/index.html")

def entry(request):
    f = formAppForm()
    return render(request, "form_apps/entry.html",{'formAppForm': f})

def refer(request):
    print('referMethod')
    datas = test_emps.objects.all()
    params = {
        'form':SearchForm(),
        'data':datas,
    }
    print(datas)
    return render(request,'form_apps/refer.html',params)

def search(request):
    searchName = request.POST.get('searchName')
    datas = test_emps.objects.filter(name__contains=searchName)
    params = {
        'form':SearchForm(request.POST),
        'data':datas
    }
    print('searchMethod')
    print(datas)
    return render(request,'form_apps/refer.html',params)