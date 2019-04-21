# Fancier Output Formatting
# https://docs.python.org/3/tutorial/inputoutput.html
# https://docs.python.org/3/library/string.html#formatstrings
"""Basic usage of the str.format() method looks like this:"""
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print("======================================")

"""The brackets and characters within them (called format fields) 
are replaced with the objects passed into the str.format() method. 
A number in the brackets can be used to refer to the position 
of the object passed into the str.format() method."""
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))
print("======================================")

"""If keyword arguments are used in the str.format() method, 
their values are referred to by using the name of the argument."""
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
print("======================================")

"""Positional and keyword arguments can be arbitrarily combined:"""
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
print("======================================")

"""'!a' (apply ascii()), '!s' (apply str()) and '!r' 
(apply repr()) can be used to convert the value before it 
is formatted:"""
contents = 'eels'
print('My hovercraft is full of {}.'.format(contents))
print('My hovercraft is full of {!r}.'.format(contents))
print("======================================")

"""An optional ':' and format specifier can follow the field name. 
This allows greater control over how the value is formatted. 
The following example rounds Pi to three places after the decimal."""
import math

print('The value of PI is approximately {0:.3f}.'.format(math.pi))
print("======================================")

"""Passing an integer after the ':' will cause that field to be a 
minimum number of characters wide. This is useful for making 
tables pretty."""
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))
print("======================================")

"""If you have a really long format string that you don’t want to split up, 
it would be nice if you could reference the variables to be 
formatted by name instead of by position. This can be done by 
simply passing the dict and using square brackets '[]' to 
access the keys"""
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))
print("======================================")

"""This could also be done by passing the table as keyword arguments 
with the ‘**’ notation."""
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
print("======================================")
