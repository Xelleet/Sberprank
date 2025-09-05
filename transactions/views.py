from decimal import Decimal, InvalidOperation

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, serializers
from .models import Transaction
from .serializers import TransactionSerializer
from accounts.models import Account


EXCHANGE_RATES = {
    ('RUB', 'USD'): 90.0,
    ('RUB', 'EUR'): 100.0,
    ('USD', 'RUB'): 91.0,
    ('EUR', 'RUB'): 102.0
}

TRANSFER_FEE_PERCENT = 1.0

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def transactions_list(request):
    user_accounts = Account.objects.filter(user=request.user)
    transactions = Transaction.objects.filter(from_account__in=user_accounts) | Transaction.objects.filter(to_account__in=user_accounts)
    transactions = transactions.order_by('-timestamp')
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_transfer(request):
    from_account_id = request.data.get('from_account_id')
    to_account_id = request.data.get('to_account_id')
    amount_str = request.data.get('amount')
    description = request.data.get('description', '')

    if not all([from_account_id, to_account_id, amount_str]):
        return Response(
            {"error": "Укажите from_account_id, to_account_id и amount"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        amount = Decimal(amount_str)
        if amount <= 0:
            return Response(
                {"error": "Сумма должна быть больше 0"},
                status=status.HTTP_400_BAD_REQUEST
            )
    except (ValueError, InvalidOperation):
        return Response(
            {"error": "Некорректная сумма"},
            status=status.HTTP_400_BAD_REQUEST
        )

    from_account = get_object_or_404(Account, id=from_account_id, user=request.user)
    to_account = get_object_or_404(Account, id=to_account_id)

    # === Логика перевода между валютами ===
    fee = amount * Decimal(TRANSFER_FEE_PERCENT / 100)
    fee = int(fee)
    amount_after_fee = amount - fee
    amount_after_fee = float(amount_after_fee)

    if from_account.currency == to_account.currency:
        # Простой перевод
        received_amount = amount_after_fee
        exchange_rate = None
    else:
        # Конвертация
        rate_key = (from_account.currency, to_account.currency)
        rate = Decimal(EXCHANGE_RATES.get(rate_key))

        if not rate:
            return Response(
                {"error": f"Нет курса для перевода {from_account.currency} → {to_account.currency}"},
                status=status.HTTP_400_BAD_REQUEST
            )

        received_amount = amount_after_fee / rate
        exchange_rate = float(rate)

    # Проверка баланса
    if from_account.balance < amount:
        return Response(
            {"error": "Недостаточно средств"},
            status=status.HTTP_400_BAD_REQUEST
        )
    from django.db import transaction
    # Атомарная транзакция
    with transaction.atomic():
        # Списание в валюте отправителя
        from_account.balance -= amount
        from_account.save()

        # Зачисление в валюте получателя
        to_account.balance += Decimal(received_amount)
        to_account.save()

        # Создание транзакции
        transaction = Transaction.objects.create(
            from_account=from_account,
            to_account=to_account,
            amount=amount,
            received_amount=received_amount,  # новое поле
            transaction_type='transfer',
            status='completed',
            description=description,
            fee=fee,
            exchange_rate=exchange_rate,
        )

    # Возвращаем данные
    return Response({
        "message": "Перевод выполнен",
        "sent": f"{amount} {from_account.currency}",
        "fee": f"{fee} {from_account.currency}",
        "received": f"{received_amount:.2f} {to_account.currency}",
        "exchange_rate": exchange_rate,
        "transaction_id": transaction.id,
    }, status=status.HTTP_201_CREATED)

