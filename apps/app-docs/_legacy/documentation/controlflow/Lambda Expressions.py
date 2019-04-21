# They are syntactically restricted to a single expression.
# Semantically, they are just syntactic sugar for a normal
# function definition.

def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
print(f(0))
print(f(2))
print(f(22341242100))
print("//\nqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq\n")
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)
