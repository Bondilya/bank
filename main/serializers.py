from rest_framework import serializers
from .models import User, Transaction, Balance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = '__all__'
