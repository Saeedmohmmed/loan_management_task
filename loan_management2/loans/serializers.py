# loans/serializers.py
from rest_framework import serializers
from .models import LoanFund, LoanCustomer, BankPersonnel , Plan

class LoanFundSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanFund
        fields = '__all__'

class LoanCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanCustomer
        fields = '__all__'

class BankPersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankPersonnel
        fields = '__all__'

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'
