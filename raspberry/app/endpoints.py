
#--------------------------------------------------------------------------------------------------
def home():
    return "<h1 style='color:blue'>Hello There!</h1>"


#--------------------------------------------------------------------------------------------------
def open_pin(pin_no):
    return "<h1 style='color:blue'>Hello There, {}</h1>".format(pin_no)


#--------------------------------------------------------------------------------------------------
def close_pin(pin_no):
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
