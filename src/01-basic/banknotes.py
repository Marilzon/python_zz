# -*- coding: utf-8 -*-

input = input()

def get_banknotes(value):
  amount = int(value)
  bank_values = [100, 50, 20, 10, 5, 2, 1]
  print(amount)
  for i in bank_values:
    print(f"{int(amount / i)} nota(s) de R$ {i},00")
    amount -= int(amount / i) * i
  
get_banknotes(input)