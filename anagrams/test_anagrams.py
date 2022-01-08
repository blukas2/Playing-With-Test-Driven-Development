# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 18:31:09 2021

@author: Balazs
"""

# 1 Get letters from a Name into pool (list)
# 2 Get list of words from dictionary if longer than 1
# 3 Select word from dictionary if all characters are in the name character pool
### 3.1 split name into list of characters
### 3.2 chreate character count pool object for name
### 3.3 split word into list of characters
### 3.4  count letters in word
### 3.5 check if all characers of the word are in the character count pool
### 3.6 remove characters from the pool if they are used
### 3.7 remove word from dictionary

# 4 remove letters from the name pool and the word from the dictionary
# 5 continue search until all characters from the name are used up or until it is possible to find a word


import pytest
import numpy as np

exec(open('E:\\Software Engineering\\Playing with TDD\\anagrams\\anagrams.py').read())


class testAnagramGenerator:
    def __init__(self):
        pass
    def test_anagram_generator_name(self, anagram_generator=anagram_generator):
        assert type(anagram_generator.name)==str
        assert 'Balazs Lukacs'==anagramGenerator(name='Balazs Lukacs', dictionary=sample_dictionary).name
        with pytest.raises(ValueError):
            anagramGenerator(name=124, dictionary=sample_dictionary)
        with pytest.raises(ValueError):
            anagramGenerator(name='abcd', dictionary=sample_dictionary)
            
    def test_anagram_generator_dictionary(self, anagram_generator=anagram_generator):
        assert type(anagram_generator.dictionary)==list
        assert ['cat', 'dog', 'horse']==anagramGenerator(name='Balazs Lukacs', dictionary=['cat', 'dog', 'horse']).dictionary
        
        test_dict= anagramGenerator(name='Balazs Lukacs', dictionary=['cat', 'dog', 'horse', 'a']).dictionary
        assert all([len(i)>1 for i in test_dict])
        
        with pytest.raises(ValueError):
            anagramGenerator(name='Balazs Lukacs', dictionary='sample_dictionary')
            
    def test_chars_to_list(self, anagram_generator=anagram_generator):
        assert anagram_generator.chars_to_list('a')==['a']
        assert anagram_generator.chars_to_list('ab')==['a', 'b']
        assert anagram_generator.chars_to_list('a b')==['a', 'b']
        assert anagram_generator.chars_to_list('Joe')==['j', 'o', 'e']
        
    def test_name_split(self, anagram_generator=anagram_generator):
        assert (anagramGenerator(name='Balazs', dictionary=['cat', 'dog', 'horse']).name_split==['b','a','l','a','z','s'])
        
    def test_get_letter_counts(self, anagram_generator=anagram_generator):
        assert anagram_generator.get_letter_counts(['j','o','e'])=={'j':1,'o':1,'e':1}
        assert anagram_generator.get_letter_counts(['b','a','l','a','z','s'])=={'b':1,'a':2,'l':1,'z':1,'s':1}
        
    def test_name_letter_pool(self, anagram_generator=anagramGenerator(name='Balazs', dictionary=['cat', 'dog', 'horse'])):
        assert anagram_generator.get_letter_counts(anagram_generator.name_split) == anagram_generator.name_letter_pool
        assert anagram_generator.name_letter_pool_value == anagram_generator.calculate_pool_value(anagram_generator.name_letter_pool)
        
    def test_is_chr_pool_in_chr_pool(self, anagram_generator=anagram_generator):
        assert anagram_generator.is_chr_pool_in_chr_pool({'a':1,'b':1,'s':1}, {'b':1,'a':2,'l':1,'z':1,'s':1})==True
        assert anagram_generator.is_chr_pool_in_chr_pool({'a':1,'b':1,'s':2}, {'b':1,'a':2,'l':1,'z':1,'s':1})==False
        assert anagram_generator.is_chr_pool_in_chr_pool({'a':1,'b':1,'e':1}, {'b':1,'a':2,'l':1,'z':1,'s':1})==False
        
    def test_substract_chr_pool_from_chr_pool(self, anagram_generator=anagram_generator):
        assert (anagram_generator.substract_chr_pool_from_chr_pool({'a':1,'b':1,'s':1}, {'b':1,'a':2,'l':1,'z':1,'s':1})==
                {'b':0,'a':1,'l':1,'z':1,'s':0})
        
    def test_calculate_pool_value(self, anagram_generator=anagram_generator):
        assert anagram_generator.calculate_pool_value({'b':1,'a':2,'l':1,'z':1,'s':1})==6
        
    def test_select_word_from_dictionary(self):
        anagram_generator_test1=anagramGenerator(name='Balazs', dictionary=['cat','abs', 'dog'])
        anagram_generator_test1.select_word_from_dictionary()
        assert anagram_generator_test1.last_select == 'abs'
        assert anagram_generator_test1.last_select not in anagram_generator_test1.dictionary
        assert anagram_generator_test1.name_letter_pool=={'b':0,'a':1,'l':1,'z':1,'s':0}
        assert anagram_generator_test1.name_letter_pool_value==(anagram_generator_test1
                                                               .calculate_pool_value(anagram_generator_test1.name_letter_pool))
        
        anagram_generator_test2=anagramGenerator(name='Balazs', dictionary=['cat','horse', 'dog'])
        anagram_generator_test2.select_word_from_dictionary()
        assert anagram_generator_test2.last_select == None
        
    def test_collect_anagram_words(self, anagram_generator=anagramGenerator(name='Balazs Lukacs', dictionary=['cab','horse', 'sul'])):
        anagram_generator.collect_anagram_words()
        assert type(anagram_generator.anagram_wordlist)==list
        assert anagram_generator.anagram_wordlist==['cab', 'sul']

        
    
            


test_anagram_generator=testAnagramGenerator()
test_anagram_generator.test_anagram_generator_name()
test_anagram_generator.test_anagram_generator_dictionary()
test_anagram_generator.test_chars_to_list()
test_anagram_generator.test_name_split()
test_anagram_generator.test_get_letter_counts()
test_anagram_generator.test_name_letter_pool()
test_anagram_generator.test_is_chr_pool_in_chr_pool()
test_anagram_generator.test_substract_chr_pool_from_chr_pool()
test_anagram_generator.test_calculate_pool_value()
test_anagram_generator.test_select_word_from_dictionary()
test_anagram_generator.test_collect_anagram_words()

