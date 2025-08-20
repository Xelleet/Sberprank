from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Account
from .serializers import AccountSerializer, CreateAccountSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def accounts_list(request):
    accounts = Account.objects.filter(user=request.user)
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def account_detail(request, account_id):
    account = Account.objects.get(user=request.user, id=account_id)
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