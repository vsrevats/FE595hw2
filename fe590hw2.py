##Vasu Srevatsan
##HW2 FE 595
## October 5,2020
##I pledge that I have abided by Stevens Honor System.


import requests
from bs4 import BeautifulSoup
import csv
import os
import sys
import pandas as pd


def scraper2(website, numscrapes,df):
    goodscrap = 0
    badscrap = 0
    ##scrape until you get 50 scrapes
    while goodscrap < numscrapes:
        try:
            ##parse website
            req = requests.get(website)
            reqtext = req.text
            soup = BeautifulSoup(reqtext, 'html.parser')
            attributes = soup.find_all('li')
            print(attributes)
            ##find Name and Purpose
            for attr in attributes:
                if "Name:" in attr.text:
                    name = attr.text.split("Name: ")[1]
                    print(name)
                elif "Purpose:" in attr.text:
                    purpose = attr.text.split("Purpose: ")[1]
                    print(purpose)
            ##add to df if Name and Purpose are there
            if name is not None and purpose is not None:
                goodscrap +=1
                df = df.append({'Name' : name, 'Purpose' : purpose},ignore_index = True)
        ##throw error if it doesn't work
        except:
            print("Error has occurred.")
            badscrap +=1
    ##export to csv
    df.to_csv('C:/Users/vasu530/Desktop/fe595export.csv',index=False, header=True)
    print(df)


if __name__ == '__main__':
    finaldf = pd.DataFrame(columns=['Name', 'Purpose'])

    website = 'http://3.95.249.159:8000/random_company'

    scraper2(website,50,finaldf)
