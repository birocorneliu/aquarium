import json
import requests
from flask import request
from datetime import datetime, timedelta
from dateutil.parser import parse

from app.io import IO
from app.temperature import read_temp
from lib import helpers 
from lib.db import Temperature, TempCommands
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
        helpers.send_alert(message)
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
        return helpers.send_temperature()


#-------------------------------------------------------------------------------------------------
def pc_stats():
    return json.dumps({
        "memory_indo": helpers.get_ram_info(),
        "cpu_info": {
            "temperature": helpers.get_cpu_temperature(),
            "load": helpers.get_cpu_use()
        },
    })


#-------------------------------------------------------------------------------------------------
def set_temperature():
    temperature = str(read_temp())
    Temperature.add_entry(temperature)

    return temperature


#-------------------------------------------------------------------------------------------------
def get_temperatures():
    end_date = request.args.get("end_date")
    end_date = parse(end_date) if end_date else datetime.now()
    start_date = request.args.get("start_date")
    start_date = parse(start_date) if start_date else end_date - timedelta(days=3)
    temps = Temperature.get(start_date, end_date)
   
    data = []
    for temp in temps:
        data.append({
            "temperature": temp.temperature, 
            "register_date": temp.register_date.strftime("%Y-%m-%d %H:%M")
        })
    return json.dumps(data)


#--------------------------------------------------------------------------------------------------
def doser(pin_id, quantity):
    seconds = IO.temp_open(pin_id, quantity)
    return "just dosed '{}' for {} seconds".format(pin_id, seconds)


#--------------------------------------------------------------------------------------------------
def status():
    return json.dumps(helpers.get_statuses())


#-------------------------------------------------------------------------------------------------
def reload_pins():
    statuses = helpers.get_statuses()
    IO.set_pins(statuses)

    return str(statuses)


#-------------------------------------------------------------------------------------------------
def set_procedure(procedure):
    statuses = {}
    expire_delta = 120
    if procedure == "lights_on":
        statuses = {"led_4000": True, "led_6500": True}
    elif procedure == "lights_off":
        statuses = {"led_4000": False, "led_6500": False}
    elif procedure == "movie":
        expire_delta = 150
        statuses = {"led_4000": False, "led_6500": True}
    elif procedure == "schimb_apa":
        statuses = {"led_4000": True, "led_6500": True, "filtru": False, "incalzitor": False, "circulant": False}
    elif procedure == "feed":
        expire_delta = 10
        statuses = {"filtru": False, "circulant": False}
    elif procedure == "switch_lights":
        statuses = helpers.get_statuses()
        if statuses.get("led_4000") or statuses.get("led_6500"):
            statuses.update({"led_4000": False, "led_6500": False, "reflector": False})
        else:
            statuses.update({"led_4000": True, "led_6500": True, "reflector": True})
    elif procedure == "reset":
        TempCommands.clear_all()
        statuses = helpers.get_statuses(with_db=False)

    TempCommands.add_entry(statuses, expire_delta)
    IO.set_pins(statuses)

    return procedure
