# -*- coding: utf-8 -*-

x_input = input()
y_input = input()


def calc_consumption(x, y):
    x = int(x)
    y = float(y)
    consumption = x / y

    print(f"{consumption:.3f} km/l")


calc_consumption(x_input, y_input)
