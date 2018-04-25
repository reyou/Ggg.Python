dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dishes.keys()
values = dishes.values()

# iteration
n = 0
for val in values:
    n += val
print("n:")
print(n)
print("")
# keys and values are iterated over in the same order
print("list(keys):")
print(list(keys))
print("")
print("list(values):")
print(list(values))
print("")
# view objects are dynamic and reflect dict changes
del dishes['eggs']
del dishes['sausage']
print("list(keys):")
print(list(keys))
print("")
# set operations
keys = keys & {'eggs', 'bacon', 'salad'}
print("list(keys) &:")
print(list(keys))
print("")
keys = keys ^ {'sausage', 'juice'}
print("list(keys) ^:")
print(list(keys))
print("")
