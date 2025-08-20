from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Loan, LoanPayment
from .serializers import LoanSerializer, LoanPaymentSerializer
from accounts.models import Account

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def apply_for_loan(request):
    account_id = request.data.get('account_id')
    amount = request.data.get('amount')
    term_months = request.data.get('term_months')

    if not all([account_id, amount, term_months]):
        return Response({'error': "Неполные данные"}, status=status.HTTP_400_BAD_REQUEST)

    account = get_object_or_404(Account, id=account_id, user=request.user)
    loan = Loan.objects.create(user=request.user, account=account, amount=amount, term_months=term_months, status='pending')
    from datetime import date, timedelta
    for month in range(loan.term_months):
        due_date = loan.start_date + timedelta(days=30*(month+1))
        LoanPayment.objects.create(loan=loan, amount=loan.monthly_payment, due_date=due_date)
    serializer = LoanSerializer(loan)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes(IsAuthenticated)
def my_loans(request):
    loans = Loan.objects.filter(user=request.user).order_by('-start_date')
    serializer = LoanSerializer(loans, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def loan_detail(request, loan_id):
    loan = get_object_or_404(Loan, id=loan_id, user=request.user)
    payments = LoanPayment.objects.filter(loan=loan).order_by('due_date')
    loan_serializer = LoanSerializer(loan)
    payments_serializer = LoanPaymentSerializer(payments, many=True)
    return Response({
        'loan': loan_serializer.data,
        'payments': payments_serializer.data
    })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def make_loan_payment(request, loan_id):
    loan = get_object_or_404(Loan, id=loan_id, user=request.user)
    payment = get_object_or_404(LoanPayment, loan=loan, is_paid=False, paid_date__isnull=True)

    if loan.account.balance < payment.amount:
        return Response({"error": "Недостаточно средств"}, status=status.HTTP_400_BAD_REQUEST)

    from django.db import transaction as db_transaction
    from datetime import date

    with db_transaction.atomic():
        loan.account.balance -= payment.amount
        loan.account.save()
        payment.is_paid = True
        payment.save()
        payment.paid_date = date.today()
        loan.remaining_balance -= payment.amount
        if loan.remaining_balance < 0:
            loan.remaining_balance = 0
            loan.status = 'paid'
        loan.save()
        return Response({"message": 'Платёж успешно проведен'}, status=status.HTTP_200_OK)