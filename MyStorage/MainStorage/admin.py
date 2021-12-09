from django.contrib import admin
from .models import *

# Register your models here.
class SaveFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'file_describe', 'time_save', 'time_update')
    search_fields = ('title', 'file_describe')

admin.site.register(SaveFile, SaveFileAdmin)