from django.contrib import admin
from users.models import *
from django.contrib.auth.admin import UserAdmin 
# Register your models here.

class  CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superadmin','role')
    ordering = ('-date_joined',)
    list_filter = ('is_active', 'is_staff', 'is_superadmin')
    filter_horizontal = ()
    fieldsets = ()
admin.site.register(User, CustomUserAdmin)
