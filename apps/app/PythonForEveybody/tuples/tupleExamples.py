t1 = ('a',)
print("t1", t1)
print("type(t1)", type(t1))
t = tuple('lupins')
print("t", t)
t = ('a', 'b', 'c', 'd', 'e')
print("t", t)
print("t[0]", t[0])
print("t[1:3]", t[1:3])
# TypeError: object doesn't support item assignment
# t[0] = 'A'
t = ('A',) + t[1:]
print("t", t)
print("(0, 1, 2) < (0, 3, 4)", (0, 1, 2) < (0, 3, 4))
print("(0, 1, 2000000) < (0, 3, 4)", (0, 1, 2000000) < (0, 3, 4))
