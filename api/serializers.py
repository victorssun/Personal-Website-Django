from rest_framework import serializers

from .models import MonthlySummary, Transactions
from .models import Positions, Trades, Transfers


class IncomeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MonthlySummary
        fields = ('date', 'income', 'cashback', 'interest', 'investment')


class ExpensesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MonthlySummary
        fields = ('date', 'eatingOut', 'groceries', 'restaurants', 'personalItems', 'extra', 'transportation', 'housing', 'help')


class TransactionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transactions
        fields = ('rowId', 'date', 'description', 'location', 'category', 'amount')


class PositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = ('date', 'account', 'symbol', 'quantity', 'amount')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['account'] = instance.account.name
        ret['symbol'] = instance.symbol.symbol
        ret['date'] = instance.date.date
        return ret


class TradesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trades
        fields = ('date', 'account', 'symbol', 'quantity', 'amount')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['account'] = instance.account.name
        ret['symbol'] = instance.symbol.symbol
        ret['date'] = instance.date.date
        return ret


class TransfersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfers
        fields = ('date', 'account', 'amount')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['account'] = instance.account.name
        ret['date'] = instance.date.date
        return ret
