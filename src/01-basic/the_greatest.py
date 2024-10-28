# -*- coding: utf-8 -*-

values_str = input()
#
def eval_bigger(values):
    bigger = 0
    str_values = values.split(" ")
    int_area_arr = list(map(lambda v: int(v), str_values))

    for i in range(len(int_area_arr)):
        if int_area_arr[i] >= bigger:
            bigger = int_area_arr[i]

    print(f"{bigger} eh o maior")

eval_bigger(values_str)
