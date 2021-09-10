
def decide_on_model(model):
    """Small helper function to pipe all DB operations of a worlddata model to the world_data DB"""
    if model._meta.app_label == 'monthly_summary':
        return 'monthly_summary'
    elif model._meta.app_label == 'account_data':
        return 'account_data'
    else:
        return None


class ApiRouter:
    """
    Implements a database router so that:

    - Django related db goes to 'default'
    - Legacy monthly_summary db goes to 'monthly_summary'
    - Legancy account_data db goes to 'account_data'
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
        if db == 'default' and (app_label != 'monthly_summary' or app_label != 'account_data'):
            return True

        # allow migrations on the legacy database too:
        # this will enable to actually alter the database schema of the legacy DB!
        if db == 'monthly_summary' and app_label == "monthly_summary":
           return True

        if db == 'account_data' and app_label == "account_data":
            return True

        return False
