# -*- coding: utf-8 -*-
from flask import make_response, request, current_app
from functools import update_wrapper

import requests
from datetime import datetime, timedelta
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


#--------------------------------------------------------------------------------------------------
def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    #----------------------------------------------------------------------------------------------
    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    #----------------------------------------------------------------------------------------------
    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers
            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            h['Access-Control-Allow-Credentials'] = 'true'
            h['Access-Control-Allow-Headers'] = \
                "Origin, X-Requested-With, Content-Type, Accept, Authorization"
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator
