# Import the beautifulsoup
# and request libraries of python.
import requests
import bs4
import pandas as pd
from collections import Counter as cnt
from time import sleep
import time

# Record the start time
start_time = time.time()


columns=['Searchterm','1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th']
df_links = pd.DataFrame(columns=columns)
df_titles = pd.DataFrame(columns=columns)

################

print('hi')
k=0
kw_df=pd.read_csv('searchterms2.csv')
keywords=kw_df.iloc[:,0]

###########
# Make two strings with default google search URL
# 'https://google.com/search?q=' and
# our customized search keyword.
# Concatenate them

for j in range(len(keywords)):
    
    print(j)
    text= keywords[j]
    df_links.loc[j,columns[0]]=keywords[j]
    df_titles.loc[j,columns[0]]=keywords[j]
    print(keywords[j])

    b=True
    while b :

        url = 'https://google.com/search?q=' + text

        # Fetch the URL data using requests.get(url),
        # store it in a variable, request_result.
        try:
            request_result=requests.get( url )

            # Pulling HTTP data from internet 
            soup = bs4.BeautifulSoup( request_result.text, "html.parser" )
            if soup.findAll(text='Why did this happen?'):
                sleep(300)
                print('Blocked')
                continue
            else:
                sleep(1)
                b=False
        except:
            sleep(15)
            




    
    links = soup.findAll("a")
    #print( links )
    serp_links=[]
    for i in range(len(links)):
        try: 
          if len(links[i].find('h3'))>0:
              serp_links.append(links[i])
              
        except:
            continue
    
    for i in range(min(len(serp_links),10)):
        
        a=serp_links[i]['href'].find('=')+1
        b=serp_links[i]['href'].find('&')
        df_links.loc[j,columns[i+1]]=serp_links[i]['href'][a:b]
        print(serp_links[i]['href'][a:b])
        df_titles.loc[j,columns[i+1]]=serp_links[i].find('h3').text
        print(serp_links[i].find('h3').text)
        print('------')
    # Record the end time
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    print(f"Process time: {elapsed_time} seconds")
        


i=0
while i< len(df_links):
    q=set(df_links.iloc[i,:])
    if len(q)==2:
        df_links=df_links.drop(df_links.index[i])
        df_titles=df_titles.drop(df_titles.index[i])
    i=i+1
        
df_links.to_csv('links.csv',index=False)
df_titles.to_csv('titles.csv',index=False)
