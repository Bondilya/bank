from django.utils import timezone
from django.db.models import Sum
from rest_framework import generics

from .models import Balance, Transaction, User
from .serializers import BalanceSerializer, TransactionSerializer, UserSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TopUsers(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        six_months_ago = timezone.now() - timezone.timedelta(days=180)
        queryset = User.objects.filter(
            transaction__date__gte=six_months_ago
        ).annotate(tr_amount_sum=Sum('transaction__amount')).order_by('-tr_amount_sum')

        return queryset


class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class BalanceList(generics.ListCreateAPIView):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer
