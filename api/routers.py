
class Database:
    """ Name of sqlite database as shown in settings.py """
    MonthlySummary = 'monthly_summary'
    Questrade = 'questrade'


def decide_on_model(model):
    """Small helper function to pipe all DB operations of a worlddata model to the world_data DB"""
    if model._meta.app_label == Database.MonthlySummary:
        return Database.MonthlySummary
    elif model._meta.app_label == Database.Questrade:
        return Database.Questrade
    else:
        return None


class ApiRouter:
    """
    Implements a database router so that:

    - Django related db goes to 'default'
    - Legacy monthly_summary db goes to 'monthly_summary'
    """
    def db_for_read(self, model, **hints):
        return decide_on_model(model)

    def db_for_write(self, model, **hints):
        return decide_on_model(model)

    def allow_relation(self, obj1, obj2, **hints):
        # Allow any relation if both models are part of the worlddata app
        if obj1._meta.app_label == 'api' and obj2._meta.app_label == 'api':
            return True
        # Allow if neither is part of worlddata app
        elif 'api' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        # by default return None - "undecided"

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # allow migrations on the "default" (django related data) DB
        if db == 'default' and (app_label != Database.MonthlySummary or app_label != Database.Questrade):
            return True

        # allow migrations on the legacy database too:
        # this will enable to actually alter the database schema of the legacy DB!
        if db == Database.MonthlySummary and app_label == Database.MonthlySummary:
           return True

        if db == Database.Questrade and app_label == Database.Questrade:
            return True

        return False
