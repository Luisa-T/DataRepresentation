from bs4 import BeautifulSoup

with open("carsLuisaTLab2.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')

print (soup.prettify())