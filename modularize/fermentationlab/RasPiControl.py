from picamera import PiCamera
import RPi.GPIO as GPIO
import time

class Camera():

    def videoMod():
        #Records a ten second video
        PiCamera.resolution = (640, 480)
        PiCamera.start_preview()
        PiCamera.start_recording('test_video.h264')
        #Controls how long the camera records
        time.sleep(10)
        PiCamera.stop_recording()
        PiCamera.stop_preview

    def captureMod():
        #Takes a picture
        PiCamera.resolution = (640, 480)
        PiCamera.start_preview()
        #Timer before picture is taken
        time.sleep(3)
        PiCamera.capture('test_photo.jpg')
        PiCamera.stop_preview

    def PreviewMod(option):
        #Opens or closes a preview of what the camera sees
        PiCamera.resolution = (640, 480)
        if option == True:
            PiCamera.start_preview()

        else:
            PiCamera.stop_preview()

class LED():
    def greenLED():
        #this will turn the green LED on for five seconds and turn it off
        green_led = 5
        sleep_time = 5

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(green_LED, GPIO.OUT)

        GPIO.output(green_led, GPIO.HIGH)
        time.sleep(sleep_time)
        GPIO.output(green_led, GPIO.LOW)
        GPIO.cleanup()

    def redLED():
        #this will make the red LED blink five times
        red_led = 6
        sleep_time = 1

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(red_LED, GPIO.OUT)

        for i in range (5):
            GPIO.output(red_led, GPIO.HIGH)
            time.sleep(sleep_time)
            GPIO.output(red_led, GPIO.LOW)
            time.sleep(sleep_time)
        GPIO.cleanup()
