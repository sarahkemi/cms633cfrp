import requests
from datetime import datetime
from statistics import mean
import json

r = requests.get('http://api.cfregisters.org/play_ticket_sales')

data = r.json()

#seating capacity, date, total_sold

sales_by_year = {}

for x in data:
	date = datetime.strptime(x['date'],"%Y-%m-%d")
	year = date.year
	if x['seating_capacity'] and x['total_sold']:
		if year in sales_by_year:
			sales_by_year[year].append(int(x['seating_capacity']) * int(x['total_sold']))
		else:
			sales_by_year[year] = [int(x['seating_capacity']) * int(x['total_sold'])]


# print(sales_by_year)

#average yearly ticket slales

average_sales_by_year = {}

for year in sales_by_year:
	average_sales_by_year[year] = mean(sales_by_year[year])

print(average_sales_by_year)

#dump the averages into a file

with open('data.txt', 'w') as outfile:  
    json.dump(average_sales_by_year, outfile)

print("done!")


