from django.urls import path
from . import views


urlpatterns = [
    path('api/users/register/', views.register, name='register'),
    path('api/users/login/', views.login, name='login'),
    path('api/users/me/', views.profile, name='profile')
]
