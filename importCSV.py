# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 12:14:10 2017

@author: Yiming
"""

import os
import pandas as pd 

Filepath = 'D:/OneDrive/Documents/2017 Summer/CENG 420/train.csv'
pwd = os.getcwd()
print(pwd)

df = pd.read_csv(Filepath)
hands = []
for index, row in df.iterrows():
    hands.append(Hand(row))
    train_data = row[:]
    print(train_data)