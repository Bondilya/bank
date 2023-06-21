from decimal import Decimal
from django.contrib.auth.models import User
from django.db import models


class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0))


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
