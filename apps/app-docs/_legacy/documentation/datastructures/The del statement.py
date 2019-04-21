# The del statement can also be used to remove slices
# from a list or clear the entire list (which we did earlier
# by assignment of an empty list to the slice). For example:
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
del a[1:3]
print(a)
