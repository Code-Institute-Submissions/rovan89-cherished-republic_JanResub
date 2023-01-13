from django.contrib import admin
from .models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ Profile admin registration """
    list_display = ('id', 'user', 'first_name')
    
