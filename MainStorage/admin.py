from django.contrib import admin
from .models import *

# Register your models here.
class SaveFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'file_describe', 'time_save', 'time_update')
    search_fields = ('title', 'file_describe')

admin.site.register(SaveFile, SaveFileAdmin)

class NewFileAdmin(admin.ModelAdmin):
    exclude = ('user_id',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user_id = request.user
        super().save_model(request, obj, form, change)