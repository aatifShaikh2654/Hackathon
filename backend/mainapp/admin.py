from django.contrib import admin
from .models import Book, Transaction

# Register your models here.
@admin.register(Book)
class ShowBook(admin.ModelAdmin):
    list_display = ['title', 'author', 'year', 'created_at',]

@admin.register(Transaction)
class AdminTransaction(admin.ModelAdmin):
    list_display = ['id']