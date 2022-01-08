# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 22:29:20 2022

@author: Balazs
"""

# 1 The Name
### 1.1 Get letters from a Name into a list of letters
### 1.2 create a pool from the list

# 2 The dictionary
### 2.1 Get list of words from dictionary if longer than 1
### 2.2 Get only those words from the dictionary where all characters are in the name

# 3 Get anagrams
### 3.1 Generate all combinations of words from the dictionary where the number of characters is the same as in the name
### 3.1 Keep only those combinations where the number of each and every character is the same


import pytest
import numpy as np

exec(open('E:\\Software Engineering\\Playing with TDD\\anagrams\\anagrams_v2.py').read())


class testHelperFunctions:
    def __init__(self):
        pass
    
    def test_get_unique_values_from_list(self):
        mylist = ['a', 'a', 'b', 'c', 'c']
        assert get_unique_elements_from_list(mylist)==['a','b','c']        
        mylist2 = [[2,2],[3,3],[2,4],[2,4]]
        assert get_unique_elements_from_list(mylist2)==[[2,2],[3,3],[2,4]]
        
    def test_append_list_if_sum_is_not_over_target(self):    
        assert append_list_if_sum_is_not_over_target([2,3], 5, 12)==[2,3,5]
        
    def test_get_list_of_unique_combinations(self):
        my_combinations=get_list_of_unique_combinations([3,2,2], 2)
        assert (([2,2] in my_combinations) & ([2,3] in my_combinations))
        
    def test_get_charlist_from_stinglist(self):
        stringlist=['bob', 'doug']
        assert get_charlist_from_stinglist(stringlist)==['b','o','b','d','o','u','g']
        

class testAnagramGenerator:
    def __init__(self):
        pass
    def test_anagram_generator_name(self, anagram_generator=anagramGenerator(name='Balazs Lukacs', dictionary=sample_dictionary)):
        assert type(anagram_generator.name)==str
        assert 'Balazs Lukacs'==anagramGenerator(name='Balazs Lukacs', dictionary=sample_dictionary).name
        with pytest.raises(ValueError):
            anagramGenerator(name=124, dictionary=sample_dictionary)
        with pytest.raises(ValueError):
            anagramGenerator(name='abcde', dictionary=sample_dictionary)
            
    def test_anagram_generator_dictionary(self, anagram_generator=anagramGenerator(name='Balazs Lukacs', dictionary=sample_dictionary)):
        assert type(anagram_generator.dictionary)==list
        assert ['cat', 'dog', 'horse']==anagramGenerator(name='Balazs Lukacs', dictionary=['cat', 'dog', 'horse']).dictionary
        
        test_dict= anagramGenerator(name='Balazs Lukacs', dictionary=['cat', 'dog', 'horse', 'a']).dictionary
        assert all([len(i)>1 for i in test_dict])
        
        with pytest.raises(ValueError):
            anagramGenerator(name='Balazs Lukacs', dictionary='sample_dictionary')
            
    def test_anagram_generator_other_attributes(self,anagram_generator= anagramGenerator(name='Balazs Lukacs', dictionary=['cat', 'dog', 'horse'])):
        assert type(anagram_generator.namelength_sum_components)==list
            
    def test_chars_to_list(self, anagram_generator=anagramGenerator(name='Balazs Lukacs', dictionary=sample_dictionary)):
        assert anagram_generator.chars_to_list('a')==['a']
        assert anagram_generator.chars_to_list('ab')==['a', 'b']
        assert anagram_generator.chars_to_list('a b')==['a', 'b']
        assert anagram_generator.chars_to_list('Joe')==['j', 'o', 'e']
        
    def test_name_split(self, anagram_generator=anagramGenerator(name='Balazs Lukacs', dictionary=sample_dictionary)):
        assert (anagramGenerator(name='Balazs', dictionary=['cat', 'dog', 'horse']).name_split==['b','a','l','a','z','s'])
        
    def test_get_letter_counts(self, anagram_generator=anagramGenerator(name='Balazs Lukacs', dictionary=sample_dictionary)):
        assert anagram_generator.get_letter_counts(['j','o','e'])=={'j':1,'o':1,'e':1}
        assert anagram_generator.get_letter_counts(['b','a','l','a','z','s'])=={'b':1,'a':2,'l':1,'z':1,'s':1}
        
    def test_filter_for_usable_words(self):
        anagram_generator_test=anagramGenerator(name='Balazs', dictionary=['sab', 'zab', 'horse'])
        anagram_generator_test.filter_for_usable_words()
        assert anagram_generator_test.dictionary==['sab', 'zab']
        
        anagram_generator_test2=anagramGenerator(name='Mariaa', dictionary=['mar', 'mariama'])
        anagram_generator_test2.filter_for_usable_words()
        assert anagram_generator_test2.dictionary==['mar']
        
        anagram_generator_test3=anagramGenerator(name='Mariaa', dictionary=['mar', 'maria'])
        anagram_generator_test3.filter_for_usable_words()
        assert anagram_generator_test3.dictionary==['mar']
        
        anagram_generator_test4=anagramGenerator(name='Mariaa', dictionary=['mar', 'mii'])
        anagram_generator_test4.filter_for_usable_words()
        assert anagram_generator_test4.dictionary==['mar']
        
        anagram_generator_test5=anagramGenerator(name='Mariaa', dictionary=['mar', 'ria', 'ia'])
        anagram_generator_test5.filter_for_usable_words()
        assert anagram_generator_test5.dictionary==['mar','ria']

        
        
    
    def test_generate_dictionary_wordlength_list(self):
        anagram_generator1=anagramGenerator(name='Balazs', dictionary=['sab', 'zab', 'horse'])
        anagram_generator1.generate_dictionary_wordlength_list()
        assert anagram_generator1.dictionary_wordlengths==[3,3,5]
        
        anagram_generator2=anagramGenerator(name='Balazs', dictionary=['sab', 'zab', 'dab', 'horse'])
        anagram_generator2.generate_dictionary_wordlength_list()
        assert anagram_generator2.dictionary_wordlengths==[3,3,5]
            
    def test_compile_sum_components(self,anagram_generator=anagramGenerator(name='Balazs', dictionary=['sab', 'zab', 'horse'])):        
        def statement(input_list, target_value, expected_output):
            generated_components=anagram_generator.compile_sum_components(input_list,target_value)
            return (all([g in expected_output for g in generated_components]) &
                all([t in generated_components for t in expected_output]))        
        assert statement([2,3],5,[[2,3]])
        assert statement([2,3,4],5,[[2,3]])
        assert statement([2,3,4,5],5,[[2,3],[5]])
        assert anagram_generator.compile_sum_components([2,2],6)==[]
        assert statement([2,2,2],6,[[2,2,2]])
        assert statement([2,3,2,3,2,4],6,[[2,2,2],[3,3],[2,4]])
        assert statement([4,3,3,2,2,2],6,[[2,2,2],[3,3],[2,4]])
        
    def test_create_distributed_word_collection(self,anagram_generator=anagramGenerator(name='Balazs', dictionary=['sab', 'zab', 'horse'])):
        assert type(anagram_generator.distributed_word_collection)==list
        anagram_generator.namelength_sum_components=[[3,5]]
        anagram_generator.create_distributed_word_collection()
        assert anagram_generator.distributed_word_collection==[[['sab','zab'],['horse']]]
    
    def test_generate_possible_anagram_combinations(self,anagram_generator=anagramGenerator(name='Balazs', dictionary=['sab', 'zab', 'horse'])):
        assert type(anagram_generator.anagram_combinations)==list
        anagram_generator.distributed_word_collection=[[['sab','zab'],['horse']]]
        anagram_generator.generate_possible_anagram_combinations()
        assert anagram_generator.anagram_combinations==[['sab', 'horse'],['zab','horse']]
        
    def test_filter_for_applicable_anagram_combinations(self,anagram_generator=anagramGenerator(name='Balazs', dictionary=['sab', 'zab', 'horse'])):
        anagram_generator.anagram_combinations=[['bazs','la'],['bbb','aaa']]
        anagram_generator.filter_for_applicable_anagram_combinations()
        assert anagram_generator.anagram_combinations==[['bazs','la']]
        
    def test_generate_final_anagram_list(self,anagram_generator=anagramGenerator(name='Balazs', dictionary=['sab', 'zab', 'horse'])):
        assert type(anagram_generator.anagram_list)==list
        anagram_generator.anagram_combinations=[['bazs','la'],['la','bazs']]
        anagram_generator.generate_final_anagram_list()
        assert anagram_generator.anagram_list==['Bazs La', 'La Bazs']
        
    # def test_get_anagram(self,anagram_generator=anagramGenerator(name='Balazs', dictionary=['sab', 'zab', 'horse'])):
    #     anagram_generator.anagram_list=['Bazs La', 'La Bazs']
    #     assert type(anagram_generator.get_anagram())==str
    #     assert anagram_generator.get_anagram() in ['Bazs La', 'La Bazs']



test_helper_functions=testHelperFunctions()
test_helper_functions.test_get_unique_values_from_list()
test_helper_functions.test_append_list_if_sum_is_not_over_target()
test_helper_functions.test_get_list_of_unique_combinations()
test_helper_functions.test_get_charlist_from_stinglist()

test_anagram_generator=testAnagramGenerator()
test_anagram_generator.test_anagram_generator_name()
test_anagram_generator.test_anagram_generator_dictionary()
test_anagram_generator.test_anagram_generator_other_attributes()
test_anagram_generator.test_chars_to_list()
test_anagram_generator.test_filter_for_usable_words()
test_anagram_generator.test_generate_dictionary_wordlength_list()
test_anagram_generator.test_compile_sum_components()
test_anagram_generator.test_create_distributed_word_collection()
test_anagram_generator.test_generate_possible_anagram_combinations()
test_anagram_generator.test_filter_for_applicable_anagram_combinations()
test_anagram_generator.test_generate_final_anagram_list()
# test_anagram_generator.test_get_anagram()
