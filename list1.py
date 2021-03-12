import requests
from bs4 import BeautifulSoup
import csv
import requests
from bs4 import BeautifulSoup
import time
import json
import os



file = open('xyz.txt','r')

for f in file:
    page_url = f
    page_url = page_url.replace('\n','')

    page_url = 'https://salonlofts.com' + page_url

    print (page_url)

    try:

        response = requests.request("GET", page_url)
        html = BeautifulSoup(response.content, 'html.parser')


        name = ''
        jobtitle = ''

        streetAddress = ''
        postOfficeBoxNumber = ''
        addressLocality = ''
        addressRegion = ''
        postalCode = ''
        email = ''
        telephone = ''
        about_us = ''
        featred_service = ''
        product = ''




        try:

            name = html.find('h1',{'class':'loft-owner-name'})
            name = name.text.strip()
        except:
            print ("Name Error")


        try:

            jobtitle = html.find('h2',{'class':'loft-owner-title'})
            jobtitle = jobtitle.text.strip()
        except:
            print ("Title Error")


        try:

            streetAddress = html.find('div',{'class':'loft-owner-loft-number'})
            streetAddress = streetAddress.text.strip()
        except:
            print ("Streert Error")


        try:

            email = html.find('a',{'class':'email-address'})
            email = email.text.strip()
        except:
            print ("Email Error")


        try:

            telephone = html.find('div',{'class':'phone-number'})
            telephone = telephone.text.strip()
        except:
            print ("Phone Error")



        try:

            services = html.find('div',{'class':'loft-owner-profile-section services'})

            text = services.text.strip()

            text = os.linesep.join([s for s in text.splitlines() if s])
            text = text.replace('Featured Services','')
            featred_service = text

            featred_service = featred_service.strip()

            featred_service = featred_service.split('\n')

            str1 = ''

            for d in featred_service:
                if '$' in d:
                    str1 = str1 + d + ';'
                else:
                    str1 = str1 + d

            featred_service = str1

        except:
            print (" s Error")

        try:

            about = html.find('div', {'class': 'loft-owner-profile-section about'})

            text = about.text.strip()

            text = os.linesep.join([s for s in text.splitlines() if s])
            text = text.replace('About', '')
            about_us = text.strip()

            about_us = about_us.replace('¬†', '')

            # print (about_us)

        except:
            print ("p Error")


        try:

            products = html.find('div', {'class': 'loft-owner-profile-section products'})

            text = products.text.strip()

            text = os.linesep.join([s for s in text.splitlines() if s])
            text = text.replace('Products', '')
            product = text.strip()

            product = product.replace('\n',';')

            # print (product)

        except:
            print ("ps Error")

        arr = []
        temp = []
        temp.append(page_url)
        temp.append('BEAUTY SPECIALISTS')
        temp.append(name)

        temp.append(jobtitle)
        temp.append(email)
        temp.append(telephone)
        temp.append(streetAddress)
        temp.append(postOfficeBoxNumber)
        temp.append(addressLocality)
        temp.append(addressRegion)
        temp.append(postalCode)

        temp.append(about_us)
        temp.append(featred_service)
        temp.append(product)



        arr.append(temp)

        with open('sydney22.csv', 'a+') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(arr)

    except:
        f1 = open('errors1.txt','a+')
        f1.write(f)
        f1.close()
