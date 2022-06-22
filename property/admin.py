from django.contrib import admin

from .models import Flat, Complaint


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('owner', 'town', 'address')
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ['new_building']
    list_filter = ('has_balcony', 'new_building', 'rooms_number')

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'complaint_flat']    

admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
