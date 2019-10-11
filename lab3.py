import requests
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print (page)
print("---------------")
print (page.content)
import requests
from bs4 import BeautifulSoup
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print (page)
print("-------------------")
print (page.content)
soup1 = BeautifulSoup(page.content, 'html.parser')
print("-------------------")
print (soup1.prettify())
from bs4 import BeautifulSoup
with open("../week02/carviewer2.html") as fp:
 soup = BeautifulSoup(fp,'html.parser')
print (soup.prettify())

from bs4 import BeautifulSoup
with open("../week02/carviewer2.html") as fp:
 soup = BeautifulSoup(fp,'html.parser')
print (soup.tr)
#print (soup.tr)
rows = soup.findAll("tr")
for row in rows:
 print("------")
 print(row)
for row in rows:
 #print(row)
 cols = row.findAll("td")
 for col in cols:
 print(col.text)
dataList = []
 for col in cols:
 dataList.append(col.text)
 print (dataList)

import csv
employee_file = open('employee_file.csv', mode='w')
employee_writer = csv.writer(employee_file, delimiter=',', quotech
ar='"', quoting=csv.QUOTE_MINIMAL)
employee_writer.writerow(['John Smith', 'Accounting', 'November'])
employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
employee_file.close()

from bs4 import BeautifulSoup
import csv
with open("../week02/carviewer2.html") as fp:
 soup = BeautifulSoup(fp,'html.parser')
#print (soup.tr)
employee_file = open('week02data.csv', mode='w')
employee_writer = csv.writer(employee_file, delimiter=',', quotech
ar='"', quoting=csv.QUOTE_MINIMAL)
rows = soup.findAll("tr")
for row in rows:

 cols = row.findAll("td")
 dataList = []
 for col in cols:
 dataList.append(col.text)
 employee_writer.writerow(dataList)
employee_file.close()

<import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.myhome.ie/residential/
mayo/property-for-sale?page=1")
soup = BeautifulSoup(page.content, 'html.parser')
print (soup.prettify())
listings = soup.find("div", class_="PropertyListingCard" )
print (listings)
price = listings.find(class_="PropertyListingCard__Price").text
print (price)
price = listings.find(class_="PropertyListingCard__Price").text
print (price)
listings = soup.findAll("div", class_="PropertyListingCard" )
for listing in listings:
 entry = []

 price = listing.find(class_="PropertyListingCard__Price").text
 entry.append(price)
 address = listing.find(class_="PropertyListingCard__Address").text
 entry.append(address)
 print(entry)

import requests
import csv
from bs4 import BeautifulSoup
page = requests.get("https://www.myhome.ie/residential/mayo/property-forsale?page=1")
soup = BeautifulSoup(page.content, 'html.parser')
home_file = open('week03MyHome.csv', mode='w')
home_writer = csv.writer(home_file, delimiter='\t', quotechar='"', quoting=csv
.QUOTE_MINIMAL)
listings = soup.findAll("div", class_="PropertyListingCard" )
for listing in listings:
 entryList = []

 price = listing.find(class_="PropertyListingCard__Price").text
 entryList.append(price)
 address = listing.find(class_="PropertyListingCard__Address").text
 entryList.append(address)
 home_writer.writerow(entryList)
home_file.close()