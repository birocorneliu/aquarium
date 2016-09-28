import json
import requests
from flask import request

from app.io import IO
from app.temperature import read_temp
from lib.helpers import get_statuses, send_temperature, send_alert
from lib.db import TempCommands
from lib import config

#-------------------------------------------------------------------------------------------------
def home():
    return "<h1 style='color:blue'>Hello There!</h1>"


#-------------------------------------------------------------------------------------------------
def find_issues():
    if config.TEMP_MIN < read_temp()< config.TEMP_MAX:
        return "Status OK, temp: {} Celsius".format(read_temp())
    else:
        message = "Status NOT OK, temp: {} Celsius".format(read_temp())
        send_alert(message)
        return message


#-------------------------------------------------------------------------------------------------
def open_pin(pin_id):
    obj = TempCommands.add_entry({pin_id: True})
    IO.open(pin_id)
    return "<h1 style='color:blue'>Hello There, {}</h1>".format(pin_id)


#-------------------------------------------------------------------------------------------------
def close_pin(pin_id):
    obj = TempCommands.add_entry({pin_id: False})
    IO.close(pin_id)
    return "<h1 style='color:blue'>Hello There, {}</h1>".format(pin_id)


#-------------------------------------------------------------------------------------------------
def temperature():
    if request.method == "GET":
        return str(read_temp())
    else:
        return send_temperature()


#-------------------------------------------------------------------------------------------------
def get_temperatures():
    response = requests.get("http://aquanet.ro/temperature")
    return response.content


#--------------------------------------------------------------------------------------------------
def doser(pin_id, quantity):
    seconds = IO.temp_open(pin_id, quantity)
    return "just dosed '{}' for {} seconds".format(pin_id, seconds)


#--------------------------------------------------------------------------------------------------
def status():
    return json.dumps(get_statuses())


#-------------------------------------------------------------------------------------------------
def reload_pins():
    statuses = get_statuses()
    IO.set_pins(statuses)

    return str(statuses)


#-------------------------------------------------------------------------------------------------
def set_procedure(procedure):
    statuses = {}
    db_save = True
    expire_delta = 120
    if procedure == "lights_on":
        statuses = {"865": True, "led": True, "led_rgb": True}
    elif procedure == "lights_off":
        statuses = {"865": False, "led": False, "led_rgb": False}
    elif procedure == "movie":
        expire_delta = 150
        statuses = {"865": False, "led": False, "led_rgb": True}
    elif procedure == "schimb_apa":
        statuses = {"865": False, "led": True, "led_rgb": True, "pompa": False, "incalzitor": False}
    elif procedure == "feed":
        expire_delta = 10
        statuses = {"pompa": False}
    elif procedure == "reset":
        db_save = False
        TempCommands.clear_all()
        statuses = get_statuses()

    if db_save:
        TempCommands.add_entry(statuses, expire_delta)

    IO.set_pins(statuses)

    return procedure
