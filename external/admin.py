"""Imagetext admin."""
from django.contrib import admin

class ItemAdmin(admin.ModelAdmin):
    """Admin panel for External Quiz."""

    list_display = ['id', 'image', 'text']
    search_fields = ['id', 'text']
