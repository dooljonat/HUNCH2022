from django.apps import AppConfig

class CeleryWorker(AppConfig):
    name = 'djcelery'
    


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
