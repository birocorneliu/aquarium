
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
config = {
    "temp_id": "28-03146adc35ff",
    "pin_list": [],
    "NI_pins": ["pompa", "incalzitor"],
    "pins": {
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
        "supplemental_pin2": 12,
    },
    "resources": {
        "micro": 3.3,
        "macro": 3.3,
        "fier": 3.3,
        "twinstar": 1
    },
    "lights": [
        Light(**{"id": "co2", "on_hour":  6, "on_minute":  0, "off_hour":  9, "off_minute": 30}),
        Light(**{"id": "led", "on_hour":  7, "on_minute":  0, "off_hour":  7, "off_minute": 50}),
        Light(**{"id": "830", "on_hour":  7, "on_minute": 20, "off_hour": 10, "off_minute":  0}),
        Light(**{"id": "865", "on_hour":  7, "on_minute": 50, "off_hour":  9, "off_minute": 30}),
        Light(**{"id": "led", "on_hour":  9, "on_minute": 30, "off_hour": 10, "off_minute": 30}),


        Light(**{"id": "co2", "on_hour": 15, "on_minute":  0, "off_hour": 20, "off_minute": 30}),
        Light(**{"id": "led", "on_hour": 17, "on_minute":  0, "off_hour": 18, "off_minute":  0}),
        Light(**{"id": "830", "on_hour": 17, "on_minute": 40, "off_hour": 22, "off_minute":  0}),
        Light(**{"id": "865", "on_hour": 18, "on_minute":  0, "off_hour": 21, "off_minute": 30}),
        Light(**{"id": "led", "on_hour": 21, "on_minute": 30, "off_hour": 22, "off_minute": 45}),
    ],
}

