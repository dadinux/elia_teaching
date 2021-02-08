#!/usr/bin/python3

import pandas

df = pandas.read_csv('SOE_Shutdown_180517.csv', index_col='Timestamp') 
print(df)