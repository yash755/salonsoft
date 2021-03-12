import requests
from bs4 import BeautifulSoup
import csv
import requests
from bs4 import BeautifulSoup
import time
import json
import os



file = open('url1.txt','r')

for f in file:
    page_url = f
    page_url = page_url.replace('\n','')

    page_url = 'https://salonlofts.com' + page_url

    print (page_url)

    try:

        response = requests.request("GET", page_url)
        html = BeautifulSoup(response.content, 'html.parser')

        atags = html.find_all('a',{'class':'view-my-profile-link'})

        for atag in atags:
            print (atag.get('href'))
            f1 = open('xyz.txt', 'a+')
            f1.write(atag.get('href'))
            f1.write('\n')
            f1.close()




    except:
        f1 = open('errors1.txt','a+')
        f1.write(f)
        f1.close()