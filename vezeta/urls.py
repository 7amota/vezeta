from django.urls import include, path
from . import views
urlpatterns = [
path('' , views.index , name='index'),
path('sign/' , views.sign_up , name='sign'),
path('update_profile/' , views.update_profile , name='update'),
path('myprofile/' , views.my_profile , name='myprofile'),
path('newpost/' , views.new_plugin , name='newplugin'),
path('blugs/' , views.blug_list , name='bluglist'),
path('blugdetail/' , views.blug_detail , name='blugdetail'),
path('login/' , views.login_form , name='login'),
path('<slug:slug>/' , views.doctor_detail , name='doctor_detail')
    
]
