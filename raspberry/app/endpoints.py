import time
from app.io import IO
from app.cron import Cron
from lib.config import config
from lib.helpers import get_statuses, get_times
from lib.db import TempCommands, session

#-------------------------------------------------------------------------------------------------
def home():
    return "<h1 style='color:blue'>Hello There!</h1>"


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
def set_times_to_cron():
    times = Cron.set_times()
    return str(times)


#-------------------------------------------------------------------------------------------------
def temperature():
    return "temp is 29.7"


#-------------------------------------------------------------------------------------------------
def temperature_save():
    return "temp is 29.7"


#--------------------------------------------------------------------------------------------------
def doser(pin_id, quantity):
    seconds = IO.temp_open(pin_id, quantity)
    return "just dosed '{}' for {} seconds".format(pin_id, seconds)


#--------------------------------------------------------------------------------------------------
def reload_pins():
    statuses = get_statuses()
    obj = TempCommands.get()
    if obj is not None:
        statuses.update(obj.statuses)
    IO.set_pins(statuses)

    return str(statuses)


#-------------------------------------------------------------------------------------------------
def set_procedure(procedure):
    #statuses = get_statuses(procedure)
    statuses = {}
    if procedure == "lights_on":
        statuses = {"865": True, "830": True}
    elif procedure == "lights_off":
        statuses = {"865": False, "830": False, "led": False}
    elif procedure == "movie":
        statuses = {"865": False, "830": False, "led": True}
    elif procedure == "reset":
        TempCommands.clear_all()
        statuses = get_statuses()


    obj = TempCommands.add_entry(statuses)
    IO.set_pins(statuses)

    return procedure
