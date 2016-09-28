
###################################################################################################
class Light(object):

    #----------------------------------------------------------------------------------------------
    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            setattr(self, key, value)

    #----------------------------------------------------------------------------------------------
    def __str__(self):
        return self.id


###################################################################################################

TEMP_MIN = 22.0
TEMP_MAX = 28.0
WHATER_LEVEL_PIN = 5
TEMP_ID = "28-03146adc35ff"
PUSH_BULLET_AUTH = "o.nkeVGJI9f2EP9w8B6OR0O3wMzdKt3N0D"
NI_pins = ["pompa", "incalzitor"]

pins = {
    "865":  19,
    "reflector": 16,
    "led_rgb": 23,
    "co2": 	26,
    "pompa": 20,
    "incalzitor": 21,
    "micro": 22,
    "macro": 24,
    "fier":  27,
    "twinstar": 13,
    "led": 6,
    "supplemental_pin2": 12
}
resources = {
    "micro": 3.6,
    "macro": 3.6,
    "fier": 3.6,
    "twinstar": 1
}
lights = [
    Light(**{"id": "led",       "on_hour":  5, "on_minute": 50, "off_hour": 8, "off_minute": 30}),
    Light(**{"id": "led_rgb",   "on_hour":  5, "on_minute": 40, "off_hour": 8, "off_minute": 40}),


    Light(**{"id": "led",       "on_hour": 17, "on_minute":  0, "off_hour": 19, "off_minute": 35}),
    Light(**{"id": "led_rgb",   "on_hour": 16, "on_minute": 50, "off_hour": 22, "off_minute": 30}),
    Light(**{"id": "reflector", "on_hour": 19, "on_minute": 30, "off_hour": 22, "off_minute":  0}),


    Light(**{"id": "865", "on_hour": 17, "on_minute":  0, "off_hour": 17, "off_minute": 0}),
]

