# If you don’t need the removed value, you can use the del operator:
t = ['a', 'b', 'c']
del t[1]
print(t)
# If you know the element you want to remove
# (but not the index), you can use remove:
t = ['a', 'b', 'c']
t.remove('b')
print(t)
# To remove more than one element, you can use del with a slice index:
t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print(t)
