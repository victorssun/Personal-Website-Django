from django.db import models

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
    eatingOut = models.FloatField(db_column='eating out', blank=True, null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    groceries = models.FloatField(blank=True, null=True)  # This field type is a guess.
    restaurants = models.FloatField(blank=True, null=True)  # This field type is a guess.
    personalItems = models.FloatField(db_column='personal items', blank=True, null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    extra = models.FloatField(blank=True, null=True)  # This field type is a guess.
    transportation = models.FloatField(blank=True, null=True)  # This field type is a guess.
    housing = models.FloatField(blank=True, null=True)  # This field type is a guess.
    education = models.FloatField(blank=True, null=True)  # This field type is a guess.
    help = models.FloatField(blank=True, null=True)  # This field type is a guess.
    income = models.FloatField(blank=True, null=True)  # This field type is a guess.
    bank = models.FloatField(blank=True, null=True)  # This field type is a guess.
    cashback = models.FloatField(blank=True, null=True)  # This field type is a guess.
    interest = models.FloatField(blank=True, null=True)  # This field type is a guess.
    investment = models.FloatField(db_column='invest QT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'monthly_summary'
        app_label = 'monthly_summary'


class Transactions(models.Model):
    """ Transaction information for categeorized expensese """
    rowId = models.IntegerField(primary_key=True)
    date = models.DateField()
    dateStatement = models.DateField(db_column='date_statement')
    description = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    category = models.TextField()
    amount = models.FloatField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'transactions'
        app_label = 'monthly_summary'


class Balances(models.Model):
    """ Summary on investment balances: total equity, cash, market value"""
    rowId = models.IntegerField(primary_key=True)
    date = models.DateField()
    exchangeRate = models.FloatField(db_column='exchangeRate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cash = models.FloatField(blank=True, null=True)  # This field type is a guess.
    marketValue = models.FloatField(db_column='marketValue', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    totalEquity = models.FloatField(db_column='totalEquity')  # Field name made lowercase. This field type is a guess.
    cumulative = models.FloatField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'df_balances'
        app_label = 'account_data'


class Positions(models.Model):
    """ Positions information of stock holdings """
    rowId = models.IntegerField(primary_key=True)
    date = models.DateField()
    symbol = models.TextField()
    amount = models.FloatField(db_column='value')  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'df_positions'
        app_label = 'account_data'


class Returns(models.Model):
    """ Return on stock holdings """
    rowId = models.IntegerField(primary_key=True)
    date = models.DateField()
    symbol = models.TextField()
    quantity = models.IntegerField(blank=True, null=True)  # This field type is a guess.
    netProfit = models.FloatField(db_column='netProfit')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'df_returns'
        app_label = 'account_data'


class Trades(models.Model):
    """ Trades on stock holdings """
    rowId = models.IntegerField(primary_key=True)
    date = models.DateField()
    symbol = models.TextField()
    quantity = models.IntegerField()  # This field type is a guess.
    amount = models.FloatField(db_column='totalCost')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'df_trades'
        app_label = 'account_data'


class Transfers(models.Model):
    """ Withdrawals and deposits in investment account """
    rowId = models.IntegerField(primary_key=True)
    date = models.DateField()
    amount = models.FloatField(db_column='added', blank=True, null=True)  # This field type is a guess.
    cumulative = models.FloatField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'df_transfers'
        app_label = 'account_data'
