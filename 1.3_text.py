"""
There are 10 types of people.
Those who know binary and those who don't. 
I said: There are 10 types of people.
I also said: 'Those who know binary and those who don't. '
Isn't the joke funny?! False
This is the left side of...a string with a right side.
"""

types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"

do_not = "don't"

y = f"Those who know {binary} and those who {do_not}. "

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_eval = "Isn't the joke funny?! {}"

print(joke_eval.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
