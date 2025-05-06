from django.contrib import admin
from .models import Register


# Register your models here.
@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('name', 'prename', 'email', 'password')
    search_fields = ('name', 'prename', 'email')
    list_filter = ('name', 'prename')
    ordering = ('name',)