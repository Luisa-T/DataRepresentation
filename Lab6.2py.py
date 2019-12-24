import json 
import requests 

#html = '<h1>hello world</h1>This is html' 
f = open("CarsLuisaTLab2.html", "r") 
html = f.read() 
#print (html) 
 
apiKey = '46ceed910c24ff7cce8240e89ec7b71912f6f40f2ec55fd217ce150a d6d4f1c4' 
url = 'https://api.html2pdf.app/v1/generate' 
 
data = {'html': html,'apiKey': apiKey} 
response = requests.post(url, json=data) 
print (response.status_code)

newFile = open("lab06.02.01.htmlaspdf.pdf", "wb") 
newFile.write(response.content)
 
response = requests.get(url, auth=('token',apiKey)) 
 
repoJSON = response.json() 
#print (response.json())
file = open('lab06.02.01.htmlaspdf.pdf', 'w') 
json.dump(repoJSON, file, indent=4)