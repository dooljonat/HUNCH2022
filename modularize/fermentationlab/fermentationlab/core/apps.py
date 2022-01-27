from django.apps import AppConfig

from . import sensor as sensor

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        print("READY FUNCTION INITIATED")
        sensor.read_sensor()