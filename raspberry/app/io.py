#!/usr/bin/python
import time
from RPi import GPIO
from lib import config


###################################################################################################
class IO_BASE(object):
    PINS = config.pins
    NI_PINS = config.NI_pins
    RESOURCES = config.resources
    MOTOR_PINS = config.MOTOR_PINS
    MOTOR_PINS_BACK = config.MOTOR_PINS_BACK


    #----------------------------------------------------------------------------------------------
    def __init__(self, GPIO):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.GPIO = GPIO
        self.OPEN_PIN = GPIO.LOW
        self.CLOSE_PIN = GPIO.HIGH
        self.OPEN_NI_PIN = GPIO.HIGH
        self.CLOSE_NI_PIN = GPIO.LOW


    #----------------------------------------------------------------------------------------------
    def open(self, pin_id):
        state =  self.OPEN_NI_PIN if pin_id in self.NI_PINS else self.OPEN_PIN
        self.change_pin_status(pin_id, state)


    #----------------------------------------------------------------------------------------------
    def close(self, pin_id):
        state =  self.CLOSE_NI_PIN if pin_id in self.NI_PINS else self.CLOSE_PIN
        self.change_pin_status(pin_id, state)


    #----------------------------------------------------------------------------------------------
    def temp_open(self, pin_id, quantity):
        seconds = float(quantity) * self.RESOURCES.get(pin_id, 0)
        self.open(pin_id)
        time.sleep(seconds)
        self.close(pin_id)
        return seconds


    #----------------------------------------------------------------------------------------------
    def change_pin_status(self, pin_id, required_status):
        pin = self.PINS.get(pin_id)
        if pin is None:
            return

        if self.status(pin) != required_status:
            self.GPIO.output(pin, required_status)
            time.sleep(0.6)


    #----------------------------------------------------------------------------------------------
    def status(self, pin):
        try:
            return self.GPIO.input(pin)
        except:
            self.GPIO.setup(pin, self.GPIO.OUT)
            return self.GPIO.input(pin)


    #----------------------------------------------------------------------------------------------
    def set_pins(self, statuses):
        for pin_id, status in statuses.iteritems():
            self.open(pin_id) if status else self.close(pin_id)
    
    
    #----------------------------------------------------------------------------------------------
    def feed(self):
        def reset_pins():
            for pin in self.MOTOR_PINS:
                self.GPIO.setup(pin, self.GPIO.OUT)
                self.GPIO.output(pin, 0)

        def invarte(direction, cycles): 
            seq = [
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
            ]
            for _ in range(cycles):
                for step in range(4):
                    for pin in range(4):
                        self.GPIO.output(direction[pin], seq[step][pin])
                        time.sleep(0.001)

        reset_pins()
        for i in range(10):
            invarte(self.MOTOR_PINS_BACK, 64)
            invarte(self.MOTOR_PINS, 128 + 64)
        reset_pins()



IO = IO_BASE(GPIO)
