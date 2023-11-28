from .models import LoanFund, LoanCustomer, BankPersonnel
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, status
from .models import LoanFund, LoanCustomer, BankPersonnel ,Plan
from .serializers import LoanFundSerializer, LoanCustomerSerializer, BankPersonnelSerializer ,PlanSerializer




@api_view(['GET', 'POST'])
def loan_fund(request):
    if request.method == 'GET':
        loan_funds = LoanFund.objects.all()
        serializer = LoanFundSerializer(loan_funds, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = LoanFundSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response

@api_view(['GET', 'POST'])
def loan_customer(request):
    if request.method == 'GET':
        loan_customer = LoanCustomer.objects.all()
        serializer = LoanCustomerSerializer(loan_customer, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = LoanCustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response

@api_view(['GET', 'POST'])
def bank_personnel(request):
    if request.method == 'GET':
        bank_personnel = BankPersonnel.objects.all()
        serializer = BankPersonnelSerializer(bank_personnel, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = BankPersonnelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response

@api_view(['GET', 'POST'])
def plan_loans(request):
    if request.method == 'GET':
        plan_loans =Plan.objects.all()
        serializer = PlanSerializer(plan_loans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = PlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response


class LoanFundViewSet(viewsets.ModelViewSet):
    queryset = LoanFund.objects.all()
    serializer_class = LoanFundSerializer

class LoanCustomerViewSet(viewsets.ModelViewSet):
    queryset = LoanCustomer.objects.all()
    serializer_class = LoanCustomerSerializer

class BankPersonnelViewSet(viewsets.ModelViewSet):
    queryset = BankPersonnel.objects.all()
    serializer_class = BankPersonnelSerializer
