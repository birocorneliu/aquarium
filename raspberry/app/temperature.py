from lib.config import config

PATH_PREFIX = "/sys/bus/w1/devices"
PATH_SUFIX = "w1_slave"

def read_temp():
    path = "{}/{}/{}".format(PATH_PREFIX, config["temp_id"], PATH_SUFIX)

    with open(path) as file_obj:
        data = [line.strip() for line in file_obj.readlines()]

    if data[0][-3:] != "YES" or len(data[1].split("t=")) != 2:
        raise ValueError("Can't read temperature")

    return float(data[1].split("t=")[1]) / 1000.0
