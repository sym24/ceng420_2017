# -*- coding: utf-8 -*-
"""
Created on Sat Aug 05 21:40:42 2017

@author: Yiming
"""

from classifier import classify_one
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
    classify_one(myhand)
    hands.append([row['id'], myhand.assigned_class])

print 'data classified and loaded'
dfw = pd.DataFrame(hands, columns = ['id','hand'])

print 'write to csv'
dfw.to_csv('classifyTest.csv', sep = ',', index=False)