from django.db import models
from .routers import Database

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class MonthlySummary(models.Model):
    """ Monthly summation of incomes and expenses based on categories """
    rowId = models.IntegerField(primary_key=True)
    date = models.DateField()
    eatingOut = models.FloatField(db_column='eating out', blank=True, null=True)
    groceries = models.FloatField(blank=True, null=True)
    restaurants = models.FloatField(blank=True, null=True)
    personalItems = models.FloatField(db_column='personal items', blank=True, null=True)
    extra = models.FloatField(blank=True, null=True)
    transportation = models.FloatField(blank=True, null=True)
    housing = models.FloatField(blank=True, null=True)
    education = models.FloatField(blank=True, null=True)
    help = models.FloatField(blank=True, null=True)
    income = models.FloatField(blank=True, null=True)
    bank = models.FloatField(blank=True, null=True)
    cashback = models.FloatField(blank=True, null=True)
    interest = models.FloatField(blank=True, null=True)
    investment = models.FloatField(db_column='invest QT', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monthly_summary'
        app_label = Database.MonthlySummary


class Transactions(models.Model):
    """ Transaction information for categorized expenses """
    rowId = models.IntegerField(primary_key=True)
    date = models.DateField()
    dateStatement = models.DateField(db_column='date_statement')
    description = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    category = models.TextField()
    amount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'transactions'
        app_label = Database.MonthlySummary


class Accounts(models.Model):
    id = models.IntegerField(db_column='account_id', primary_key=True)
    number = models.IntegerField(unique=True)
    name = models.CharField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'accounts'
        app_label = Database.Questrade


class Dates(models.Model):
    id = models.IntegerField(db_column='date_id', primary_key=True)
    date = models.DateField(unique=True)

    def __str__(self):
        return str(self.date)

    class Meta:
        managed = False
        db_table = 'dates'
        app_label = Database.Questrade


class Symbols(models.Model):
    id = models.IntegerField(db_column='symbol_id', primary_key=True)
    symbol = models.CharField(unique=True)

    def __str__(self):
        return self.symbol

    class Meta:
        managed = False
        db_table = 'symbols'
        app_label = Database.Questrade


class Positions(models.Model):
    """ Positions information of stock holdings """
    rowId = models.IntegerField(db_column='position_id', primary_key=True)
    account = models.ForeignKey(Accounts, db_column='account_id', on_delete=models.CASCADE)
    symbol = models.ForeignKey(Symbols, db_column='symbol_id', on_delete=models.CASCADE)
    date = models.ForeignKey(Dates, db_column='date_id', on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    amount = models.FloatField(db_column='value')

    class Meta:
        managed = False
        db_table = 'positions'
        app_label = Database.Questrade


class Trades(models.Model):
    """ Trades on stock holdings """
    rowId = models.IntegerField(db_column='trade_id', primary_key=True)
    account = models.ForeignKey(Accounts, db_column='account_id', on_delete=models.CASCADE)
    symbol = models.ForeignKey(Symbols, db_column='symbol_id', on_delete=models.CASCADE)
    date = models.ForeignKey(Dates, db_column='date_id', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    amount = models.FloatField(db_column='value')

    class Meta:
        managed = False
        db_table = 'trades'
        app_label = Database.Questrade


class Transfers(models.Model):
    """ Withdrawals and deposits in investment account """
    rowId = models.IntegerField(db_column='transfer_id', primary_key=True)
    account = models.ForeignKey(Accounts, db_column='account_id', on_delete=models.CASCADE)
    date = models.ForeignKey(Dates, db_column='date_id', on_delete=models.CASCADE)
    amount = models.FloatField(db_column='deposit', blank=True)

    class Meta:
        managed = False
        db_table = 'transfers'
        app_label = Database.Questrade
