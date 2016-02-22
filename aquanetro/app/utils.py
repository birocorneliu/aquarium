from datetime import datetime

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
