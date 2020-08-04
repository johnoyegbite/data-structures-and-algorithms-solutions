# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 10:48:47 2020

@author: johnoyegbite
"""
# SOLVED!
"""Collatz Conjectrue

Take any natural number 𝑛. If 𝑛 is even, divide it by 2 to get 𝑛/2, if 𝑛 is odd multiply it by 3 and add 1 to obtain 3𝑛+1.
Repeat the process indefinitely. The conjecture is that no matter what number you start with, you will always eventually reach 1. [...]


n = 20

-> n is even
n = n/2 = 20/2 = 10

-> n is still even
n = n/2 = 10/2 = 5

-> n is odd
n = 3n+1 = 3(5) + 1 = 16

-> n is even
n = n/2 = 16/2 = 8

-> n is even
n = n/2 = 8/2 = 4

-> n is even
n = n/2 = 4/2 = 2

-> n is even
n = n/2 = 2/2 = 1 # HALT
"""


def conjecture(n):
    conjected = []
    steps = 0
    while n != 1:
      if n % 2 == 0:
        n = n/2.0
      else:
        n = 3*n + 1
      conjected.append(n)
      steps += 1
    return conjected, steps
    return conjected

def conjecture_tree(n, steps=0):
    if n == 1:
        return steps
    if n % 2 == 0:
        n = n /2.0
    else:
        n = 3*n + 1
    steps += 1
    return conjecture_tree(n, steps)


if __name__ == "__main__":
    n = 3
    print(conjecture(n))
    print(conjecture_tree(n))
    