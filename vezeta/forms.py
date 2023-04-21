from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class UserCreationForms(UserCreationForm):
    username = forms.CharField(label='اسم المستخدم')
    email = forms.CharField(label='ألبريد')
    first_name = forms.CharField(label='الاسم الاول')
    last_name = forms.CharField(label='الاسم الاخير')
    password1 = forms.CharField(label='كلمة المرور' , widget=forms.PasswordInput)
    password2 = forms.CharField(label='تكرار كلمة المرور', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )



class Login(forms.ModelForm):
    username = forms.CharField(label='اسم المستخدم')
    password = forms.CharField(label='كلمة المرور' , widget= forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username' , 'password')
        
class UpdateUserForm(forms.ModelForm):
    email = forms.CharField(label='ألاميل الالكتروني')
    first_name = forms.CharField(label='ألاسم الاول')
    last_name = forms.CharField(label='ألاسم الاخير')
    class Meta:
        model = User
        fields = ('first_name' , 'last_name' , 'email')

class UpdateProfileForm(forms.ModelForm):
    name = forms.CharField(label='الاسم بالكامل')
    
    class Meta:
        model = Profile
        fields = (
         'name',
         'address',
         'subtitle',
         'who_i',
         'price',
         'number_phone',
         'working_hours',
         'waiting_time',
         'facebook',
         'twitter',
         'google',
         'gender',
        'Specialization',
        'image'
        )
class New_Plugin(forms.ModelForm):
    class Meta:
        model = NewPost
        fields = (
            'title_plugin',
            'plugin',
            'img'
        )

class Appointmentform(forms.ModelForm):
    class Meta:
        model = Appointmentdef
        fields = (
            'name',
            'phone',
            'gmail',
        )