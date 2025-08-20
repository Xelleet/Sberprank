from django.urls import path
from . import views


urlpatterns = [
    path('', views.transactions_list, name='transactions_list'),
    path('transfer/', views.create_transfer, name='create_transfer')
]