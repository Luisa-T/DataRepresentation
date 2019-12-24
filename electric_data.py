# The following file will attempt to answer challenge 07/01
import requests
import json
from xlwt import *

date="2019-11-08"
url = "https://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20and%20Imbalance%20Market%20Cost%20View&Date=>"+date
response = requests.get(url)
data = response.json()

totalPages = data["pagination"]["totalPages"]

pageNumber = 1
global listOfReports
listOfReports = []

while pageNumber <= totalPages:
    pageUrl =url + "&page" + str(pageNumber)
    data = requests.get(pageUrl).json()
    for item in data["items"]:
        listOfReports.append(item["ResourceName"])
    pageNumber +=1

# output the data
print(data)

for item in data["items"]:
    print(item["ResourceName"])
    listOfReport.append(item["ResourceName"])


        
# write to the excel file
w = workbook()
ws = w.add_sheet('Reports')
rowNumber = 0;
ws.write(rowNumber, 0, "StartTime")
ws.write(rowNumber, 1, "EndTime")
ws.write(rowNumber, 2, "ImbalanceVolume")
ws.write(rowNumber, 3, "ImbalancePrice")
ws.write(rowNumber, 4, "ImbalanceCost")
rowNumber += 1
for ReportName in listOfReports:
    print(ReportName)
    url="https://reports.sem-o.com/api/v1/documents/"+ReportName
    print(url)
    response= requests.get(url)
    sampleReport = response.json()
    for row in sampleReport["rows"]:
        ws.write(rowNumber, 0, row["StartTime"])
        ws.write(rowNumber, 1, row["EndTime"])
        ws.write(rowNumber, 2, row["ImbalanceVolume"])
        ws.write(rowNumber, 3, row["ImbalancePrice"])
        ws.write(rowNumber, 4, row["ImbalanceCost"])
        rowNumber += 1
w.save('balancing.xls')
# save that to a file
filename = 'allReports.json'

# writing the JSON code
f = open(filename, 'w')
json.dump(data, f, indent=4)