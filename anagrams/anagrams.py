# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 16:43:09 2021

@author: Balazs
"""

file_path = 'E:\\Software Engineering\\Playing with TDD\\anagrams\\2of12inf.txt'
file = open(file_path,'r')
lines = file.readlines()
file.close()

dictionary=[word.replace('\n','').replace('%','') for word in lines]


len(dictionary)

81000**3

class anagramGenerator:
    def __init__(self, name, dictionary):
        self.__set_name(name)
        self.__set_dictionary(dictionary)
        self.name_split=self.chars_to_list(self.name)        
        self.name_letter_pool=self.get_letter_counts(self.name_split)
        self.name_letter_pool_value=self.calculate_pool_value(self.name_letter_pool)
        
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
    
    def is_chr_pool_in_chr_pool(self, word, reference):
        if all([letter in reference for letter in word])==False:
            return False
        else:
            return all([word[letter]<=reference[letter] for letter in word])
        
    def substract_chr_pool_from_chr_pool(self, word, reference):
        for letter in word:
            reference[letter]=reference[letter]-word[letter]
        return reference
    
    def calculate_pool_value(self, pool):
        value=0
        for i in pool:
            value=value+pool[i]
        return value
    
    def select_word_from_dictionary(self):
        for i in self.dictionary:
            word_charlist=self.get_letter_counts(self.chars_to_list(i))
            if self.is_chr_pool_in_chr_pool(word_charlist, self.name_letter_pool)==True:
                self.last_select=i
                self.dictionary.remove(i)
                self.name_letter_pool=self.substract_chr_pool_from_chr_pool(word_charlist, self.name_letter_pool)
                self.name_letter_pool_value=self.calculate_pool_value(self.name_letter_pool)
                break
            self.last_select=None
    
    def collect_anagram_words(self):
        self.last_select=''
        self.anagram_wordlist=[]
        while (len(self.dictionary)>=0) & (self.last_select!=None) & (self.name_letter_pool_value>=2):
            self.select_word_from_dictionary()
            if self.last_select!=None:
                self.anagram_wordlist.append(self.last_select)
    
            
    def __set_name(self, name):
        if (type(name)!=str):
            raise ValueError('Name must a string!')
        elif len(name)<5:
            raise ValueError('Name must at least 5 characters long!')
        else:
            self.name=name
            
    def __set_dictionary(self, dictionary):
        if (type(dictionary)!=list):
            raise ValueError('The dictionary must be a list of words')
        else:
            self.dictionary=[word for word in dictionary if len(word)>1]
            
    
    
        
sample_dictionary=['cat', 'dog', 'horse', 'a']
anagram_generator=anagramGenerator('Balazs Lukacs', dictionary = dictionary)

anagram_generator.collect_anagram_words()
anagram_generator.anagram_wordlist
anagram_generator.name_letter_pool
