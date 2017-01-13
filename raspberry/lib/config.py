from datetime import datetime, timedelta


###################################################################################################
class Light(object):

    #----------------------------------------------------------------------------------------------
    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            setattr(self, key, value)

    #----------------------------------------------------------------------------------------------
    def __str__(self):
        return self.id


    @property
    #----------------------------------------------------------------------------------------------
    def on_hour(self):
        hour = self.get_hour(self._on_hour)
        backup = (datetime.now() + timedelta(hours=1)).hour
        return hour if hour else backup


    @property
    #----------------------------------------------------------------------------------------------
    def off_hour(self):
        hour = self.get_hour(self._off_hour)
        backup = (datetime.now() - timedelta(hours=1)).hour
        return hour if hour else backup


    #----------------------------------------------------------------------------------------------
    def get_hour(self, hour):
        if type(hour) == int:
            return hour

        this_hour = datetime.now().hour
        if hour == "*":
            return this_hour

        if hour.startswith("*/"):
            rate = int(hour.replace("*/", ""))
            for time in range(0, 24, rate):
                if time == this_hour:
                    return this_hour

        return


###################################################################################################

TEMP_MIN = 22.0
TEMP_MAX = 28.0
WHATER_LEVEL_PIN = 5
TEMP_ID = "28-03146adc35ff"
PUSH_BULLET_AUTH = "o.nkeVGJI9f2EP9w8B6OR0O3wMzdKt3N0D"
NI_pins = ["pompa", "incalzitor"]

pins = {
    "polish":  19,
    "reflector": 16,
    "led_rgb": 23,
    "circulant": 26,
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
    Light(**{"id": "led",       "_on_hour":  6, "on_minute": 30, "_off_hour": 8, "off_minute": 30}),
    Light(**{"id": "led_rgb",   "_on_hour":  6, "on_minute": 25, "_off_hour": 8, "off_minute": 40}),


    Light(**{"id": "led_rgb",   "_on_hour": 16, "on_minute": 50, "_off_hour": 22, "off_minute": 30}),
    Light(**{"id": "led",       "_on_hour": 17, "on_minute":  0, "_off_hour": 22, "off_minute":  0}),
    Light(**{"id": "reflector", "_on_hour": 19, "on_minute": 30, "_off_hour": 19, "off_minute": 40}),


    #Light(**{"id": "polish", "_on_hour": 17, "on_minute":  0, "_off_hour": 17, "off_minute": 0}),
    Light(**{"id": "circulant", "_on_hour": "*", "on_minute":  0, "_off_hour": "*", "off_minute": 10}),
]

