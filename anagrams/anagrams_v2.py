# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 22:29:07 2022

@author: Balazs
"""
import numpy as np
import itertools
from itertools import combinations
import random


# helper functions
def get_unique_elements_from_list(mylist):
    list_unique=[]
    for i in mylist:
        if i not in list_unique:
            list_unique.append(i)
    return list_unique

def append_list_if_sum_is_not_over_target(input_list, new_element, target_value):
    if sum(input_list)+new_element<=target_value:
        input_list.append(new_element)
    return input_list


def get_list_of_unique_combinations(value_list, n_of_elements_picked):
    comb = list(combinations(value_list, n_of_elements_picked))
    comb=[list(c) for c in comb]
    comb_out=[]
    for i in comb:
        combination=i
        combination.sort()
        comb_out.append(combination)
    return get_unique_elements_from_list(comb_out)

def get_charlist_from_stinglist(stringlist):
    charlist=[]
    for i in stringlist:
        for k in i:
            charlist.append(k)
    return charlist


file_path = 'E:\\Software Engineering\\Playing with TDD\\anagrams\\2of12inf.txt'
file = open(file_path,'r')
lines = file.readlines()
file.close()

dictionary=[word.replace('\n','').replace('%','') for word in lines]


class anagramGenerator:
    def __init__(self, name, dictionary):
        self.__set_name(name)
        self.__set_dictionary(dictionary)
        self.name_split=self.chars_to_list(self.name)        
        self.name_letter_pool=self.get_letter_counts(self.name_split)
        self.namelength_sum_components=[]
        self.distributed_word_collection=[]
        self.anagram_combinations=[]
        self.anagram_list=[]
        
    def chars_to_list(self, string):
        return [i for i in string.replace(' ','').lower()]
    
    def get_letter_counts(self, letter_list):
        letter_count = {}
        for i in letter_list:
            try: 
                letter_count[i]=letter_count[i]+1
            except:
                letter_count[i]=1
        return letter_count
    
    def filter_for_usable_words(self):
        word_selection=[]
        for word in self.dictionary:
            is_all_letters_of_word_in_name = all([(letter in self.name_split) for letter in word])
            if is_all_letters_of_word_in_name:
                word_selection.append(word)
        word_selection=[word for word in word_selection if (((len(word)<=len(self.name_split)) &
                                                            (len(word)!=(len(self.name_split)-1))) &
                                                            (len(word)>=3))]
        word_selection_charcount_based=[]
        for word in word_selection:
            word_char_pool=self.get_letter_counts(self.chars_to_list(word))
            num_of_chars_is_less_or_equal_to_name=(
                all([word_char_pool[c]<=self.name_letter_pool[c] for c in word_char_pool])
                )
            if num_of_chars_is_less_or_equal_to_name:
                word_selection_charcount_based.append(word)            
        self.dictionary=word_selection_charcount_based
        
        
    def generate_dictionary_wordlength_list(self):
        wordlengths_raw=[len(word) for word in self.dictionary]
        unique_wordlengths=np.unique(wordlengths_raw).tolist()
        name_wordlength=len(self.name_split)
        wordlengths_collected=[]
        for i in unique_wordlengths:
            n_of_instances=wordlengths_raw.count(i)
            max_number_in_an_anagram=name_wordlength//i
            for k in range(min([n_of_instances,max_number_in_an_anagram])):
                wordlengths_collected.append(i)                        
        self.dictionary_wordlengths=wordlengths_collected
        
    
    def compile_sum_components(self, value_list, sum_target):
        list_of_all_combinations=[]
        n_of_max_elements_in_combination=sum_target//2
        for k in range(1,n_of_max_elements_in_combination+1):
            unique_combinations_temp=get_list_of_unique_combinations(value_list,k)
            list_of_all_combinations=list_of_all_combinations+unique_combinations_temp                                      
        list_of_combinations=[c for c in list_of_all_combinations if sum(c)==sum_target]
        list_of_combinations=get_unique_elements_from_list(list_of_combinations)
        return list_of_combinations
    
    def get_namelength_sum_components(self):
        self.namelength_sum_components=self.compile_sum_components(self.dictionary_wordlengths, len(self.name_split))
        
    def create_distributed_word_collection(self):
        distributed_word_collection=[]
        for i in self.namelength_sum_components:
            combination_word_collection=[]
            for k in i:
                selected_words=[word for word in self.dictionary if len(word)==k]
                combination_word_collection.append(selected_words)
            distributed_word_collection.append(combination_word_collection)
        self.distributed_word_collection=distributed_word_collection        
        
    def generate_possible_anagram_combinations(self):
        anagram_combinations=[]
        for i in self.distributed_word_collection:
            combinations_raw = list(itertools.product(*i))
            combinations_list = [list(element) for element in combinations_raw]
            anagram_combinations=anagram_combinations+combinations_list
        self.anagram_combinations=anagram_combinations
        
    
    def filter_for_applicable_anagram_combinations(self):
        anagram_combinations_filtered=[]
        for i in self.anagram_combinations:
            charlist=get_charlist_from_stinglist(i)
            charpool=self.get_letter_counts(charlist)
            all_characters_in_name=(
                all([charpool[char]==self.name_letter_pool[char] for char in charpool])
                )
            if all_characters_in_name:
                anagram_combinations_filtered.append(i)
        self.anagram_combinations=anagram_combinations_filtered
    
    def generate_final_anagram_list(self):
        anagram_list=[]
        for i in self.anagram_combinations:
            anagram_string=''
            for k in i:
                anagram_string=anagram_string+k[0].upper()+k[1:]+' '
            anagram_string=anagram_string.rstrip()
            anagram_list.append(anagram_string)
        self.anagram_list=anagram_list
        
    def get_anagram(self):
        print(random.choice(self.anagram_list))
    
    def create_anagrams(self):
        self.filter_for_usable_words()
        self.generate_dictionary_wordlength_list()
        self.get_namelength_sum_components()
        self.create_distributed_word_collection()
        self.generate_possible_anagram_combinations()
        self.filter_for_applicable_anagram_combinations()
        self.generate_final_anagram_list()    
        
    def __set_name(self, name):
        if (type(name)!=str):
            raise ValueError('Name must a string!')
        elif len(name)<6:
            raise ValueError('Name must at least 5 characters long!')
        else:
            self.name=name
            
    def __set_dictionary(self, dictionary):
        if (type(dictionary)!=list):
            raise ValueError('The dictionary must be a list of words')
        else:
            self.dictionary=[word.lower() for word in dictionary if len(word)>1]
                

      
sample_dictionary=['cat', 'dog', 'horse', 'a']


anagram_generator=anagramGenerator('Lord Voldemort', dictionary = dictionary)
anagram_generator.create_anagrams()
anagram_generator.get_anagram()
anagram_generator.anagram_list

#anagram_generator.filter_for_usable_words()
# anagram_generator.generate_dictionary_wordlength_list()
# anagram_generator.get_namelength_sum_components()
# anagram_generator.create_distributed_word_collection()
# anagram_generator.generate_possible_anagram_combinations()
# anagram_generator.filter_for_applicable_anagram_combinations()
# anagram_generator.generate_final_anagram_list()
# anagram_generator.anagram_list
