#import Adafruit_DHT
import time
from datetime import datetime, timedelta
import pytz

# DHT_SENSOR = Adafruit_DHT
# DHT_PIN = 6

# Data Models


class Temperature:
    def __init__(self, created_on, temperature):
        self.created_on = created_on
        self.temperature = temperature


class Humidity:
    def __init__(self, created_on, humidity):
        self.created_on = created_on
        self.humidity = humidity


class Sensor:
    def read_sensor(self):
        temperature_obj = None
        humidity_obj = None
        humidity, temperature = Adafruit_DHT.read(11, DHT_PIN)
        if humidity is not None and temperature is not None:
            dt = pytz.utc.localize(datetime.now())
            temperature_obj = Temperature(
                created_on=dt, temperature=temperature)
            humidity_obj = Humidity(created_on=dt, humidity=humidity)

            print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(
                temperature, humidity))
        else:
            print(
                "[FERMENTATIONLAB :: TEMP_HUMIDITY_SENSOR] Sensor failure. Check wiring.")

        return temperature_obj, humidity_obj

    def create_test_data(self):
        temperature_list = []
        humidity_list = []

        temp1 = Temperature(created_on=pytz.utc.localize(
            datetime.now()), temperature="70")
        temp2 = Temperature(created_on=pytz.utc.localize(
            datetime.now()), temperature="71")
        temp3 = Temperature(created_on=pytz.utc.localize(
            datetime.now()), temperature="72")
        temp4 = Temperature(created_on=pytz.utc.localize(
            datetime.now()), temperature="73")

        humidity1 = Humidity(created_on=pytz.utc.localize(
            datetime.now()), humidity="31")
        humidity2 = Humidity(created_on=pytz.utc.localize(
            datetime.now()), humidity="32")
        humidity3 = Humidity(created_on=pytz.utc.localize(
            datetime.now()), humidity="33")
        humidity4 = Humidity(created_on=pytz.utc.localize(
            datetime.now()), humidity="34")

        temperature_list.append(temp1)
        temperature_list.append(temp2)
        temperature_list.append(temp3)
        temperature_list.append(temp4)

        humidity_list.append(humidity1)
        humidity_list.append(humidity2)
        humidity_list.append(humidity3)
        humidity_list.append(humidity4)

        return temperature_list, humidity_list
