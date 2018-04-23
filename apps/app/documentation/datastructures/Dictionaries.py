# It is best to think of a dictionary as an unordered set of key:
# value pairs, with the requirement that the keys are unique
# (within one dictionary).
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)
print("tel.keys():", tel.keys())
print("list(tel.keys()):", list(tel.keys()))
print(sorted(tel.keys()))
print('guido' in tel)
print('jack' not in tel)
# The dict() constructor builds dictionaries directly
# from sequences of key-value pairs:
qqq = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(qqq)
# In addition, dict comprehensions can be used to create
# dictionaries from arbitrary key and value expressions:
www = {x: x ** 2 for x in (2, 4, 6)}
print(www)
# When the keys are simple strings, it is sometimes easier to
# specify pairs using keyword arguments:
eee = dict(sape=4139, guido=4127, jack=4098)
print(eee)
