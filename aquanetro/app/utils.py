import json
import urllib2
from datetime import datetime


#--------------------------------------------------------------------------------------------------
def get_light():

    light_intensity = 0
    lights = [
        [30, {"on": [ 7, 00], "off": [ 7, 20]}],
        [39, {"on": [ 7, 20], "off": [10, 00]}],
        [39, {"on": [ 7, 50], "off": [ 9, 30]}],
        [30, {"on": [10, 00], "off": [10, 20]}],

        [30, {"on": [17, 20], "off": [17, 40]}],
        [39, {"on": [17, 40], "off": [22, 00]}],
        [39, {"on": [18, 00], "off": [21, 35]}],
        [30, {"on": [22, 00], "off": [22, 30]}],
    ]
    co2 = [
        [50, {"on": [ 6, 00], "off": [ 9, 30]}],
        [50, {"on": [15, 00], "off": [20, 30]}],
    ]
    time = datetime.now().replace(second=0, microsecond=0)
    hour = 5
    minute = 30
    watts = []
    co2_stat = 0

    for i in range(1080):
        for watt, status in lights:
            if status["on"] == [hour, minute]:
                light_intensity += watt
            if status["off"] == [hour, minute]:
                light_intensity -= watt
        for watt, status in co2:
            if status["on"] == [hour, minute]:
                co2_stat += watt
            if status["off"] == [hour, minute]:
                co2_stat -= watt

        watts.append({
            "date": time.replace(hour=hour, minute=minute),
            "light_intensity": light_intensity,
            "co2_stat": co2_stat
        })
        minute += 1
        if minute == 60:
            hour += 1
            minute = 0

    return watts


FACEBOOK_ID = "1566961360262390"
FACEBOOK_SECRET = "19739dd9f84b9015d46edb0b0ffbcd93"

#Oauth 2 Facebook login
#--------------------------------------------------------------------------------------------------
def connect_user_through_facebook(access_token):
    app_id = FACEBOOK_ID
    app_secret = FACEBOOK_SECRET
    url = "https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s" % (
        app_id, app_secret, access_token)
    result = urllib2.urlopen(url).read()

    # Use token to get user info from API
    userinfo_url = "https://graph.facebook.com/v2.2/me"
    # strip expire tag from access token
    token = result.split("&")[0]

    # Get user picture
    url = "https://graph.facebook.com/v2.2/me/picture?%s&redirect=0&height=200&width=200" % token
    result = urllib2.urlopen(url).read()
    data = json.loads(result)
    picture = data["data"]["url"]

    #Get user data
    url = "https://graph.facebook.com/v2.2/me?%s" % token
    result = urllib2.urlopen(url).read()
    data = json.loads(result)

    # The token must be stored in the login_session in order to properly logout, let"s strip out the information before the equals sign in our token
    stored_token = token.split("=")[1]

    # see if user exists

    return {
        "name": data["name"],
        "picture": picture,
        "access_token": stored_token,
    }


