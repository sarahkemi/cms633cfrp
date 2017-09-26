#just playing with the data here

import json 

data = {}
with open('data.txt') as json_file:  
    data = json.load(json_file)

years = sorted([int(x) for x in data.keys()])

print(max(years))