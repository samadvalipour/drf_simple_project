from rest_framework.authtoken import views as auth_token
from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.UserRegitrations.as_view(), name='user_register'),
    path('all/', views.GetAllUsers.as_view(), name='all_user'),
    path('api-token-auth/', auth_token.obtain_auth_token)
]