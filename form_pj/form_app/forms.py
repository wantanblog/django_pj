from socket import fromshare
from django import forms
from.models import test_emps

class EmpsEntryForm(forms.ModelForm):
    class Meta:
        model = test_emps
        fields = ['name','mail','gender','age','birthday']

class SearchForm(forms.Form):
    searchName = forms.CharField(label='name')