import json
import requests
from flask import request, render_template

from app.io import IO
from app.temperature import read_temp
from lib import config
from lib.db import TempCommands, Thermostats
from lib.helpers import get_statuses, send_temperature, send_alert
from lib.salus_it_600 import SalusIT600

#-------------------------------------------------------------------------------------------------
def home():
    pins = get_statuses()
    pins_order = pins.keys()
    pins_order.sort(key = lambda s: len(s))
    
    return render_template("commands.jinja2", pins=pins, pins_order=pins_order)


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
def open_pin_time(pin_id, expire_delta):
    TempCommands.add_entry({pin_id: True}, expire_delta)
    IO.open(pin_id)
    return "<h1 style='color:blue'>Hello There, {} for {} minutes</h1>".format(pin_id, expire_delta)



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
    expire_delta = 120
    if procedure == "lights_on":
        statuses = {"led_daylight": True, "led_albastru": True}
    elif procedure == "lights_off":
        statuses = {"led_daylight": False, "led_albastru": False}
    elif procedure == "movie":
        expire_delta = 150
        statuses = {"led_daylight": False, "led_albastru": True}
    elif procedure == "schimb_apa":
        statuses = {"led_daylight": True, "led_albastru": True, "pompa": False, "incalzitor": False, "circulant": False}
    elif procedure == "feed":
        expire_delta = 10
        statuses = {"pompa": False, "circulant": False}
    elif procedure == "switch_lights":
        statuses = get_statuses()
        if statuses.get("led_daylight") or statuses.get("led_albastru"):
            statuses.update({"led_daylight": False, "led_albastru": False, "reflector": False})
        else:
            statuses.update({"led_daylight": True, "led_albastru": True, "reflector": True})
    elif procedure == "reset":
        statuses = get_statuses(with_db=False)

    TempCommands.add_entry(statuses, expire_delta)
    IO.set_pins(statuses)

    if procedure == "feed":
        IO.feed()

    return procedure


#-------------------------------------------------------------------------------------------------
def thermostats():
    return json.dumps(Thermostats.get())


#-------------------------------------------------------------------------------------------------
def set_thermostats(email, paswd):
    data = SalusIT600(email, paswd).statuses
    Thermostats.add_entry(data)
    return json.dumps(data)
