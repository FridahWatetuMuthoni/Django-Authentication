from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile

# Register your models here.

class CustomUserAdmin(UserAdmin):
    #list_display = ('username','first_name', 'last_name', 'email','bio','is_staff')
    fieldsets = (
        (None,{'fields':('username','password','first_name', 'last_name', 'email','bio','is_staff','date_joined','last_login', 'is_active', 'is_superuser','groups','user_permissions',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Profile)


#Admin Customazation
admin.site.site_title = 'Django Authentication'
admin.site.site_header = 'Django Authentication'
admin.site.index_title = 'Django Authentication Administration Site'