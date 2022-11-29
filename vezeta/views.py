from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    profile =   User.objects.all()
    context = {
            'profile' : profile
    }
    return render(request , 'pages/doctorlist.html' , context )
def doctor_detail(request , slug):
    search = Profile.objects.all()
    title = None
    if 'search_name' in request.GET:
            title = request.GET['search_name']
            if title:
                    search = search.filter(title__icontains = title)
            
    doctor_detail = Profile.objects.get(slug = slug)
    context = {
            'doctor_detail' : doctor_detail,
            'search' : search
    }
    return render(request , 'pages/doctors_detail.html' , context )

def login_form(request):
        form = Login()
        if request.method == 'POST':
                form = Login()
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request , username=username  , password=password)
                if user:
                        login(request , user)
                        return redirect('/')
                else:
                        form = Login()


        context = {'form' : form}
        return render( request ,'pages/login.html', context )
@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('/')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'pages/update_profile.html', {'user_form': user_form, 'profile_form': profile_form})
def sign_up(request):
        if request.method == 'POST':
              sign = UserCreationForms(request.POST)
              if sign.is_valid():
                      user = sign.save()
                      login(request , user)
                      messages.success(request, "Registration successful." )

                      username = sign.cleaned_data.get('username')
                      password = sign.cleaned_data.get('password1')
                      users = authenticate(request , username=username  , password=password)
                      return redirect('/')
                      
                                
                        
                        
        else:
                sign = UserCreationForms()
        return render(request ,'pages/sign_up.html' , {
                'sign' : sign
        } )
@login_required(login_url='login')
def my_profile(request):
       
                return render(request ,'pages/myprofile.html' )

def new_plugin(request):
        form = New_Plugin()
        if request.method == 'POST':
                form =  New_Plugin(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect('/')
                

        return render(request , 'pages/new_plugin.html', {
                'plugin' : form
        })

def blug_list(request):
        blug = NewPost.objects.all()
        context = {
                'blug' : blug
        }
        
        return render(request , 'pages/blug_list.html', context )
def blug_detail(request):
        return render(request , 'pages/blug_detail.html' )