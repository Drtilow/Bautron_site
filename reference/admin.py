from django.contrib import admin
from .models import Reference

@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('nazev', 'typ')
