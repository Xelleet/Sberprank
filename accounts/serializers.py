from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
        'id',
        'account_number',
        'currency',
        'balance',
        'is_active',
        'created_at'
        ]
        read_only_fields = [
        'account_number',
        'balance',
        'is_active',
        'created_at'
        ]

class CreateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['user', 'currency']
        extra_kwargs = {
            'user': {'read_only': True}
        }