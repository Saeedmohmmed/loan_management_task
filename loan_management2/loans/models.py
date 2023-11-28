# loans/models.py
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class LoanFund(models.Model):
    Owner          = models.OneToOneField(User, on_delete=models.PROTECT)
    amount         = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate  = models.FloatField()
    date           = models.DateField(auto_now=True)

    def __str__(self):
        return self.Owner.username

class LoanCustomer(models.Model):
    user            = models.ForeignKey(User, on_delete=models.PROTECT)


    def __str__(self):
        return "customer: "+self.user.username



class BankPersonnel(models.Model):
    user            = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.username


class Plan(models.Model):
    name            = models.CharField(max_length=255)
    min_amount      = models.DecimalField(max_digits=10, decimal_places=2)
    max_amount      = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate   = models.FloatField()
    duration        = models.DurationField()
    bankPersonnel   = models.ForeignKey(BankPersonnel,  on_delete=models.PROTECT)
    description     = models.TextField()

    def __str__(self):
        return self.name


class Transaction (models.Model):
    customer        = models.ForeignKey(LoanCustomer,  on_delete=models.PROTECT)
    plan            = models.ForeignKey(Plan,  on_delete=models.PROTECT)
    date            = models.DateField(auto_now=True)
    amount          = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.customer.user.username + " has " + self.plan.name +" on "+ str(self.date)
