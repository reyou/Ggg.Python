# https://docs.python.org/3/tutorial/stdlib.html
"""The re module provides regular expression tools for advanced string processing.
For complex matching and manipulation, regular expressions offer
succinct, optimized solutions:"""
import re
found = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(found)
sub = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print(sub)
# When only simple capabilities are needed, string methods are
# preferred because they are easier to read and debug:
rep = 'tea for too'.replace('too', 'two')
print(rep)

