# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 17:48:12 2021

@author: Balazs
"""

exec(open('E:\\Software Engineering\\Playing with TDD\\palingrams\\palingrams.py').read())

def test_is_palingram():
    assert is_palingram('apple')==False
    assert is_palingram('gag')==True
    assert is_palingram('sexes')==True
    assert is_palingram(' ')==False
    assert is_palingram('')==False
    
test_is_palingram()


def test_palingram_list():
    assert all([is_palingram(palingram) for palingram in palingramlist])

test_palingram_list()
