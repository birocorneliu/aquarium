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
TEMP_ID = "28-03146aca73ff"
NI_pins = ["filtru", "incalzitor"]
pins = {
    "feeder": 7, 

    "led_4000": 9,
    "led_rgb":  25,
    "led_6500": 8,

    "filtru_uv": 11,
    "circulant": 10,
    "incalzitor": 24,
    "filtru": 22,
}
resources = {
    "feeder": 3.8,
}
lights = [
    Light(**{"id": "led_rgb",   "_on_hour":  6, "on_minute":  0, "_off_hour": 21, "off_minute":  0}),
    Light(**{"id": "led_6500",  "_on_hour":  9, "on_minute":  0, "_off_hour": 16, "off_minute": 30}),
    Light(**{"id": "led_4000",  "_on_hour":  9, "on_minute": 30, "_off_hour": 16, "off_minute":  0}),

    Light(**{"id": "filtru_uv", "_on_hour": 21, "on_minute":  0, "_off_hour":  5, "off_minute":  0}),

]

