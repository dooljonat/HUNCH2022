import random
from datetime import datetime, timedelta

import pytz
from django.core.management.base import BaseCommand

from fermentationlab.models import Temperature, CO2Level

class Command(BaseCommand):
    help = 'Populates the database with randomly generated data'

    def add_arguments(self, parser):
        parser.add_argument('--amount', type=int, help='The number of purchases that should be created.')
        # return super().add_arguments(parser)
    
    def handle(self, *args, **options):
        amount = options['amount'] if options['amount'] else 2500
        for i in range(0, amount):
            dt = pytz.utc.localize(datetime.now() - timedelta(days=random.randint(0, 1825)))
            temperature = Temperature.objects.create(
                temperature = random.randint(50, 100)
            )
            co2_level = CO2Level.objects.create(
                co2_level = random.randint(50, 100)
            )

            temperature.created_on = dt
            co2_level.created_on = dt

            temperature.save()
            co2_level.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database.'))