from django.urls import path
from main.views import UserList, UserDetail, TransactionList, TransactionDetail, BalanceList, TopUsers

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('transactions/', TransactionList.as_view()),
    path('transactions/<int:pk>/', TransactionDetail.as_view()),
    path('balances/', BalanceList.as_view()),
    path('top-users/', TopUsers.as_view())
]
