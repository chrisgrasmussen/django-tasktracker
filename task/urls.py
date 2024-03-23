from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task/<str:pk>/', views.update_task, name='update_task'),
    path('task/<str:pk>/delete/', views.delete_task, name='delete_task'),
    
    path('register/', views.registerView, name='register'),
    path('login/', views.loginView, name='login'),
    path('user-logout/', views.logoutView, name='user-logout'),
]