from django.urls import path
from . import views


urlpatterns = [
    path('apply/', views.apply_for_loan, name='apply_for_loan'),
    path('', views.my_loans, name='my_loans'),
    path('<int:loan_id>/', views.loan_detail, name='loan_detail'),
    path('int:loan_id/pay/', views.make_loan_payment, name='male_loan_payment')
]