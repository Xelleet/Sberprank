from django.contrib import admin
from .models import Loan

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'account',
        'amount',
        'interest_rate',
        'term_months',
        'monthly_payment',
        'remaining_balance',
        'status',
        'start_date',
        'end_date',
    )
    list_filter = ('status', 'start_date', 'end_date', 'interest_rate')
    search_fields = ('user__username', 'account__id')
    readonly_fields = ('monthly_payment', 'remaining_balance', 'start_date', 'end_date')  # status убран
    ordering = ('-start_date',)
    list_editable = ('status',)

    fieldsets = (
        ('Основная информация', {
            'fields': ('user', 'account', 'amount', 'interest_rate', 'term_months')
        }),
        ('Расчёты', {
            'fields': ('monthly_payment', 'remaining_balance')
        }),
        ('Статус', {
            'fields': ('status',)   # тут можешь выбирать
        }),
        ('Даты', {
            'fields': ('start_date', 'end_date')
        }),
    )
