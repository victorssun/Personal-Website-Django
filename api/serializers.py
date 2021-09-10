from rest_framework import serializers

from .models import MonthlySummary, Transactions
from .models import Positions, Trades, Transfers


class IncomeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MonthlySummary
        fields = ('rowId', 'date', 'income', 'cashback', 'interest', 'investment')


class TransactionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transactions
        fields = ('rowId', 'date', 'description', 'location', 'category', 'amount')


class PositionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Positions
        fields = ('date', 'symbol', 'amount')


class TradesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trades
        fields = ('date', 'symbol', 'quantity', 'amount')


class TransfersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transfers
        fields = ('date', 'amount')
