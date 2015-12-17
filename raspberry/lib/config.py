
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
    "pin_list": [27, 3, 4, 17],
    "pins": {
        "865":  4,
        "830": 	17,
        "co2": 	None,
        "pompa": None,
        "micro": None,
        "macro": None,
        "fier":  None,
        "twinstar": 3,
    },
    "resources": {
        "micro": 2.3,
        "macro": 2.3,
        "fier": 2.3,
        "twinstar": 20
    },
    "lights": [
        Light(**{"id": "co2", "on_hour":  6, "on_minute":  0, "off_hour":  9, "off_minute": 30}),
        Light(**{"id": "led", "on_hour":  7, "on_minute":  0, "off_hour":  7, "off_minute": 20}),
        Light(**{"id": "865", "on_hour":  7, "on_minute": 20, "off_hour": 10, "off_minute":  0}),
        Light(**{"id": "830", "on_hour":  7, "on_minute": 50, "off_hour":  9, "off_minute": 30}),
        Light(**{"id": "led", "on_hour": 10, "on_minute": 15, "off_hour": 10, "off_minute": 20}),

        Light(**{"id": "co2", "on_hour": 15, "on_minute":  0, "off_hour": 20, "off_minute": 30}),
        Light(**{"id": "led", "on_hour": 17, "on_minute": 20, "off_hour": 17, "off_minute": 40}),
        Light(**{"id": "865", "on_hour": 17, "on_minute": 40, "off_hour": 22, "off_minute":  0}),
        Light(**{"id": "830", "on_hour": 18, "on_minute":  0, "off_hour": 21, "off_minute": 30}),
        Light(**{"id": "led", "on_hour": 22, "on_minute":  0, "off_hour": 22, "off_minute": 30}),
    ],
}

