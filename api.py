import requests
from datetime import datetime
from statistics import mean

r = requests.get('http://api.cfregisters.org/play_ticket_sales?genre=eq.com%C3%A9die&play_performance_id=lt.1000')

data = r.json()

#seating capacity, date, total_sold

sales_by_year = {}

for x in data:
	date = datetime.strptime(x['date'],"%Y-%m-%d")
	year = date.year
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




