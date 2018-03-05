# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 20:21:15 2017

@author: asus
"""

import pandas as pd


class Sort:
    
    def sortWay(self, inCSV, word):
        df = pd.read_csv(inCSV, index_col = 0)
        
         #if no word found
        if word not in df.columns.values:
            return 'No Such Word Present'
        
        #make dataframe with only one row of required word
        df = df[word:word]        
        df = df.T.sort_values(word, ascending=False).T
        
        return df.columns.values
    
    def maxWay(self, inCSV, word, number = 5):
        
        correlated = ""
        
        df = pd.read_csv(inCSV, index_col = 0)
        
        #if no word found
        if word not in df.columns.values:
            return 'No Such Word Present'
        
        #make dataframe with only one row of required word
        df = df[word:word] 
        
        #find max and delete
        for i in range (number):
            temp = df.idxmax(axis=1)
            correlated += temp[0] + "\n"
            #print(temp[0])
            del(df[temp[0]])
            
        return correlated
            
            
        
#sort = Sort()
#print(sort.maxWay('new.csv', 'guitar', 7))






