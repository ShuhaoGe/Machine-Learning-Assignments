#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 11:51:25 2018

@author: geshuhao
"""

import pandas as pd


database=pd.read_csv('ML.csv')

print(database)

database.describe(include='all')

database.dropna(thresh=0.5*len(database), axis=1)

print (database)