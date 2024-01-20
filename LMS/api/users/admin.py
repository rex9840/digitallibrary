from django.contrib import admin
from .models import *



@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ['ID','email','first_name','last_name','age','address','phone_number','school_id','is_teacher','is_admin','profile_pic']
    exclude = ['ID']

