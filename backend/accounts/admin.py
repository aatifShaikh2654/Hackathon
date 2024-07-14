from django.contrib import admin
from .models import CustomUser, Address

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['id']