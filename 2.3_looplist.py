"""
This is count1.
This is count2.
This is count3.
This is count4.
This is count5.
A fruit of type: apples.
A fruit of type: oranges.
A fruit of type: pears.
A fruit of type: apricots.
I got 1.
I got pennies.
I got 2.
I got dimes.
I got 3.
I got quarters.
Adding 0 to the list.
Adding 1 to the list.
Adding 2 to the list.
Adding 3 to the list.
Adding 4 to the list.
Adding 5 to the list.
Element was: 0
Element was: 1
Element was: 2
Element was: 3
Element was: 4
Element was: 5
"""


the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print(f"This is count{number}.")
    
for fruit in fruits:
    print(f"A fruit of type: {fruit}.")
    
for i in change:
    print(f"I got {i}.")

elements = []

for i in range(0,6):
    print(f"Adding {i} to the list.")
    elements.append(i)

for i in elements:
    print(f"Element was: {i}")
    
