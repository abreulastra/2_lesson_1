# -*- coding: utf-8 -*-
"""
Created on Thu May 19 11:58:14 2016

@author: AbreuLastra_Work
"""

import pandas as pd
from scipy import stats

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data = data.splitlines()
data = [i.split(',') for i in data]


column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

drugs = ['Alcohol','Tobacco']

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)


for drug in drugs:  
    m_drug = 0    
    print("The mean value for %s is %f" % (drug, df[drug].mean()))
    print("The median value for %s is %f" % (drug, df[drug].median()))
    m_drug = stats.mode(df[drug])[0] 
    print("The mode value for %s is %s" % (drug, m_drug))    
    print("The range for %s is %f" % (drug,(max(df[drug]) - min(df[drug]))))
    print("The std. deviation for %s is %f" % (drug, df['Alcohol'].std()))
    print("The variance for %s is %f" % (drug, df['Alcohol'].var()))
    print('\n')
