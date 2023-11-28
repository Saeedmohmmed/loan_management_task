# loans/urls.py
from django.urls import path, include
from .views import (
    loan_fund, loan_customer, LoanFund , bank_personnel ,plan_loans
    ,LoanFundViewSet,LoanCustomerViewSet,BankPersonnelViewSet)

from rest_framework.routers import DefaultRouter


# viewsets
router = DefaultRouter()
router.register("loan-funds", LoanFundViewSet)
router.register("loan-customer", LoanCustomerViewSet)
router.register("bank-personnel", BankPersonnelViewSet)
###############

app_name = "loans"


urlpatterns = [
    path('loan-funds/', loan_fund, name='loan-funds'),
    path('loan-customers/', loan_customer, name='loan-customer-list'),
    path('bank-personnel/',bank_personnel, name='bank-personnel-list'),
    path('plan-loans/',plan_loans, name='plan-loans'),


    # viewsets
    path("api/", include(router.urls))


]
