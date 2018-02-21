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
    "led_albastru":  19,
    "led_daylight": 16,
    "led_rgb_12v": 23,
    "circulant": 26,
    "pompa": 20,
    "incalzitor": 21,
    "micro": 22,
    "macro": 24,
    "fier":  27,
    "twinstar": 13,
    "led_12v": 6,
    "supplemental_pin2": 12
}
button_pins = {
    "reset": 11, #green
    "schimb_apa": 9, #red
    "feed": 10, #yellow
    "switch_lights": 5, #black
}
resources = {
    "micro": 3.6,
    "macro": 3.6,
    "fier": 3.6,
    "twinstar": 1
}
lights = [
    #Light(**{"id": "led",       "_on_hour":  6, "on_minute": 30, "_off_hour": 8, "off_minute": 30}),
    Light(**{"id": "led_daylight",       "_on_hour":  6, "on_minute": 30, "_off_hour": 8, "off_minute": 30}),
    Light(**{"id": "led_albastru",   "_on_hour":  6, "on_minute": 25, "_off_hour": 8, "off_minute": 40}),


    Light(**{"id": "led_albastru",   "_on_hour": 16, "on_minute": 50, "_off_hour": 22, "off_minute": 30}),
    #Light(**{"id": "led",       "_on_hour": 17, "on_minute":  0, "_off_hour": 22, "off_minute":  0}),
    Light(**{"id": "led_daylight",       "_on_hour": 17, "on_minute":  0, "_off_hour": 22, "off_minute":  0}),



    #Light(**{"id": "polish", "_on_hour": 17, "on_minute":  0, "_off_hour": 17, "off_minute": 0}),
    #Light(**{"id": "circulant", "_on_hour": 17, "on_minute": 10, "_off_hour": 21, "off_minute": 50}),
    Light(**{"id": "circulant", "_on_hour": "*", "on_minute":  0, "_off_hour": "*", "off_minute": 10}),
    Light(**{"id": "circulant", "_on_hour": "*", "on_minute": 20, "_off_hour": "*", "off_minute": 30}),
    Light(**{"id": "circulant", "_on_hour": "*", "on_minute": 40, "_off_hour": "*", "off_minute": 50}),
]

