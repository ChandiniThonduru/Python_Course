# factorial of a number
import math


def fact(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num * fact(num - 1)


def logTen(num):
    return math.log10(num)


def degToRadian(num):
    return num * (math.pi / 180)


def sine_cos_tan(angle):
    return math.sin(angle), math.cos(angle), math.tan(angle)



