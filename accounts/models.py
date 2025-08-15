from django.contrib.auth.models import User
from django.db import models
import random

class Account(models.Model):
    CURRENCY_CHOICES = [
        ('RUB', 'Российский рубль'),
        ('USD', 'Доллар США'),
        ('EUR', 'Евро'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts')
    account_number = models.CharField(max_length=20, unique=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='RUB')
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.account_number} ({self.currency}) - {self.balance}"

    def save(self, *args, **kwargs):
        if not self.account_number:
            self.account_number = "".join([str(random.randint(0,9)) for _ in range(20)])
        super().save(*args, **kwargs)