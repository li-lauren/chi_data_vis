import json

# Count and store the number of tickets per month in both 2019 and 2020
months = [1,2,3,4,5,6,7]

# hash tables for each year where key=month, value=count
h_2019 = {}
h_2020 = {}

for month in months:
    h_2019[month] = 0
    h_2020[month] = 0

def get_tickets_per_month (json_path, h):
    with open(json_path) as f:
        data = json.load(f)

        for ticket in data['features']:
            month = int(ticket['properties']['NOV_DATE'][0])
            h[month] += 1


get_tickets_per_month('data/urin_rec_2019.json', h_2019)
get_tickets_per_month('data/urin_rec_2020.json', h_2020)

print(h_2019)
print(h_2020)