travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(countryy,visited,city):
    empty = {}
    empty["country:"] = countryy
    empty["visits:"] = visited
    empty["cities:"] = city
    travel_log.append(empty) 

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log[0])



