"""
----------
NY State has:  New York
OR state has:  Portland
----------
Michigan's abbreviation is:  MI
Florida's abbreviation is:  FL
----------
Michigan has:  Detroit
Florida has:  Jacksonville
----------
Oregon is abbreviated OR.
Florida is abbreviated FL.
California is abbreviated CA.
New York is abbreviated NY.
Michigan is abbreviated MI.
----------
CA has city San Francisco.
MI has city Detroit.
FL has city Jacksonville.
NY has city New York.
OR has city Portland.
----------
Oregon state is abbrevaited OR
and has city Portland
Florida state is abbrevaited FL
and has city Jacksonville
California state is abbrevaited CA
and has city San Francisco
New York state is abbrevaited NY
and has city New York
Michigan state is abbrevaited MI
and has city Detroit
----------
Sorry, no Texas.
The city for the state 'TX' is: Does not Exist

"""

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#add more cities
cities['NY']='New York'
cities['OR']='Portland'

print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR state has: ", cities['OR'])

print('-' * 10)
print("Michigan's abbreviation is: ",states['Michigan'])
print("Florida's abbreviation is: ",states['Florida'])

print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}.")

print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has city {city}.")

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbrevaited {abbrev}")
    print(f"and has city {cities[abbrev]}")
    
print('-' * 10)
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")
    
city = cities.get('TX', 'Does not Exist')
print(f"The city for the state 'TX' is: {city}")
