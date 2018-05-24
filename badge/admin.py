from django.contrib.auth.models import Group
from django.utils.html import format_html
from django.contrib import admin

from .utils import download_pdf, render_to_pdf
from .models import Employee
from datetime import datetime, timedelta

admin.site.disable_action('delete_selected')
admin.site.unregister(Group)

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'employee_id', 
        'name', 
        'id_no', 
        'position',
        'custom_actions'
    )
    list_display_links = (
        'employee_id', 
        'name', 
        'id_no'
    )
    search_fields = (
        'surname', 
        'other_names', 
        'id_no', 
        'position'
    )
    actions = ['download_card']

    def name(self, obj):
        return obj.other_names + ' ' + obj.surname

    def custom_actions(self, obj):
        return format_html('<a class="button" href="#">Preview</a>&nbsp;<a class="button" href="#">Download</a>')
    custom_actions.short_description = 'Actions'
    custom_actions.allow_tags = True

    def download_card(self, request, queryset):      
        for info in queryset:
            data = {
                "employee_name": info.other_names + ' ' + info.surname,
                "id_no": info.id_no,
                "position": info.position,
                "photo": info.photo,
                "expiry_date" : datetime.now()+timedelta(days=365)
            }
            file = download_pdf(data, request)
            return file
        
    
    download_card.short_description = 'Download card for selected employees' 