from .models import Loan, LoanPayment
from accounts.models import Account
from rest_framework import serializers

class LoanPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanPayment
        fields = ['id', 'loan', 'amount', 'due_date', 'paid_date', 'is_paid']
        read_only_fields = ['loan']

class LoanSerializer(serializers.ModelSerializer):
    account_number = serializers.CharField(source='account.account_number', read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)
    payments = LoanPaymentSerializer(many=True, read_only=True)

    class Meta:
        model = Loan
        fields = [
            'id',
            'user',  # ID пользователя (авто-подставится)
            'user_username',  # Логин (только для чтения)
            'account',  # ID счёта для списаний
            'account_number',  # Номер счёта (чтение)
            'amount',
            'interest_rate',
            'term_months',
            'start_date',
            'end_date',
            'monthly_payment',
            'status',
            'remaining_balance',
            'payments',  # Все платежи по кредиту
        ]
        read_only_fields = [
            'start_date',
            'end_date',
            'monthly_payment',
            'status',
            'remaining_balance',
        ]

    def create(self, validated_data):
        # При создании кредита статус — "На рассмотрении"
        loan = Loan.objects.create(
            status='pending',
            **validated_data
        )
        return loan