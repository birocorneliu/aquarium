
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

temp_id = "28-03146adc35ff"
NI_pins = ["pompa", "incalzitor"]
WHATER_LEVEL_PIN = 5
pins = {
    "865":  19,
    "830": 	16,
    "led": 23,
    "co2": 	26,
    "pompa": 20,
    "incalzitor": 21,
    "micro": 22,
    "macro": 24,
    "fier":  27,
    "twinstar": 13,
    "supplemental_pin1": 6,
    "supplemental_pin2": 12
}
resources = {
    "micro": 3.3,
    "macro": 3.3,
    "fier": 3.3,
    "twinstar": 1
}
lights = [
    Light(**{"id": "co2", "on_hour":  5, "on_minute": 40, "off_hour": 7, "off_minute": 30}),
    Light(**{"id": "830", "on_hour":  6, "on_minute":  0, "off_hour": 8, "off_minute":  0}),
    Light(**{"id": "865", "on_hour":  6, "on_minute": 10, "off_hour": 7, "off_minute": 50}),


    Light(**{"id": "co2", "on_hour": 15, "on_minute": 30, "off_hour": 20, "off_minute": 30}),
    Light(**{"id": "830", "on_hour": 16, "on_minute": 40, "off_hour": 22, "off_minute":  0}),
    Light(**{"id": "865", "on_hour": 17, "on_minute":  0, "off_hour": 21, "off_minute": 30}),
    Light(**{"id": "led", "on_hour": 21, "on_minute": 30, "off_hour": 22, "off_minute": 30}),
]

