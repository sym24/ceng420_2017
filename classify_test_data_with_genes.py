# -*- coding: utf-8 -*-
"""
Created on Sat Aug 05 21:40:42 2017

@author: Yiming
@edited: Raymond, August 14, 2017
"""

from classifier_with_genes import classify
import pandas as pd
from hand import Hand
import os

Testpath = 'test.csv'
pwd = os.getcwd()
print(pwd)

print 'loading testing data'
df = pd.read_csv(Testpath)
hands = []
for index, row in df.iterrows():
#    print row['id']
    myhand = Hand(row)
    classify(myhand)
    hands.append([row['id'], myhand.assigned_class, '.'.join(str(i) for i in myhand.genes)])

print 'data classified and loaded'
dfw = pd.DataFrame(hands, columns = ['id','hand','genes'])

print 'write to csv'
dfw.to_csv('classified_with_genes.csv', sep = ',', index=False)
