from django.urls import path
from . import views


urlpatterns = [
    path('', views.accounts_list, name='accounts-list'),
    path('create/', views.create_account, name='create-account'),
    path('<int:account_id>/', views.account_detail, name='account-detail'),
    path('deposit/', views.deposit_account, name='deposit_account'),
]