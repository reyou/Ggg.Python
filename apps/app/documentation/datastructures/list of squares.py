squares = []
for x in range(10):
    squares.append(x ** 2)

print("x", squares)

# map(func, *iterables) –> map object
# map: Make an iterator that computes the function using arguments
# from each of the iterables. Stops when the shortest iterable is exhausted.
squares = list(map(lambda x2: x2 ** 2, range(10)))
print("x2", squares)
# or, equivalently:
squares = [x3 ** 2 for x3 in range(10)]
print("x3", squares)
