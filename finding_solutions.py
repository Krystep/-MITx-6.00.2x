# -*- coding: utf-8 -*-
"""
Created on Sun May  1 13:56:56 2022

@author: Krystyna
"""

def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    x = 0
    for i in range(1, 1000):
        if test(x):
            return abs(x)
        else: 
            if i%2 == 1:
                x+=i
            else:
                x-=i

#### This test case prints 49 ####
def f(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))

#### This test case prints 0 ####
def f(x):
    return x == 0
print(solveit(f))
