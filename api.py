import requests
from datetime import datetime
from statistics import mean
from collections import Counter
import json

r = requests.get('http://api.cfregisters.org/play_ticket_sales')

data = r.json()

#seating capacity, date, total_sold

sales_by_year = {}

for x in data:
	date = datetime.strptime(x['date'],"%Y-%m-%d")
	year = date.year
	if x['seating_capacity'] and x['total_sold'] and x['title'] and x['genre'] and x['author']:
		if year in sales_by_year:
			sales_by_year[year]['sales'].append(int(x['seating_capacity']) * int(x['total_sold']))
			sales_by_year[year]['title'].append(x['title'])
			sales_by_year[year]['genre'].append(x['genre'])
			sales_by_year[year]['author'].append(x['author'])
		else:
			sales_by_year[year] = {'sales':[int(x['seating_capacity']) * int(x['total_sold'])],'title': [x['title']], 'genre': [x['genre']], 'author': [x['author']]}

# print(sales_by_year)

#average yearly ticket slales

average_sales_by_year = {}

for year in sales_by_year:
	titles = Counter(sales_by_year[year]['title'])
	pop_title = titles.most_common()[0][0]
	genres = Counter(sales_by_year[year]['genre'])
	pop_genre = genres.most_common()[0][0]
	authors = Counter(sales_by_year[year]['author'])
	pop_author = authors.most_common()[0][0] 
	average_sales_by_year[year] = {'sales': mean(sales_by_year[year]['sales']), 'title': pop_title, 'genre': pop_genre, 'author':pop_author}

# print(average_sales_by_year)

#dump the averages into a file

with open('data.txt', 'w') as outfile:  
    json.dump(average_sales_by_year, outfile)

print("done!")


