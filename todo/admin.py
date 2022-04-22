from django.contrib import admin
from .models import ToDoList
from django_summernote.admin import SummernoteModelAdmin

@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):

    list_display = ('title', 'status', 'created_on')
    summernote_fields = ('content')

