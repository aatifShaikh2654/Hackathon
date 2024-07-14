from django.contrib import admin
from django.urls import path, include
from accounts import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/',views.signup,name='signup'),
    path('getUser/',views.get_user,name='get_data'),
    path('getAllUser/',views.getAllUser,name='getAllUsers'),
    path('profile/',views.profile,name='profile'),
    path("getAllAddresses/", views.getAllAddresses, name="getAllAddresses"),
    path("addAddress/", views.addAddress, name="addAddress"),
    path("updateAddress/", views.updateAddress, name="updateAddress"),
    path("deleteAddress/<int:id>/", views.deleteAddress, name="deleteAddress"),
    path("",include("mainapp.urls"))

] + static(settings.MEDIA_URL, docummen_root=settings.MEDIA_ROOT)