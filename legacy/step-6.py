# Import the beautifulsoup
# and request libraries of python.
import requests
import bs4
import pandas as pd
from collections import Counter as cnt
from time import sleep
import time


############


############



df_titles=pd.read_csv('titles.csv')
print( 'fetched!')
df_links=pd.read_csv('links.csv')
print( 'fetched!')
df_titles=df_titles.set_index('Searchterm')       

# Record the start time
columns=['hi']+list(range(len(df_links)))
    
start=time.time()



#sorted_df=pd.read_csv('sorted.csv')
sorted_df = pd.read_parquet('sorted.parquet')
print( 'fetched2!')



############
print(sorted_df.shape)


############




#sorted_df = sorted_df.rename(columns={'0': 'Hi', '0.1': '0'})
df_articles=pd.DataFrame(columns=['Articles'])
sorted_df= sorted_df.set_index("hi")
##################
i=0
while len(sorted_df):
    row_drops=[]
    column_drops=[]
    str_titles=''
    n=0
    #df_articles.loc[len(df_articles),'Articles']=sorted_df.iloc[i,0]

    for j in range(i,len(sorted_df.columns)):
        if sorted_df.iloc[i,j]==1:  
            df_articles.loc[len(df_articles),'Articles']=sorted_df.columns[j]

            n+=1
            list_titles=df_titles.loc[sorted_df.columns[j],:]
            for u in range(5):
                str_titles=str_titles+' '+str(list_titles[u])


            
            column_drops.append(sorted_df.columns[j])
    print(column_drops)


    sorted_df=sorted_df.drop(columns=column_drops)
    sorted_df=sorted_df.drop(column_drops)

        
    #sorted_df=sorted_df.drop(sorted_df.index[i])
    #sorted_df=sorted_df.drop(columns=sorted_df.columns[1])
    print(sorted_df.shape)
    df_articles.loc[len(df_articles),'Articles']='            '
    df_articles.loc[len(df_articles),'Articles']='عنوان شامل اين کلمات:'
    split_it = str_titles.split()
    Counter = cnt(split_it)
    
    title_words={k for (k,v) in Counter.items() if v > 3*n}
    print(title_words)
    df_articles.loc[len(df_articles),'Articles']=title_words
    
    df_articles.loc[len(df_articles),'Articles']='--------'
    df_articles.loc[len(df_articles),'Articles']='--------'
    
df_articles.to_csv('articles.csv',index=False)        

