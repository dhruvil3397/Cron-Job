from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
from django.contrib.auth.models import User

# Register your models here.
class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User_Profile'

    

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    list_display = ['id','username','first_name','last_name','is_staff']
    


admin.site.unregister(User)
admin.site.register(User,CustomUserAdmin)