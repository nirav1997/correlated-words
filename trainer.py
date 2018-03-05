# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 14:20:00 2017

@author: asus
"""
import re
import numpy as np
import pandas as pd

class Trainer:

    df = None 
    
    #cleaner
    def clean(self, paraList):
        doc = []
        
        for para in paraList:
            formatedPara = re.sub('<[^>]+>', '', str(para))
            formatedPara = re.sub(r'\([^()]*\)', '', formatedPara)
            formatedPara = re.sub(r'\[.*?\]', '', formatedPara)   
            if formatedPara:
                doc.append(formatedPara)
                
        return doc
    
    #load from text
    def loadData(self, fileName):
        file = open(fileName, 'r')
        data = file.read()
        doc = data.split('\n')
        return doc
    
    #load csv file ( if pre traiend present )
    def loadDF(self, inCSV = None):
        if inCSV == None:
            self.df=pd.DataFrame()
        else:  
            self.df = pd.read_csv(inCSV, index_col = 0)
    
    #update model
    def updateDF(self, words, val):
        
        #if only one word found no relations
        if len(words) == 1:
            return
        
        #removing already present values
        present = self.df.index.values
        old = words
        words = list(set(words) - set(present))
              
        
        size = len(words)
        
        if self.df.empty:
            self.df = pd.DataFrame(np.zeros((size,size)), index = words, columns = words)
            
        else:
            #create df of new rows and append
            noCols = self.df.shape[1]
            nameCols = self.df.columns.values
            tp = pd.DataFrame(np.zeros((size, noCols)), index = words, columns = nameCols)
            self.df = self.df.append(tp)
            
            #create df of new columns and append
            noRows = self.df.shape[0]
            nameRows = self.df.index.values
            tp = pd.DataFrame(np.zeros((noRows, size)), index=nameRows, columns = words)
            self.df = self.df.join(tp)
        
        #updating weights
        for i in range(0, len(old)): 
            for j in range(i+1, len(old)):
                    self.df[old[i]][old[j]] += val 
                    self.df[old[j]][old[i]] += val
    
    #remove stopwords like is,are,the..
    def bagOfWords(self, words):
        stopwords = open('stopwords.txt').read().split()    
        reqWords = list(set(words) - set(stopwords))    
        return(reqWords)
    
    #extract only unique words
    def uniqueWords(self, words):
        return np.unique(words)
    
    #update line connected words with weight 3    
    def updateLine(self, words):
        self.updateDF(words, 3)
    
    #update line connected words with weight 2
    def updatePara(self, words):
        self.updateDF(words, 2)
        
    #update line connected words with weight 1
    def updateDoc(self, words):
        self.updateDF(words, 1)
        
    #update All
    def updateAll(self, doc):
        docWords = []
        for para in doc:
            #print('...')
            paraWords = []
            lines = para.split('.')
            lines.pop()
            for line in lines:
                line = line.lower()
                
                #find all words in line, removing useless characters like: , - " ...
                lineWords = re.findall(r"(?:[a-z])+", line)
        
                #add unique words from line after removing stopwords and call update line for each line
                lineWords = self.bagOfWords(lineWords)
                lineWords = self.uniqueWords(lineWords)
                self.updateLine(lineWords)
                
                #add each line to para updater
                paraWords.extend(word for word in lineWords)
            
            #find unique and call update para for each para
            paraWords = self.uniqueWords(paraWords)
            self.updatePara(paraWords)
            
            #add each para to doc updater
            docWords.extend(paraWords)
        
        #find unique and call update para for whole doc
        docWords = self.uniqueWords(docWords)    
        self.updateDoc(docWords)
    
    #print model
    def printDF(self):
        print(self.df)
    
    #save to csv
    def saveDF(self, outCSV):
        self.df.to_csv(outCSV, index=True, header=True, sep=',')


