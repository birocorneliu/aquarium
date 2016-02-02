
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
    "pin_list": [27, 3, 22, 17],
    "pins": {
        "865":  22,
        "830": 	17,
        "led": 27,
        "co2": 	None,
        "pompa": None,
        "micro": 25,
        "macro": 24,
        "fier":  23,
        "twinstar": 3,
    },
    "resources": {
        "micro": 4.1,
        "macro": 4.1,
        "fier": 4.1,
        "twinstar": 1
    },
    "lights": [
        Light(**{"id": "co2", "on_hour":  6, "on_minute":  0, "off_hour":  9, "off_minute": 30}),
        Light(**{"id": "led", "on_hour":  7, "on_minute":  0, "off_hour":  7, "off_minute": 21}),
        Light(**{"id": "865", "on_hour":  7, "on_minute": 20, "off_hour": 10, "off_minute":  1}),
        Light(**{"id": "830", "on_hour":  7, "on_minute": 50, "off_hour":  9, "off_minute": 30}),
        Light(**{"id": "led", "on_hour": 10, "on_minute":  0, "off_hour": 10, "off_minute": 30}),


        Light(**{"id": "co2", "on_hour": 15, "on_minute":  0, "off_hour": 20, "off_minute": 30}),
        Light(**{"id": "led", "on_hour": 17, "on_minute":  0, "off_hour": 17, "off_minute": 41}),
        Light(**{"id": "865", "on_hour": 17, "on_minute": 40, "off_hour": 22, "off_minute":  1}),
        Light(**{"id": "830", "on_hour": 18, "on_minute":  0, "off_hour": 21, "off_minute": 30}),
        Light(**{"id": "led", "on_hour": 22, "on_minute":  0, "off_hour": 22, "off_minute": 30}),
    ],
}

