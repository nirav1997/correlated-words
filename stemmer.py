# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 21:23:31 2017

@author: asus
"""

class Stemmer:
#check if consonant or not
    def isCons(self, word, pos):
        vowels = ['a', 'e','i', 'o', 'u']
        
        this = word[pos]
        prev = word[pos-1]
        
        #if in vowels return false
        if this in vowels:
            return False
        
        #special condition for y: if y check if prev is vowel if it is True, else false
        if this=='y':
            if pos==0:
                return True
            
            if prev in vowels:
                return True
            
            return False
        
        return True
    
    #check if vowel or not
    def isVow(self, word, pos):
        return not(self.isCons(word, pos))
    
    #return general structure of the word [C](VC)^m[V]
    def retForm(self, word):
        
        form = ""
        
        l = len(word)
        
        for i in range(l):
        
            if i==0:
                if self.isCons(word, i):
                    form += 'C'
                    
                else:
                    form += 'V'
                    
            else:
                #if this is vowel and previous is consonant append V
                if self.isCons(word, i) and self.isVow(word, i-1):
                    form += 'C'
                  
                #if this is consonant and previous is vowel append C 
                elif self.isVow(word, i) and self.isCons(word, i-1):
                    form += 'V'
    
                #else continue, i.e no change
                else: 
                    continue
                
        return form
    
    #finding value of m
    def mCount(self, form):
        return form.count('VC')
    
    #replacing suffix
    def replace(self, word, suffix, replace):
        if word.endswith(suffix):
            return word[:-len(suffix)] + replace
        return word
  
    def stem(self, word):
        #word = self.replace(word, 'ing' , '')
        form = self.retForm(word)
        m = self.mCount(form)
        print(form)
        print("m = " + str(m))
        print(word)

            
            
    
        
        
        