from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('api/login/', views.login, name='login'),
    path('api/signup/',views.signup,name='signup'),
    path('api/get_user/',views.get_user,name='get_data'),
    path('api/profile/',views.profile,name='profile'),
    path("api/getAllAddresses/", views.getAllAddresses, name="getAllAddresses"),
    path("api/addAddress/", views.addAddress, name="addAddress"),
    path("api/updateAddress/", views.updateAddress, name="updateAddress"),
    path("api/deleteAddress/<int:id>/", views.deleteAddress, name="deleteAddress"),

]