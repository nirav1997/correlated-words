# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 13:31:47 2017

@author: asus
"""

from trainer import Trainer
from wikiscrapper import WikiScrapper
from sort import Sort

word = 'Internet'
inCSV = None
outCSV = 'correlated.csv'
print(word)

scrapper = WikiScrapper()
doc = scrapper.scrap(word, 4)

trainer = Trainer()

#doc = trainer.loadData('data.txt')
doc = trainer.clean(doc)
#print('scrapped')
#print(doc)


trainer.loadDF(inCSV)
trainer.updateAll(doc)
#trainer.printDF()
#print('updated')
trainer.saveDF(outCSV)
#print('saved')

#sort = Sort()
#print(sort.maxWay(outCSV, 'cooking', 10))
