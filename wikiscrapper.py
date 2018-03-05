# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 03:27:12 2017

@author: asus
"""

import urllib3
from bs4 import BeautifulSoup


class WikiScrapper:
            
    #scrap data from wiki with no. of paras
    def scrap(self, word, size=0):
        
        #wiki base url
        wiki = "https://en.wikipedia.org/wiki/"
        
        #set url for particular word
        querry = wiki + word
    
        http = urllib3.PoolManager()
        page = http.request('GET', querry)
        
        pageContent = BeautifulSoup(page.data, "html.parser")
        
        #mine the data
        bodyContent = pageContent.find("div", id="bodyContent")
        
        doc = bodyContent.find_all('p', bodyContent)
                
        if size==0:
            return doc
    
        else:
            return doc[:size]



