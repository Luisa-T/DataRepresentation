# code for challenge 07/03
import requests
import json
from xlwt import *

#monthly weather for Athenry
url = "https://prodapi.metweb.ie/monthly-data/Athenry"
response = requests.get(url)
data = response.json()

totalWeather = list(data)

pageNumber = 1

for item in data:
    print(item)
    totalWeather.append(item)


        
# write to the excel file
w = workbook()
ws = w.add_sheet('Weather')
rowNumber = 0;
ws.write(rowNumber, 0, "name")
ws.write(rowNumber, 1, "temperature")
ws.write(rowNumber, 2, "symbol")
ws.write(rowNumber, 3, "weatherDescription")
ws.write(rowNumber, 4, "text")
ws.write(rowNumber, 5, "windSpeed")
ws.write(rowNumber, 6, "windGust")
ws.write(rowNumber, 7, "cardinalWindDirection")
ws.write(rowNumber, 8, "windDirection")
ws.write(rowNumber, 9, "humidity")
ws.write(rowNumber, 10, "rainfall")
ws.write(rowNumber, 11, "pressure")
ws.write(rowNumber, 12, "dayName")
ws.write(rowNumber, 13, "date")
ws.write(rowNumber, 14, "reportTime")
rowNumber += 1
for ReportName in totalWeather:
    print(ReportName)
    url="https://prodapi.metweb.ie/monthly-data/Athenry"
    print(url)
    response= requests.get(url)
    weatherReport = response.json()
    for row in weatherReport["rows"]:
        ws.write(rowNumber, 0, "name")
        ws.write(rowNumber, 1, "temperature")
        ws.write(rowNumber, 2, "symbol")
        ws.write(rowNumber, 3, "weatherDescription")
        ws.write(rowNumber, 4, "text")
        ws.write(rowNumber, 5, "windSpeed")
        ws.write(rowNumber, 6, "windGust")
        ws.write(rowNumber, 7, "cardinalWindDirection")
        ws.write(rowNumber, 8, "windDirection")
        ws.write(rowNumber, 9, "humidity")
        ws.write(rowNumber, 10, "rainfall")
        ws.write(rowNumber, 11, "pressure")
        ws.write(rowNumber, 12, "dayName")
        ws.write(rowNumber, 13, "date")
        ws.write(rowNumber, 14, "reportTime")
        rowNumber += 1
w.save('weather.xls')
# save that to a file
filename = 'weatherReport.json'

# writing the JSON code
f = open(filename, 'w')
json.dump(data, f, indent=4)

