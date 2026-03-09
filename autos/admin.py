from django.contrib import admin
from .models import Auto


@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ['marca', 'modelo', 'año', 'precio']
    list_filter = ['marca', 'año']
    search_fields = ['marca', 'modelo']
