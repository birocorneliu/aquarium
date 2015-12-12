from datetime import datetime
class Light(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            setattr(self, key, value)
        
    def __str__(self):
        return self.id

    @property
    def pin(self):
	return config["pin"][self.id]
        

config = {
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
    "doser":[
        {"id": "twn", "on_hour": "ALL", "on_minute": "HALF", "period": 30},
    ]
}

#--------------------------------------------------------------------------------------------------
def get_statuses():
    status = {}
    current = datetime.now().replace(second=0, microsecond=0)
    for light in config["lights"]: 
        start =  current.replace(hour=light.on_hour,  minute=light.on_minute)
        finish = current.replace(hour=light.off_hour, minute=light.off_minute)
        status.setdefault(light.id, (light, False))
        if start < current < finish:
            status[light.id] = (light, True)

    return status


#--------------------------------------------------------------------------------------------------
def get_times():
    times = []
    for light in config["lights"]:
        if (light.on_hour, light.on_minute) not in times:
            times.append((light.on_hour, light.on_minute))
    
    return times
        


