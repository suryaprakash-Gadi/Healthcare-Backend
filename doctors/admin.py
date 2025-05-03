from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'specialization', 'license_number', 'user')
    list_filter = ('specialization', 'gender')
    search_fields = ('first_name', 'last_name', 'license_number', 'specialization')
    date_hierarchy = 'created_at'