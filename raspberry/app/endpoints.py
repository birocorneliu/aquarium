import time
from app.io import IO
from app.cron import Cron
from lib.config import config
from lib.helpers import get_statuses, get_times

#--------------------------------------------------------------------------------------------------
def home():
    return "<h1 style='color:blue'>Hello There!</h1>"


#--------------------------------------------------------------------------------------------------
def open_pin(pin_id):
    IO.open(pin_id)
    return "<h1 style='color:blue'>Hello There, {}</h1>".format(pin_id)


#--------------------------------------------------------------------------------------------------
def close_pin(pin_id):
    IO.close(pin_id)
    return "<h1 style='color:blue'>Hello There, {}</h1>".format(pin_id)


#--------------------------------------------------------------------------------------------------
def set_times_to_cron():
    times = Cron.set_times()
    return str(times)


#--------------------------------------------------------------------------------------------------
def temperature():
    return "temp is 29.7"


#--------------------------------------------------------------------------------------------------
def temperature_save():
    return "temp is 29.7"


#--------------------------------------------------------------------------------------------------
def doser(pin_id, quantity):
    seconds = IO.temp_open(pin_id, quantity)
    return "just dosed '{}' for {} seconds".format(pin_id, seconds)


#--------------------------------------------------------------------------------------------------
def reload_pins():
    statuses = get_statuses()
    for pin_id, status in statuses.iteritems():
        IO.open(pin_id) if status else IO.close(pin_id)
    return str(statuses)

