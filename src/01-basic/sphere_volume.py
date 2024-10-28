# -*- coding: utf-8 -*-

radius_value = input()

def sphere_volume(radius_value):
    radius_value = int(radius_value)

    PI = 3.14159
    radius_pow = float(pow(radius_value, 3))
    volume = (4.0 / 3) * PI * radius_pow

    print(f"VOLUME = {volume:.3f}")


sphere_volume(radius_value)
