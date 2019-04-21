eng2sp = dict()
print(eng2sp)
eng2sp["one"] = 'uno'
print(eng2sp)
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)
print(eng2sp['two'])
print(len(eng2sp))
keys = list(eng2sp.keys())
print(keys)
vals = list(eng2sp.values())
print(vals)
print('uno' in vals)
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}

# Dictionaries have a method called get that takes
# a key and a default value. If the key appears in
# the dictionary, get returns the corresponding value;
# otherwise it returns the default value. For example:
print(counts.get('jan', 0))
print(counts.get('tim', 0))