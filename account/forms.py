from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .choices import *
from .models import Profile

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    email = forms.EmailField(max_length=254,  widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    password1 = forms.CharField(max_length=20,label="Password", widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'8+ characters'}))
    password2 = forms.CharField(max_length=20,label="Confirm Password", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Re-enter password'}))
    dept = forms.ChoiceField(choices=COURSES_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2','dept']
      


class UpdateProfileForm(forms.ModelForm):
    age = forms.IntegerField(max_value=50, widget=forms.NumberInput(attrs={'class':'form-control'}))
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    level = forms.ChoiceField(choices=Level, widget=forms.Select(attrs={'class':'signUpForm'}))
    mat_no = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Matric Number'}))


    class Meta:
        model = Profile
        fields = ['age', 'avatar']