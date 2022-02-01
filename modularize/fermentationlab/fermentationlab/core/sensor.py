import Adafruit_DHT
import time
from datetime import datetime, timedelta
import pytz



DHT_SENSOR = Adafruit_DHT
DHT_PIN = 6

def read_sensor(models):
    while True:
        humidity, temperature = Adafruit_DHT.read(11, DHT_PIN)
        if humidity is not None and temperature is not None:
            dt = pytz.utc.localize(datetime.now())
            temperature_object = models.Temperature.objects.create(
                temperature= temperature, 
            )
            humidity_object = models.Humidity.objects.create(
                humidity = humidity,
            )

            print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
            temperature_object.save()
            humidity_object.save()
        else:
            print("[FERMENTATIONLAB :: TEMP_HUMIDITY_SENSOR] Sensor failure. Check wiring.")
        time.sleep(10)