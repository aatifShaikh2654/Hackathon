from django.contrib import admin
from django.urls import path
from .views import Books
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('books/',Books.as_view(),name="books"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
