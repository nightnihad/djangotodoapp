from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets
class RegisterForm(UserCreationForm):
    # username=forms.CharField(widget=forms.TextInput(attrs={'class:field'}))
    password1=forms.CharField(label='parol',widget=forms.PasswordInput())
    password2=forms.CharField(label='parol tesdiqle',widget=forms.PasswordInput())

    class Meta(UserCreationForm.Meta):
        model=User
        fields = ['password1','password2','username']

class LoginForm(forms.Form):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'fields'}))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'fields'}))