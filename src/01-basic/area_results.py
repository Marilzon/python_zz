# -*- coding: utf-8 -*-

area_str = input()

def process_area(area_str):
    PI = 3.14159
    str_area_arr = area_str.split(" ")
    float_area_arr = list(map(lambda v: float(v), str_area_arr))
    a, b, c = float_area_arr

    triangle = (a * c) / 2.0
    circle = PI * (c ** 2.0)
    trapezium = ((a + b) * c) / 2.0
    square = b ** 2
    rectangle = a * b

    print(f"TRIANGULO: {triangle:.3f}")
    print(f"CIRCULO: {circle:.3f}")
    print(f"TRAPEZIO: {trapezium:.3f}")
    print(f"QUADRADO: {square:.3f}")
    print(f"RETANGULO: {rectangle:.3f}")

process_area(area_str)
