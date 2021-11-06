from django.db import models
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder':('Enter your First Name')})
        self.fields['last_name'].widget.attrs.update({'placeholder':('Enter your Last Name')})
        self.fields['email'].widget.attrs.update({'placeholder':('Enter your Email Address')})
        self.fields['username'].widget.attrs.update({'placeholder':('Enter your Medical ID '), 'title': ('Please Medical ID must comprise of 7 digits'), 'pattern': ('^[0-9]{7}$')})
        self.fields['password1'].widget.attrs.update({'placeholder':('Enter your Password')})        
        self.fields['password2'].widget.attrs.update({'placeholder':('Confirm your password')})
        self.fields['password1'].widget.attrs.update({'class':('form-control my-3 p-2'), 'title': ('Please Password must be 8 characters long consisting of at least a small letter, capital letter and number'), 'pattern': ('(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}')}) 
        self.fields['password2'].widget.attrs.update({'class':('form-control my-3 p-2'), 'title': ('Please Password must be 8 characters long consisting of at least a small letter, capital letter and number'), 'pattern': ('(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}')})  

        
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']