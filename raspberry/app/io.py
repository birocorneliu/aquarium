#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pinList = [27, 3, 4, 17]
pin_config = {
    "led": 	 3, 
    "865":  	 4, 
    "830": 	17,
    "co2": 	27, 
    "pompa": 	 3,

    "micro": 	 3,
    "macro": 	 4,
    "fier": 	17,
    "twinstar": 27,
}

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)


def pin(command, pin_id):
    if command == "open":
	set = GPIO.LOW
    elif command == "close":
	set = GPIO.HIGH
    else:
	raise ValueError("Invalid command {} for {}".format(command, pin_id))

    if pin_id not in pin_config:
	raise ValueError("Pin id '{}' is not configured".format(pin_id))
    #inregistreaza task-ul intr-un json ca sa reluam tot 
    GPIO.output(pin_config[pin_id], set)
    time.sleep(0.2)
