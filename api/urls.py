from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'api'

"""
permissions:
- admin: GET, PUT/PATCH, POST, DELETE, HEADER, OPTION
- others: GET, HEADER, OPTION

authentication:
- session: requires login through admin/
- basic: login through popup TODO: how to get rid of cookie after closing window

api/income/
- lists all income streams by month

api/transactions/
- list all transactions 

api/balances/ [NOT IMPLEMENTED]
- list balances, derived from positions

api/positions/
- list positions

api/trades/
- list trades

api/returns/ [NOT IMPLEMENTED]
- list returns, derived from trades

api/transfers/
- list withdrawals/deposits
"""

router = routers.DefaultRouter()
router.register(r'income', views.IncomeSet)
router.register(r'transactions', views.TransactionsSet)
router.register(r'positions', views.PositionsSet)
router.register(r'trades', views.TradesSet)
router.register(r'transfers', views.TransfersSet)

urlpatterns = [
    path('', include(router.urls)),
]
