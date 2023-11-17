# Import the beautifulsoup
# and request libraries of python.
import requests
import bs4
import pandas as pd
from collections import Counter as cnt
from time import sleep
import time

df_titles=pd.read_csv('titles.csv')
print( 'fetched!')
df_links=pd.read_csv('links.csv')
print( 'fetched!')
df_titles=df_titles.set_index('Searchterm')       

# Record the start time
columns=['Hi']+list(range(len(df_links)))
    
start=time.time()



df_similars=pd.read_csv('similars.csv')

print( 'fetched!')
print(df_similars.shape)


sorted_df=df_similars.sort_values(by = 'Sum', ascending = False)

print(sorted_df.shape)

sorted_df=sorted_df.drop(columns=['Sum'])
print(sorted_df.shape)


#temp_df=pd.DataFrame(columns=['searchterms']+columns)
df_searchterms=pd.DataFrame(index=range(len(sorted_df)),columns=['searchterms'])
temp_df=pd.concat([df_searchterms,sorted_df],axis=1)

temp_df['searchterms']=sorted_df['hi']

print('ok3')
sorted_df=temp_df
sorted_df= sorted_df.set_index("searchterms")

#for i in range(len(sorted_df)):

print(sorted_df.shape)
print(sorted_df)
sorted_df.to_csv('sorted.csv',index=False)
sorted_df.to_parquet('sorted.parquet')

#sorted_df = sorted_df.rename(columns={'0': 'Hi', '0.1': '0'})

