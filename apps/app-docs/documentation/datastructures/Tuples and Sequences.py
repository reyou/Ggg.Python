t = 12345, 54321, 'hello!'
print(t)
print(t[0])
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)
# Tuples are immutable:
try:
    t[0] = 88888
except Exception as err:
    print(err)
v = ([1, 2, 3], [3, 2, 1])
print(v)