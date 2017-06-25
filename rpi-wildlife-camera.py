import RPi.GPIO as GPIO
import time
import os
import picamera
from time import sleep

camera = picamera.PiCamera()
PIR_PIN = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

while True:
  if GPIO.input(PIR_PIN):
    print (“Motion Detected!”)
    os.system("sudo i2cset -y 1 0x70 0x00 0xa5")
		camera.start_recording('video.h264')
    time.sleep(1000)
		camera.stop_recording()
	else:
		os.system("sudo i2cset -y 1 0x70 0x00 0x00)
		
		

except KeyboardInterrupt:
               print “ Quit”
               GPIO.cleanup()
