from django.contrib import admin
from users.models import *
from django.contrib.auth.admin import UserAdmin 
from users.models import User, UserProfile
# Register your models here.

class  CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superadmin','role')
    ordering = ('-date_joined',)
    list_filter = ('is_active', 'is_staff', 'is_superadmin')
    filter_horizontal = ()
    fieldsets = ()
    
    
class CustomUserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address_line1', 'address_line2', 'country', 'state')
    search_fields = ('user__email', 'user__username', 'country', 'state')
    list_filter = ('country', 'state')    
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile, CustomUserProfileAdmin)
