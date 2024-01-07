from django.contrib import admin
from .models import *

# Register your models here.


#admin.site.register([User,Role])

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('ID','DateCreated','UserID','Name','Email','Password','Address','display_role','display_Rolename')
    fields = ('Name','Email','Password','Address','Role_id')



@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('RoleID','RoleName','Description')

