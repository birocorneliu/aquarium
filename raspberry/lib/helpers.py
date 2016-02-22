import requests
from datetime import datetime
from retrying import retry

from lib.config import config
from app.temperature import read_temp


@retry(stop_max_attempt_number=10, wait_fixed=1000)
#-------------------------------------------------------------------------------------------------
def send_temperature():
    temp = read_temp()
    data = {"temperature": temp}
    response = requests.post("http://aquanet.ro/temperature", data=data)

    return response.content


#--------------------------------------------------------------------------------------------------
def get_statuses():
    status = {pin_id: True for pin_id in config["NI_pins"]}
    current = datetime.now().replace(second=0, microsecond=0)
    for light in config["lights"]:
        start =  current.replace(hour=light.on_hour,  minute=light.on_minute)
        finish = current.replace(hour=light.off_hour, minute=light.off_minute)
        status.setdefault(light.id, False)
        if start < current < finish:
            status[light.id] = True

    return status


#--------------------------------------------------------------------------------------------------
def get_times():
    times = []
    for light in config["lights"]:
        if (light.on_hour, light.on_minute) not in times:
            times.append((light.on_hour, light.on_minute))

    return times

