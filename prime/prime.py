#!/usr/bin/env python

from math import sqrt
import json

def check(n, p):
   """finds n numbers congruent to 1 mod p"""
   data = [(i * p) + 1 for i in range(n)]
   
   return {i:check_prime(i) for i in data}

def check_prime(num):
    """checks if a number is prime"""
    if num <= 1:
       return False
    for i in range(2, int(sqrt(num)) + 1):
       if num % i == 0:
          return False
    return True

def print_data(n=10, p=4, file='data.json'):
   """writes output data to a file"""
   data = check(n, p)
   f = {k:v for k,v in data.items() if not v}
   t = {k:v for k,v in data.items() if v}
   data = {'false': f, 'true': t}
   with open(file, 'w') as f:
      f.write(json.dumps(data))

if __name__ == '__main__':
   print_data(100)
        