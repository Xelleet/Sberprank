from django.db import models
from django.contrib.auth.models import User
from accounts.models import Account

class Loan(models.Model):
    STATUS_CHOICES = [
        ('pending', 'На рассмотрении'),
        ('approved', 'Одобрён'),
        ('rejected', 'Отклонён'),
        ('paid', 'Погашен'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=15)
    interest_rate = models.DecimalField(default=12.00, decimal_places=2, max_digits=5)
    term_months = models.PositiveIntegerField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    monthly_payment = models.DecimalField(decimal_places=2, max_digits=15)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    remaining_balance = models.DecimalField(default=amount, decimal_places=2, max_digits=15)

    def __str__(self):
        return f"Кредит {self.amount} - {self.user.username}"

    def save(self, *args, **kwargs):
        from datetime import date, timedelta
        import math
        r = self.interest_rate / 100 / 12
        n = self.term_months
        if r > 0:
            self.monthly_payment = self.amount * (r * (1 + r)**n) / ((1 + r)**n-1)
        else:
            self.monthly_payment = self.amount / n

        self.remaining_balance = self.amount
        self.end_date = self.start_date + timedelta(days=30 * n)
        super().save(*args, **kwargs)

class LoanPayment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    paid_date = models.DateField(null=True, blank=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Платеж {self.amount} по кредиту {self.loan.id}"