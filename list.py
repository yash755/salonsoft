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




        json_1 = html.find('script',{'type':'application/ld+json'})
        json_1 = str(json_1)
        json_1 = json_1.replace('<script type="application/ld+json">','')
        json_1 = json_1.replace('</script>','')


        json_2 = json.loads(json_1)


        graph_1 = json_2['@graph']

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

        if len(graph_1) >=2:

            telephone = graph_1[1]['telephone']
            streetAddress = graph_1[1]['address']['streetAddress']
            postOfficeBoxNumber = graph_1[1]['address']['postOfficeBoxNumber']
            addressLocality = graph_1[1]['address']['addressLocality']
            addressRegion = graph_1[1]['address']['addressRegion']
            postalCode = graph_1[1]['address']['postalCode']

            emp = graph_1[1]['employee']

            name = emp['additionalName']
            jobtitle = emp['jobTitle']
            email = emp['email']


        try:

            services = html.find('div',{'class':'loft-owner-profile-section services'})

            text = services.text.strip()

            text = os.linesep.join([s for s in text.splitlines() if s])
            text = text.replace('Featured Services','')
            featred_service = text

        except:
            print ("Error")

        try:

            about = html.find('div', {'class': 'loft-owner-profile-section about'})

            text = about.text.strip()

            text = os.linesep.join([s for s in text.splitlines() if s])
            text = text.replace('About', '')
            about_us = text

        except:
            print ("Error")


        try:

            products = html.find('div', {'class': 'loft-owner-profile-section products'})

            text = products.text.strip()

            text = os.linesep.join([s for s in text.splitlines() if s])
            text = text.replace('Products', '')
            product = text

        except:
            print ("Error")

        arr = []
        temp = []
        temp.append(page_url)
        temp.append('SALONS')
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

        with open('sydney3.csv', 'a+') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(arr)

    except:
        f1 = open('errors.txt','a+')
        f1.write(f)
        f1.close()
