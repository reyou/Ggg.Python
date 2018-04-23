import collections
c = collections.Counter(a=4, b=2, c=0, d=-2)

print("\ntotal of all counts")
print(sum(c.values()))               # total of all counts
print("\nreset all counts")
print(c.clear())                      # reset all counts
print("\nlist unique elements")
print(list(c))                        # list unique elements
print("\nconvert to a set")
print(set(c))                          # convert to a set
print("\nconvert to a regular dictionary")
print(dict(c))                         # convert to a regular dictionary
print("\nconvert to a list of")
print(c.items())                      # convert to a list of (elem, cnt) pairs
# convert from a list of (elem, cnt) pairs
list_of_pairs = {"a": 1, "b": 2}
collections.Counter(dict(list_of_pairs))
n = 5
c.most_common()[:-n-1:-1]       # n least common elements
+c                              # remove zero and negative counts
