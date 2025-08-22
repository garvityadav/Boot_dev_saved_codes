import math


def log_scale(data, base):
    return [math.log(item, base) for item in data]
