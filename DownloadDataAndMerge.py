# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 22:01:54 2021

@author: AC44917
"""

import pandas as pd
import glob
import requests, zipfile, io

#def downloaddata(month,dateInString):
   
#months = ["JAN" , "FEB" , "MAR" , "APR" , "JUN" , "JUL" , "AUG" , "SEP" , "OCT" , "NOV" , "DEC"]
months = ["JAN"]
dates = range(1,31)
    
for month in months:
    for date in dates:
        if date < 10:
             dateInString = str(0)+str(date)
        else:
            dateInString = str(date) 
        url = "https://www1.nseindia.com/content/historical/EQUITIES/2020/"+month+"/cm"+dateInString+month+"2020bhav.csv.zip"
        r = requests.get(url)
        temp=r.status_code
        if(temp!=404):
                z = zipfile.ZipFile(io.BytesIO(r.content))        
                z.extractall("/Equities")
        else:
                pass

path =r'\Equities' 
allExtractedFiles = glob.glob(path + "\*.csv")
#print(allExtractedFiles)
list = []
for file in allExtractedFiles:
    df = pd.read_csv(file,index_col=None, header=0 , engine = 'python')
    list.append(df)
frame = pd.concat(list, axis = 0, ignore_index = True)


frame.to_csv('MasterFileEquity1.csv', index= False)
symbol_company_data = pd.read_csv("NewScripts.csv")
stock_data = pd.read_csv('MasterFileEquity1.csv')
stock_data['STOCKNAME']= stock_data['SYMBOL'].map(symbol_company_data.drop_duplicates('NSE SYMBOL').set_index('NSE SYMBOL')['COMPANY NAME']).fillna("Not available")

file_name = 'MasterFileEquity_Jan_2020.csv'
stock_data.to_csv(file_name, encoding='utf-8')





