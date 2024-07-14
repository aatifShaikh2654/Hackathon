from django.contrib import admin
from django.urls import path
from .views import Books
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('books/',Books.as_view(),name="books"),
    path("getBook/",views.getBook,name="getBook"),
    path("getBooksByUser/",views.GetAllBooksByUser,name="getBooksByUser"),
    path("checkoutBook/",views.checkoutBook,name="checkoutBook"),
    path("returnBook/",views.returnBook,name="returnBook"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
