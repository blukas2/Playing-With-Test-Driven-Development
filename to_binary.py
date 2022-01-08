# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 17:29:08 2021

@author: Balazs
"""

import pytest

import math

def calc_power(place_value):
    return place_value-1

def to_binary(n):
    if n==0:
        num_of_place_value = 1
    else:
        num_of_place_value = math.floor(math.log(n,2))+1
                
    value_accounted = 0
    string_digits = ''
    for i in range(num_of_place_value,0,-1):
        remaining_value = n-value_accounted
        power = i-1
        power_value = 2**power        
        number_at_place_value = remaining_value//power_value    
        value_at_place_value = number_at_place_value*power_value
        value_accounted=value_accounted+value_at_place_value
        string_digits = string_digits + str(number_at_place_value)
    return int(string_digits)
        

def test_to_binary():
    assert to_binary(0)==0
    assert to_binary(1)==1
    assert to_binary(2)==10
    assert to_binary(3)==11
    assert to_binary(4)==100
    assert to_binary(5)==101
    assert to_binary(6)==110
    assert to_binary(1689)==11010011001
 