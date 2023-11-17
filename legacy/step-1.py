

import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.parse
import time
import random

depth_level = int(input("Please enter depth level: "))


letters=["ا","ب","پ","ت","ث","ج","چ","ح","خ"\
        ,"د","ذ","ر","ز","ژ","س","ش","ص","ض",\
        "ط","ظ","ع","غ","ف","ق","ک","گ","ل","م","ن","و","ه","ی"]

keyword = str(input("Please enter your keyword: "))
# seed keyword: e.g. خريد عمده

searchterms=[]

print('hi')



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
    soup2 = BeautifulSoup(page2,'lxml')
    for suggestions in soup2.find_all('suggestion'):
        finder = int(str(suggestions).find(">"))
        suggestionclean = str(suggestions)[18:finder-1]
       # cleanlistsuggestions.append(suggestionclean)
        searchterms.append(suggestionclean)
    #searchterms.append(cleanlistsuggestions)
##########################################################
if depth_level==2:
    for letter1 in letters:
        for letter2 in letters:
            query1=(str(keyword)+" "+str(letter1)+str(letter2))
            query2=(str(letter1)+str(letter2)+" "+str(keyword))
            print(query1)
            print(query2)

            a=True
            while a:
                try:
                    page1 = urlopen('https://google.com/complete/search?output=toolbar&hl=es&q='+urllib.parse.quote(query1)).read()
                    a=False
                except:
                    print('Error1')
                    time.sleep(5)
                    continue
            
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
            soup2 = BeautifulSoup(page2,'lxml')
            for suggestions in soup2.find_all('suggestion'):
                finder = int(str(suggestions).find(">"))
                suggestionclean = str(suggestions)[18:finder-1]
               # cleanlistsuggestions.append(suggestionclean)
                searchterms.append(suggestionclean)
            #searchterms.append(cleanlistsuggestions)
searchterms=list(set(searchterms))            
######################################################
df_results=pd.DataFrame(searchterms)
df_results.to_csv("searchterms.csv", index=False)




        

        


        
