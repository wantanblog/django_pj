from ast import If, Param
from unittest import result
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import test_emps
from form_app.forms import EmpsEntryForm
from .forms import SearchForm,EmpsEntryForm
# Create your views here.

# ホーム画面初期処理
def index(request):
    return render(request, "form_apps/index.html")

# 登録画面初期処理
def entryInit(request):
    form = EmpsEntryForm()
    return render(request, "form_apps/entry.html",{'empsEntryForm': form})

# 登録画面登録処理
def entry(request):
    # インスタンス生成
    obj = test_emps()
    emp = EmpsEntryForm(request.POST,instance=obj)

    # DB登録処理
    emp.save()
    # ホーム画面にリダイレクト
    return redirect(to='/testemps/home')

# 検索画面初期処理
def refer(request):
    print('referMethod')
    datas = test_emps.objects.all()
    params = {
        'form':SearchForm(),
        'data':datas,
    }
    print(datas)
    return render(request,'form_apps/refer.html',params)

# 検索画面検索処理
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

# 編集画面初期処理
def editInit(request,num):
    obj = test_emps.objects.get(id=num)
    params = {
        'id':num,
        'editform':EmpsEntryForm(instance=obj)
    }
    return render(request,'form_apps/edit.html',params)

# 編集画面更新処理
def edit(request,num):
    # インスタンス生成
    obj = test_emps.objects.get(id=num)
    emp = EmpsEntryForm(request.POST,instance=obj)

    # DB登録処理
    emp.save()
    # 参照画面にリダイレクト
    return redirect(to='/testemps/refer')

# 編集画面削除処理
def delete(request,num):
    # インスタンス生成
    obj = test_emps.objects.get(id=num)
    # DB登録処理
    obj.delete()
    # ホーム画面にリダイレクト
    return redirect(to='/testemps/refer')