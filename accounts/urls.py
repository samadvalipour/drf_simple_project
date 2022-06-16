from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.UserRegitrations.as_view(), name='user_register'),
    path('all/', views.GetAllUsers.as_view(), name='all_user'),
]