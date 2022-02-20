# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import datetime
import board
import adafruit_dht

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D6)

class Temperature:
    def __init__(self, created_on, temperature):
        self.created_on = created_on
        self.temperature = temperature

class Humidity:
    def __init__(self, created_on, humidity):
        self.created_on = created_on
        self.humidity = humidity


def read_sensor():
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity

        temp = Temperature(datetime.now, temperature_f)
        humidity = Humidity(datetime.now(), humidity)

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)