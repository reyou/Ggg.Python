# reference
first = [1,2,3,4,5]
second = first
print(second)
second.append(6)
print(first)

# copy
third = first.copy()
third.append("copied")
print(first)
print(third)