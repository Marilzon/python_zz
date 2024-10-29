# -*- coding: utf-8 -*-
import math

x_axes = input()
y_axes = input()


def meansure_distance(x, y):
    x_arr = x.split(" ")
    y_arr = y.split(" ")

    x_float_arr = list(map(lambda v: float(v), x_arr))
    y_float_arr = list(map(lambda v: float(v), y_arr))

    distance = math.sqrt(
        ((y_float_arr[0] - x_float_arr[0]) ** 2)
        + ((y_float_arr[1] - x_float_arr[1]) ** 2)
    )

    print(f"{distance:.4f}")


meansure_distance(x_axes, y_axes)
