from __future__ import absolute_import, unicode_literals

import os
import time
from datetime import datetime
import socket
import json

from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hub.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

app = Celery('hub')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

HOST = '172.20.10.7'
PORT = 65439

from django.conf import settings
from fermentationlab.models import Temperature, Humidity, PiCameraImage


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('world') every 30 seconds
    sender.add_periodic_task(60, send_data_request.s())


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

@app.task
def send_data_request():
   """Sends a request for data from the Raspberry Pi, receives it, and adds it to the DB"""

   # instantiate a socket object
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   print('socket instantiated')

   # connect the socket
   connectionSuccessful = False
   while not connectionSuccessful:
      try:
         sock.connect((HOST, PORT))    # Note: if execution gets here before the server starts up, this line will cause an error, hence the try-except
         print('socket connected')
         connectionSuccessful = True
      except:
         pass

   socks = [sock]

   message = "get_data"
   sock.sendall(message.encode())

   try:
       received = sock.recv(1024)
       received = received.decode()
       received = json.loads(received)

       print(received)

       temperatures_list = received.get("Temperatures")
       humidities_list = received.get("Humidities")

       for temperature in temperatures_list:
           temp = Temperature()
           temp.created_on = temperature.get("created_on")
           temp.temperature = temperature.get("temperature")
           temp.save()
       for humidity in humidities_list:
           humid = Humidity()
           humid.created_on = humidity.get("created_on")
           humid.humidity = humidity.get("humidity")
           humid.save()
   except:
       print("Failed to retreive data from Raspberry Pi")
   sock.close()
   time.sleep(1)

@app.task
def send_picture_request(username):
    """Sends a request for data from the Raspberry Pi, receives it, and adds it to the DB"""

    # instantiate a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('socket instantiated')

    # connect the socket
    connectionSuccessful = False
    while not connectionSuccessful:
        try:
            sock.connect((HOST, PORT))    # Note: if execution gets here before the server starts up, this line will cause an error, hence the try-except
            print('socket connected')
            connectionSuccessful = True
        except:
            pass

        socks = [sock]

        message = "take_picture"
        sock.sendall(message.encode())

        # Get the current date
        created_on = datetime.now()
        created_on_string = str(created_on)
        created_on_string = created_on_string.replace(" ", "_")
        created_on_string = created_on_string.replace(":", "__")

        # Create file path for image, if it doesnt exist, create it
        file_path = f'media/img/{username}/'
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        # Open the image file and read it from socket connection
        file_path += f"{created_on_string}.jpg"
        print(file_path)
        
        file = open(file_path, "wb")
        image_chunk = sock.recv(4096)
        while image_chunk:
            file.write(image_chunk)
            image_chunk = sock.recv(4096)

        file.close()

        # Remove media from the path
        file_path = file_path.replace("media/", "")
        print(file_path)

        # Create new PiCameraImage model from image file
        picture = PiCameraImage()
        picture.created_on = created_on
        picture.upload = file_path
        picture.save()
    sock.close()
    time.sleep(1)


# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
