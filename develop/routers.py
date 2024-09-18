# routers.py

class SecondDatabaseRouter:
    """
    A router to control all database operations on models in the
    second database.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read models from second database.
        """
        if model._meta.app_label == 'develop':
            return 'second'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write models to second database.
        """
        if model._meta.app_label == 'develop':
            return 'second'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if models are in the second database.
        """
        if obj1._meta.app_label == 'develop' and obj2._meta.app_label == 'develop':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the second app's models get migrated to the second database.
        """
        if app_label == 'develop':
            return False  # Отключение миграции, если нужно включить db == 'second'
        return None
