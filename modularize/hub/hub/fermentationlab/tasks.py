from celery import shared_task

import time
import socket

# logger = get_task_logger(__name__)

HOST = '172.20.10.7'
PORT = 65439


@shared_task
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

   received = sock.recv(1024)
   received = received.decode()
   print("RECEIVED:" , received)
   sock.close()
   time.sleep(5)



# @periodic_task(run_every=(crontab(minute='*/5')), name="send_data_request", ignore_result=True)
# def some_task():
#     """Sends a request for temperature and humidity data from the Raspberry PI, receives it,
#        then adds it to the Temperature and Humidity DB if successful"""
#     logger.info("Sent data request")
