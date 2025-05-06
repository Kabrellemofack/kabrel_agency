from django.contrib import admin
from .models import register

# Register your models here.
@admin.register(register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('name', 'prename', 'email', 'password')
    search_fields = ('name', 'prename', 'email')
    list_filter = ('name', 'prename')
    ordering = ('name',)