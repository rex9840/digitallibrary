from django.contrib import admin
from .models import *



@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','email','first_name','last_name','age','address','phone_number','is_admin','profile_pic']
    exclude = ['id']
    list_filter  =['id','email','phone_number','is_admin']


@admin.register(UserResourceInteraction)
class UserResourceInteractionAdmin(admin.ModelAdmin):
    list_display = ['user_id','resource_id','resource_name','rating']
    list_filter =['user_id','resource_id','rating']

    user_name = lambda self, obj: obj.user_id.first_name + " " + obj.user_id.last_name
    user_name.short_description = 'User Name'


    resource_name = lambda self, obj: obj.resource_id.name
    resource_name.short_description = 'Resource Name'

