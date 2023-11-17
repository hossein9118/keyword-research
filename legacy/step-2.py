

import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.parse
import time
import random
import random




letters=["ا","ب","پ","ت","ث","ج","چ","ح","خ"\
        ,"د","ذ","ر","ز","ژ","س","ش","ص","ض",\
        "ط","ظ","ع","غ","ف","ق","ک","گ","ل","م","ن","و","ه","ی"]

#keyword = str(input("Please enter your keyword: "))

searchterms=[]

print('hi')
k=0
a=True

while a:
    try:
        kw_df=pd.read_csv('searchterms.csv')
        a=False
    except:
        time.sleep(300)
    
keywords=kw_df.iloc[:,0]

for keyword in keywords:
    print(keyword)
    k=k+1
    print(k)
    for letter in letters:
        query1=(str(keyword)+" "+str(letter))
        query2=(str(letter)+" "+str(keyword))
        a=True
        while a:
            try:
                page1 = urlopen('https://google.com/complete/search?output=toolbar&hl=es&q='+urllib.parse.quote(query1)).read()
                a=False
                
            except:
                print('Error1')
                time.sleep(5)
                continue


            
        #time.sleep(3)
        print(query1)
        soup1 = BeautifulSoup(page1,'lxml')
        #cleanlistsuggestions = []
        for suggestions in soup1.find_all('suggestion'):
            finder = int(str(suggestions).find(">"))
            suggestionclean = str(suggestions)[18:finder-1]
           # cleanlistsuggestions.append(suggestionclean)
            searchterms.append(suggestionclean)

        b=True
        while b:
            try:    
                page2 = urlopen('https://google.com/complete/search?output=toolbar&hl=es&q='+urllib.parse.quote(query2)).read()
                b=False
                
            except:
                print('Error2')
                time.sleep(5)
                continue
        #time.sleep(3)
        print(query2)
        soup2 = BeautifulSoup(page2,'lxml')
        for suggestions in soup2.find_all('suggestion'):
            finder = int(str(suggestions).find(">"))
            suggestionclean = str(suggestions)[18:finder-1]
           # cleanlistsuggestions.append(suggestionclean)
            searchterms.append(suggestionclean)
        #searchterms.append(cleanlistsuggestions)
    time.sleep(random.randint(0,1))
    if k%3==0:
        searchterms=list(set(searchterms)) 
        df_results_temp=pd.DataFrame(searchterms)
        df_results_temp.to_csv("searchterms2.csv",index=False)
        with open("num.txt", "w") as file:
           file.write(str(k))

searchterms=list(set(searchterms))           
######################################################
df_results=pd.DataFrame(searchterms)
df_results.to_csv("searchterms2.csv",index=False)




        

        


        
