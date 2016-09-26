import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(5)
    if input_state == False:
        print('Button Pressed')
    else:
        print('Button NOT Pressed')
    time.sleep(0.5)
