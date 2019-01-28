import json
import requests
from datetime import datetime
from retrying import retry

from app.temperature import read_temp
from lib import config
from lib.db import TempCommands


@retry(stop_max_attempt_number=10, wait_fixed=1000)
#-------------------------------------------------------------------------------------------------
def send_temperature():
    temp = read_temp()
    data = {"temperature": temp}
    response = requests.post("http://aquanet.ro/temperature", data=data)

    return response.content


#--------------------------------------------------------------------------------------------------
def get_statuses():
    status = {pin_id: True for pin_id in config.NI_pins}
    current = datetime.now().replace(second=0, microsecond=0)
    for light in config.lights:
        start =  current.replace(hour=light.on_hour,  minute=light.on_minute)
        finish = current.replace(hour=light.off_hour, minute=light.off_minute)
        status.setdefault(light.id, False)
        if start < current < finish:
            status[light.id] = True

    obj = TempCommands.get()
    if obj is not None:
        status.update(obj.statuses)

    return status


#--------------------------------------------------------------------------------------------------
def get_times():
    times = []
    for light in config.lights:
        if (light.on_hour, light.on_minute) not in times:
            times.append((light.on_hour, light.on_minute))

    return times


#--------------------------------------------------------------------------------------------------
def send_alert(body, title="Alerta acvariu"):
    url = "https://api.pushbullet.com/v2/pushes"
    headers = {
        "Access-Token": "o.nkeVGJI9f2EP9w8B6OR0O3wMzdKt3N0D",
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "title": title,
        "body": body,
        "type": "note"
    })
    response = requests.post(url, headers=headers, data=data)

