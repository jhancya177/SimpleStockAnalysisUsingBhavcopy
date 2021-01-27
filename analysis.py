# -*- coding: utf-8 -*-
"""
Created on Sat May 30 16:40:12 2020

@author: AC44917
"""
import pandas as pd


stock_data = pd.read_csv("MasterFileEquity_2020.csv")
columns = stock_data.columns
equity_stock_data = stock_data[stock_data['SERIES'] == 'EQ']
equity_stock_data ['DATE'] = pd.to_datetime(equity_stock_data.TIMESTAMP, dayfirst=True)

filtered_equity_stock_data = equity_stock_data[equity_stock_data['CLOSE'] < 50]
filtered_equity_stock_data = filtered_equity_stock_data[filtered_equity_stock_data['DATE'] <  '2020-05-01']

difference = []
for data, df_symbols in filtered_equity_stock_data.groupby('SYMBOL'):   
    df_symbols.sort_values(by="DATE" , inplace=True)
    start=  df_symbols['CLOSE'].iloc[0] # first element 
    end =  df_symbols['CLOSE'].iloc[-1]      
    difference =  start-end
    percentage_difference = (difference / start )* 100
    if percentage_difference > 60:
        print(df_symbols['SYMBOL'].iloc[0])
    
    
#pd.concat(df_symbols['SYMBOL'] , difference)
