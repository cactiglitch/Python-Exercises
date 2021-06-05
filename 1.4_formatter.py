"""
1 2 3 4
one two three four
True False False True
{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}
Try your Own Text here Maybe a poem Or a song about fear
"""

formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))
print(formatter.format(True,False,False,True))
print(formatter.format(formatter,formatter,formatter,formatter))

print(formatter.format(
    "Try your",
    "Own Text here",
    "Maybe a poem",
    "Or a song about fear"
))
