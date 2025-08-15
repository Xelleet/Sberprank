from django.db import models
from accounts.models import Account
from django.contrib.auth.models import User

class Transaction(models.Model):
    transactions_types = [
        ('Transfer', 'Перевод'),
        ('Replenishment', 'Пополнение'),
        ('Debit', 'Списание'),
        ('Loan_payment', 'Платеж по кредиту')
    ]

    STATUS_CHOICES = [
        ('Completed', 'Успешно'),
        ('Waiting', 'В ожидании'),
        ('Error', 'Ошибка')
    ]

    from_account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True, related_name='from_account')
    to_account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True, related_name='to_account')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    transaction_type = models.CharField(choices=transactions_types, max_length=20)
    status = models.CharField(choices=STATUS_CHOICES, default='Completed', max_length=20)
    description = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type}: {self.amount} from {self.from_account} to {self.to_account}"

    class Meta:
        ordering = ['-timestamp']