from django.contrib import admin
from .models import *
# Register your models here.
class ProfileModel(admin.ModelAdmin):
    model = Profile
    list_display = ('id','name')
    
admin.site.register(Profile,ProfileModel)
admin.site.register(NewPost)
admin.site.register(Appointmentdef)