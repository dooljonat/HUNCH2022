from celery import shared_task

import time
import socket

# logger = get_task_logger(__name__)


# @periodic_task(run_every=(crontab(minute='*/5')), name="send_data_request", ignore_result=True)
# def some_task():
#     """Sends a request for temperature and humidity data from the Raspberry PI, receives it,
#        then adds it to the Temperature and Humidity DB if successful"""
#     logger.info("Sent data request")
