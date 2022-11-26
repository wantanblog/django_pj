from socket import fromshare
from django import forms

class formAppForm(forms.Form):
    name = forms.CharField(label='name')
    password = forms.CharField(label='password')