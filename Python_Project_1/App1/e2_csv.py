# This csv module is used to read/write files in CSV format.

import csv

with open("weather.csv", 'r', encoding='utf-8') as file:
    data = list(csv.reader(file))

city = input("Enter a city: ")

for row in data:
    if row[0] == city:
        print(row[1])
