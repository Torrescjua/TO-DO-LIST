from django.apps import AppConfig

class BaseConfig(AppConfig):
    """
    Configuration class for the base application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
