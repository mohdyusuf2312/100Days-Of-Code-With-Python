#This is day_09 code

country = input("Add country name: ")
visits = int(input("Enter how many times you visit : "))
list_of_cities = eval(input("Enter list of cities: "))
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris","Lille","Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

def add_new_country(country, visits, list_of_cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = list_of_cities
    travel_log.append(new_country)

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favorite city was {travel_log[2]['cities'][0]}.")