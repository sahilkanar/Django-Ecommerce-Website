from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import *


class Registrationform(UserCreationForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text=''
        self.fields['password1'].help_text=''
        self.fields['password2'].help_text=''
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
        widgets={
            'username':forms.TextInput(attrs={"class":"form-control"}),
            'first_name':forms.TextInput(attrs={"class":"form-control"}),
            'last_name':forms.TextInput(attrs={"class":"form-control"}),
            'email':forms.EmailInput(attrs={"class":"form-control"}),
            'password1':forms.PasswordInput(attrs={"class":"form-control"}),
            'password2':forms.PasswordInput(attrs={"class":"form-control"})

        }
    

class Loginform(AuthenticationForm):
    class Meta:
        model=User
        fields = ['username','password']


class Updateform(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields = ['email','first_name','last_name']

class Productform:
    class Meta:
        model=Products
        fields='__all__'




       