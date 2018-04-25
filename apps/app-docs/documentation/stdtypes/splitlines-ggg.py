res1 = 'ab c\n\nde fg\rkl\r\n'.splitlines()

res2 = 'ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True)

"""Unlike split() when a delimiter string sep is given, 
this method returns an empty list for the empty string, 
and a terminal line break does not result in an extra line:"""
res3 = "".splitlines()

res4 = ''.split('\n')

res5 = 'Two lines\n'.split('\n')

print("res1:")
print(res1)
print("res2:")
print(res2)
print("res3:")
print(res3)
print("res4:")
print(res4)
print("res5:")
print(res5)
