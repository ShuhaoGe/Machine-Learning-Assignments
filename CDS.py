#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 23:04:44 2018

@author: geshuhao
"""

import pandas as pd
CDS=pd.read_stata('cds_spread5y_2001_2016.dta')
CDS
CRSP=pd.read_stata('crsp_quarterly.dta')
CRSP
newdata=pd.merge(CDS,CRSP,left_on=['gvkey','mdate'],right_on=['gvkey','datadate'],how='left')

n=len(newdata)/3
for i in range(n):
    newdata.iloc[3*i,4:14]=newdata.iloc[3*i+2,4:14]
    newdata.iloc[3*i+1,4:14]=newdata.iloc[3*i+2,4:14]

