from django.contrib import admin
from django.urls import path
from .views import Books

urlpatterns = [
    path('books/',Books.as_view(),name="books"),

]