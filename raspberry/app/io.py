#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pinList = [27, 3, 4, 17]

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)


def pin(command, pin_no):
    if command == "open":
	set = GPIO.LOW
    elif command == "close":
	set = GPIO.HIGH
    else:
	raise ValueError("Invalid command {} for pin {}".format(command, pin_no))

    #inregistreaza task-ul intr-un json ca sa reluam tot 
    GPIO.output(pinList[pin_no-1], set)
