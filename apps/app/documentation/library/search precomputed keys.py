"""
Unlike the sorted() function, it does not make sense for the bisect() 
functions to have key or reversed arguments because that would lead 
to an inefficient design (successive calls to bisect functions would not 
“remember” all of the previous key lookups).
Instead, it is better to search a list of precomputed keys to find the 
index of the record in question:
"""
import bisect

data = [('red', 5), ('blue', 1), ('yellow', 8), ('black', 0)]
data.sort(key=lambda r: r[1])
keys = [r[1] for r in data]         # precomputed list of keys
res = keys
print("\n", "keys", "(" + str(type(res)) + ") =>")
print(res)
print("\n")
res = data[bisect.bisect_left(keys, 0)]
print("\n", "res1_0", "(" + str(type(res)) + ") =>")
print(res)
print("\n")
res = data[bisect.bisect_left(keys, 1)]
print("\n", "res2_1", "(" + str(type(res)) + ") =>")
print(res)
print("\n")
res = data[bisect.bisect_left(keys, 5)]
print("\n", "res3_5", "(" + str(type(res)) + ") =>")
print(res)
print("\n")
res = data[bisect.bisect_left(keys, 8)]
print("\n", "res4_8", "(" + str(type(res)) + ") =>")
print(res)
print("\n")
