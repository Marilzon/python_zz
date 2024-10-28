# -*- coding: utf-8 -*-

x_value = input()
y_value = input()


def simple_price_sum(x, y):

    x_value = float(x.split()[2])
    y_value = float(y.split()[2])

    x_volume = float(x.split()[1])
    y_volume = float(y.split()[1])

    result = (x_value * x_volume) + (y_value * y_volume)
    message = "VALOR A PAGAR: R$ {:.2f}".format(result)
    print(message)


simple_price_sum(x_value, y_value)
