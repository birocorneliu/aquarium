import time
from io import GPIO, pinList, pin
from lib.helpers import get_statuses, config

#--------------------------------------------------------------------------------------------------
def home():
    return "<h1 style='color:blue'>Hello There!</h1>"


#--------------------------------------------------------------------------------------------------
def open_pin(pin_no):
    pin("open", pin_no)
    return "<h1 style='color:blue'>Hello There, {}</h1>".format(pin_no)


#--------------------------------------------------------------------------------------------------
def close_pin(pin_no):
    pin("close", pin_no)
    return "<h1 style='color:blue'>Hello There, {}</h1>".format(pin_no)


#--------------------------------------------------------------------------------------------------
def dose_pump(pump_id, ml_quantity):
    return "<h1 style='color:blue'>Hello There, pump_id={}, quantity={}</h1>".format(
        pump_id, ml_quantity)


#--------------------------------------------------------------------------------------------------
def temperature():
    return "temp is 29.7"


#--------------------------------------------------------------------------------------------------
def temperature_save():
    return "temp is 29.7"


#--------------------------------------------------------------------------------------------------
def doser(resource, quantity):
    resources = {
  	"micro": 	2.3,
	"macro": 	2.3,
	"fier": 	4,
	"twinstar": 	1
    }
    seconds = float(quantity) * resources[resource]
    pin("open", resource)
    time.sleep(seconds)
    pin("close", resource)

    return "just dosed '{}' for {} seconds".format(resource, seconds)


#--------------------------------------------------------------------------------------------------
def reload_pins():
    pins = {
	"co2": 1,
	"led": 2,
	"865": 3,
	"830": 4
    }
    statuses = get_statuses()
    for id, status in statuses.iteritems():
	if status:
	    pin("open", pins[id])
	else:
	    pin("close", pins[id])

    return str(statuses) 
   




