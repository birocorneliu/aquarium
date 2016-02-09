
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
    "pin_list": [18, 24, 23, 25, 8, 7, 11, 9, 10, 17, 22],
    "NI_pins": ["pompa", "incalzitor"],
    "pins": {
        "865":  9,
        "830": 	10,
        "led": 17,
        "co2": 	25,
        "pompa": 22,
        "incalzitor": 7,
        "micro": 24,
        "macro": 23,
        "fier":  18,
        "twinstar": 11,
        "supplemental_pin": 8,
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

