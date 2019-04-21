import re
"""Scan through string looking for the first location where the 
regular expression pattern produces a match, and return a corresponding match object. 
Return None if no position in the string matches the pattern; note that this is 
different from finding a zero-length match at some point in the string."""
m = re.search('(?<=abc)def', 'abcdef')
print(m)
g = m.group(0)
print(g)
#
m = re.search(r'(?<=-)\w+', 'spam-egg')
g = m.group(0)
print(g)
