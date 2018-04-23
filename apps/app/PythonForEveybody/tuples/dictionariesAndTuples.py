# Converting a dictionary to a list of tuples
# is a way for us to output the contents of a
# dictionary sorted by key:

d = {'a': 10, 'b': 1, 'c': 22}
t = list(d.items())
print(t)
t.sort()
print(t)
for key, val in list(d.items()):
    print(val, key)
