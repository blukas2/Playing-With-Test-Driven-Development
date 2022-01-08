# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 17:47:39 2021

@author: Balazs
"""
file_path = 'E:\\Software Engineering\\Playing with TDD\\palingrams\\2of12inf.txt'
file = open(file_path,'r')
lines = file.readlines()
file.close()

def check_palingram(word):
    word_reverse =''
    for i in range(len(word),0,-1):
        word_reverse = word_reverse+word[i-1]        
    return word==word_reverse
    

def is_palingram(word):
    if len(word)>1:
        result=check_palingram(word)
    else:
        result=False
    return result

wordlist = ['apple', 'google', 'lol', 'swag', 'gag']

wordlist=[word.replace('\n','').replace('%','') for word in lines]

palingramlist = [word for word in wordlist if is_palingram(word)]

print(palingramlist)
