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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def transactions_list(request):
    user_accounts = Account.objects.filter(user=request.user)
    transactions = Transaction.objects.filter(from_account__in=user_accounts) | Transaction.objects.filter(to_account_in=user_accounts)
    transactions = transactions.order_by('-timestamp')
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_transfer(request):
    from_account_id = request.data.get('from_account_id')
    to_account_id = request.data.get('to_account_id')
    amount = request.data.get('amount')
    description = request.data.get('description', "")


    if not all([from_account_id, to_account_id, amount]):
        return Response(
            {"error": "Необходимо указать from_account_id, to_account_id и amount"},
            status=status.HTTP_400_BAD_REQUEST
        )
    from_account = get_object_or_404(Account, id=from_account_id, user=request.user)
    to_account = get_object_or_404(Account, id=to_account_id)

    try:
        amount = Decimal(amount)
        if amount <= 0:
            return Response(
                {"error": "Сумма должна быть больше 0."},
                status=status.HTTP_400_BAD_REQUEST
            )
        amount = amount.quantize(Decimal('0.01'))
    except (ValueError, TypeError, InvalidOperation):
        return Response(
            {"error": "Некорректная сумма."},
            status=status.HTTP_400_BAD_REQUEST
        )

    if from_account.balance <= amount:
        return Response({"error": "Недостаточно средств на счёте"}, status=status.HTTP_400_BAD_REQUEST)
    if from_account.currency != to_account.currency:
        return Response({"error": "Перевод между разными валютами недоступен"}, status=status.HTTP_400_BAD_REQUEST)
    from django.db import transaction as db_transaction
    with db_transaction.atomic():
        from_account.balance -= amount
        from_account.save()

        to_account.balance += amount
        to_account.save()

        transaction = Transaction.objects.create(from_account=from_account, to_account=to_account, amount=amount, transaction_type='Transfer', status='Completed', description=description)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data, status=status.HTTP_201_CREATED)