import collections
"""Return a list of the n most common elements and their 
counts from the most common to the least. If n is omitted 
or None, most_common() returns all elements in the counter. 
Elements with equal counts are ordered arbitrarily:"""
mostCommons = collections.Counter('abracadabra').most_common(3)
print(mostCommons)
