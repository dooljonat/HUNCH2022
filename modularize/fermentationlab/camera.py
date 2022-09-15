from picamera import PiCamera
from time import sleep
import os

class Camera:
    camera = PiCamera()
    def take_picture(self):
        self.camera.capture('/home/pi/Desktop/image.jpg')
        return '/home/pi/Desktop/image.jpg'
    
    def test_take_picture(self):
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, 'raspberry-pie.jpg')
        return filename
