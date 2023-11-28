from django.contrib import admin
from .models import LoanFund, LoanCustomer, BankPersonnel, Plan, Transaction

# class LoanFundAdmin(admin.ModelAdmin):
#     list_display = ('name', 'amount')

# class LoanCustomerAdmin(admin.ModelAdmin):
#     list_display = ('loan_fund', 'loan_term', 'loan_amount')

# class BankPersonnelAdmin(admin.ModelAdmin):
#     list_display = ('name', 'max_amount', 'min_amount', 'interest_rate', 'duration')

admin.site.register(LoanFund)
admin.site.register(LoanCustomer)
admin.site.register(BankPersonnel)
admin.site.register(Plan)
admin.site.register(Transaction)
