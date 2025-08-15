from rest_framework import serializers
from .models import Transaction
from accounts.models import Account

class TransactionSerializer(serializers.ModelSerializer):
    from_account_number = serializers.CharField(source='from_account.account_number', read_only=True)
    to_account_number = serializers.CharField(source='to_account.account_number', read_only=True)

    from_user = serializers.CharField(source='from_account.user.username', read_only=True)
    to_user = serializers.CharField(source='from_account.user.username', read_only=True)

    class Meta:
        model = Transaction
        fields = ['id',
                  'from_account',
                  # ID счёта-отправителя (для записи)            'to_account',             # ID счёта-получателя (для записи)
                  'from_account_number',
                  # Номер счёта отправителя (только для чтения)            'to_account_number',      # Номер счёта получателя (чтение)
                  'from_user',  # Логин отправителя            'to_user',                # Логин получателя
                  'amount', 'transaction_type',
                  'status', 'description',
                  'timestamp']
        # При создании транзакции from/to_account обязательны, остальное — автоматически
        extra_kwargs = {
        'from_account': {'required': True}, 'to_account': {'required': True},
        'amount': {'required': True}, }

        def validate(self, data):
            if data['amount'] <= 0:
                raise serializers.ValidationError('Сумма должна быть больше 0.')

            return data