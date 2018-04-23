import pprint
"""Module pprint 
Support to pretty-print lists, tuples, & dictionaries recursively.
Very simple, but useful, especially in debugging data structures."""
"""pprint. pprint ( object, stream=None, indent=1, width=80, depth=None, 
*, compact=False )
Prints the formatted representation of object on stream, followed 
by a newline. If stream is None, sys.stdout is used. 
This may be used in the interactive interpreter instead of 
the print() function for inspecting values (you can even reassign 
print = pprint.pprint for use within a scope). indent, width, 
depth and compact will be passed to the PrettyPrinter constructor 
as formatting parameters."""
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
                                                        'yellow'], 'blue']]]

pprint.pprint(t, width=30)
