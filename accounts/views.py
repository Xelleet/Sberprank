from decimal import Decimal, InvalidOperation

from django.core.serializers import serialize
from django.db import transaction
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Account
from .serializers import AccountSerializer, CreateAccountSerializer
from transactions.models import Transaction


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def accounts_list(request):
    accounts = Account.objects.filter(user=request.user)
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def account_detail(request, account_id):
    account = get_object_or_404(Account, user=request.user, id=account_id)
    serializer = AccountSerializer(account)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_account(request):
    currency = request.data['currency']
    if currency not in [c[0] for c in Account.CURRENCY_CHOICES]:
        return Response({'Error': 'Указана не поддерживаемая валюта. Просим вас приобрести DLC со всем нужным контентом'}, status=status.HTTP_400_BAD_REQUEST)
    if Account.objects.filter(user=request.user, currency=currency).exists():
        return Response({'Error': "У вас уже имеется счёт в этой валюте. Приобрести дополнительный слот с счетом одинаковой валюты можно, приобретя BATTLE PASS"}, status=status.HTTP_400_BAD_REQUEST)
    serializer = CreateAccountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response({'success': 'Счёт успешно создан'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'error': "Ошибка в указанных данных"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def deposit_account(request):
    account_id = request.data.get('account_id')
    amount_str = request.data.get('amount')

    if not account_id or not amount_str:
        return Response(
            {"error": "Укажите account_id и amount."},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:

        amount = Decimal(amount_str)
        if amount <= 0:
            return Response(
                {"error": "Сумма должна быть больше 0."},
                status=status.HTTP_400_BAD_REQUEST
            )
        # Округляем до 2 знаков (по умолчанию в DecimalField)
        amount = amount.quantize(Decimal('0.01'))
    except (ValueError, TypeError, InvalidOperation):
        return Response(
            {"error": "Некорректная сумма."},
            status=status.HTTP_400_BAD_REQUEST
        )

    account = get_object_or_404(Account, id=account_id, user=request.user)

    with transaction.atomic():
        account.balance += amount  # Теперь: Decimal + Decimal
        account.save()

        Transaction.objects.create(
            to_account=account,
            amount=amount,
            transaction_type='deposit',
            status='completed',
            description='Пополнение счёта'
        )

    return Response({
        "message": f"Счёт пополнен на {amount} ₽",
        "new_balance": float(account.balance)
    }, status=status.HTTP_200_OK)