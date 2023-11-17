# Import the beautifulsoup
# and request libraries of python.
import requests
import bs4
import pandas as pd
from collections import Counter as cnt
from time import sleep
import time

columns=['Searchterm','1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th']

df_titles=pd.read_csv('titles.csv')
df_links=pd.read_csv('links.csv')

df_titles=df_titles.set_index('Searchterm')       
####################
columns=['hi']+list(df_links.iloc[:,0])

df_similars= pd.DataFrame(columns=columns)
print(df_similars.shape)
df_similars.loc[:,'hi']=df_links.iloc[:,0]

print(df_similars.shape)

# Record the start time
start_time = time.time()
links_list=[]
for i in range(len(df_links)):
    print(i)
    links_list.append(list(df_links.iloc[i, 2:12]))
    
start=time.time()
for i in range(len(df_links)):
    list_similarity=[]
    print(i)
    
    kw1=links_list[i]
    for j in range(len(df_links)):

        kw2=links_list[j]

        kw_total=kw1+kw2
        kw_set=set(kw_total)
        l_total=len(kw_total)
        l_set=len(kw_set)
        similarity=-2*(l_set-l_total)/l_total
        if similarity>0.75:
            list_similarity.append(1)
        

        else:

            kw22=kw2[:2]

            kw_total=kw1+kw22
            kw_set=set(kw_total)
            l_total=len(kw_total)
            l_set=len(kw_set)
            similarity=-2*(l_set-l_total)/l_total
            if similarity==1:
                list_similarity.append(1)
                
                
                
            else:
                kw23=kw2[:4]
                
                kw_total=kw1+kw23
                kw_set=set(kw_total)
                l_total=len(kw_total)
                l_set=len(kw_set)
                similarity=-2*(l_set-l_total)/l_total

            
                if similarity>0.74:
                    if df_links.iloc[i,1]==df_links.iloc[j,1]:
                         list_similarity.append(1)
                    elif similarity>0.49:
                    
                        kw24=kw2[:5]
                        
                        kw_total=kw1+kw24
                        kw_set=set(kw_total)
                        l_total=len(kw_total)
                        l_set=len(kw_set)
                        similarity=-2*(l_set-l_total)/l_total
                        if similarity>0.59:
                            if df_links.iloc[i,1]==df_links.iloc[j,1]:
                                if df_links.iloc[i,2]==df_links.iloc[j,2]:
                                    list_similarity.append(1)
                                else:    
                                    list_similarity.append(0)
                            else:
                                list_similarity.append(0)
                        else:
                            list_similarity.append(0)
                    else:
                        list_similarity.append(0)
                else:
                    list_similarity.append(0)
    end=time.time()
    totaltime=end-start
    print(totaltime)
    df_similars[columns[i+1]]=list_similarity


print(df_similars.shape)

#for i in range(len(df_similars)):
#    df_similars.loc[i,'Sum']=df_similars.iloc[i,1:].sum()            
#print(df_similars.shape)
df_similars['Sum'] = df_similars.iloc[:, 1:].sum(axis=1)


df_similars.to_parquet('similars.parquet',index=False)
df_similars.to_csv('similars.csv',index=False)

     

