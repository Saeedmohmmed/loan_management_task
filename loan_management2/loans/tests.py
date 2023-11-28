from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User
from .models import LoanFund
from .serializers import LoanFundSerializer

class LoanFundViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_get_loan_funds(self):
        # Create some test data
        LoanFund.objects.create(Owner=self.user, amount=50000, interest_rate=0.05)
        LoanFund.objects.create(Owner=self.user, amount=100000, interest_rate=0.07)

        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Make a GET request to the view
        response = self.client.get(reverse('loan-fund'))

        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response data matches the expected serialized data
        expected_data = LoanFundSerializer(LoanFund.objects.all(), many=True).data
        self.assertEqual(response.data, expected_data)

    def test_create_loan_fund(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Data for the POST request
        data = {'Owner': self.user.id, 'amount': 75000, 'interest_rate': 0.06}

        # Make a POST request to the view
        response = self.client.post(reverse('loan-fund'), data, format='json')

        # Check that the response status code is 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check that the loan fund was created in the database
        self.assertEqual(LoanFund.objects.count(), 1)

        # Check that the response data matches the expected serialized data
        expected_data = LoanFundSerializer(LoanFund.objects.first()).data
        self.assertEqual(response.data, expected_data)
