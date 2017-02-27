import time
import requests
from RPi import GPIO
from lib import config

URL = "http://127.0.0.1/set_procedure/{}"
GPIO.setmode(GPIO.BCM)
for pin in config.button_pins.itervalues():
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
    for procedure, pin in config.button_pins.iteritems():
        input_state = GPIO.input(pin)
        if input_state == False:
            print("Button '{}' Pressed".format(procedure))
            requests.get(URL.format(procedure))
    time.sleep(0.2)
