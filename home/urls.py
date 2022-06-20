from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('questions/', views.QuestionsApi.as_view(), name='questions_api'),
    path('questions/create/', views.QuestionCreateApi.as_view(), name='question_create_api'),
    path('questions/get/<int:pk>/', views.QuestionGetApi.as_view(), name='question_get_api'),
    path('questions/delete/<int:pk>/', views.QuestionDeleteApi.as_view(), name='question_delete_api'),
    path('questions/update/<int:pk>/', views.QuestionUpdateApi.as_view(), name='question_update_api'),
]