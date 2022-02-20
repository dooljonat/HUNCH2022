import sys
import json
import datetime

# def dict_to_json(message_dict):
#     return json.dumps(message_dict)

# def send_json_message(socket, address, port, message_dict):
#     # Convert dictionary to json
#     json_message = dict_to_json(message_dict)

#     # Connect to socket and send message
#     try:
#         sock = socket.socket()
#     except socket.error as err:
#         print('Socket error because of %s' % (err))

#     try:
#         sock.connect((address, port))
#         sock.send(json_message.encode())
#     except socket.gaierror:
#         print('There an error resolving the host')
#         sys.exit()
    
#     # Close socket connection 

#     print(json_message, 'was sent!')
#     sock.close()

def datetime_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError("Unknown type")