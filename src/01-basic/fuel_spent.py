# -*- coding: utf-8 -*-

spent_time = input()
average_speed = input()


def fuel_spent(spent_time, average_speed):
    spent_time, average_speed = int(spent_time), int(average_speed)
    distance = spent_time * average_speed
    fuel = distance / 12

    print(f"{fuel:.3f}")


fuel_spent(spent_time, average_speed)
