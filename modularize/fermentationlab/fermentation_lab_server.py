from re import S
import socket
import time
#import Adafruit_DHT
from datetime import datetime, timedelta
import pytz
import enum
import json

from sensor import Sensor
from camera import Camera
import utils as utils

""" This script will be on the Raspberry pi
    for the FERMENTATION LAB"""

""" TODO:
    When this server receives the message to send data,
    send json data back to client;
    Add sensor reading functionality;
    Store the sensor reading in a dictionary (clear it everytime data is successfully sent to server)
    Add camera command functionality;
"""

# For temperature and humidity sensor
# DHT_SENSOR = Adafruit_DHT
# DHT_PIN = 6

# For sockets
HOST = '192.168.1.189'
PORT = 65439


class Message(enum.Enum):
    Get_data = "1"
    Take_Picture = "2"


# Local temperature and humidity lists
temperature_list = []
humidity_list = []


def main():
    # Create the socket
    sock = create_socket()
    # start the socket listening
    sock.listen()
    print('socket now listening')
    # accept the socket response from the client, and get the connection object
    conn, addr = sock.accept()
    print('socket accepted, got connection object')

    # Create interface objects
    sensor = Sensor()

    camera = Camera()

    # Main loop
    while True:
        # Get sensor data
        temperature_obj, humidity_obj = sensor.read_sensor()
        temperature_list.append(temperature_obj)
        humidity_list.append(humidity_obj)

        # Get SOCKETS message
        message = conn.recv(1024)
        message = message.decode()

        if message == "get_data":
            print("SENDING SENSOR DATA "+ str(datetime.now()))
            # Send back the list of temperature, humidity objects in json format
            send_back_dict = data_to_dict([temperature_list, humidity_list],
                                          ["Temperatures", "Humidities"])
            send_back_json = json.dumps(send_back_dict, default=utils.datetime_handler)

            # sock.sendall(bytes(send_back_json,encoding="utf-8"))
            conn.sendall(bytes(send_back_json, encoding="utf-8"))

            # Reset the local temperature, humidity objects
            temperature_list.clear()
            humidity_list.clear()

        elif message == "take_picture":
            print("TAKING AND SENDING PICTURE AT " + str(datetime.now()))
            file_path = camera.take_picture()

            file = open(file_path, 'rb')
            image_data = file.read(2048)

            while image_data:
                conn.send(image_data)
                image_data = file.read(2048)

            file.close()
        else:
            print("Waiting for message or received unknown message " + message)

        time.sleep(50)


def data_to_dict(data_list, titles):
    """ 
    Formats lists of data into dictionaries
    Params: Data list : list of lists of data objs (temp, humidity)
            formatted like this: [[{obj}, etc..], [{obj}, etc..]]
            titles : list of titles for corresponding data lists"""
    send_back_dict = {}
    i = 0
    for list in data_list:
        dict_objs = []
        for x in range(len(list)):
            dict_objs.append(list[x].__dict__)
        send_back_dict[titles[i]] = dict_objs
        i += 1

    return send_back_dict


def create_socket():
    # instantiate a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('socket instantiated')

    # bind the socket
    sock.bind((HOST, PORT))
    print('socket binded')
    return sock


if __name__ == '__main__':
    main()
