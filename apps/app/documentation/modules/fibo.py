"""Each module has its own private symbol table, which is used as
the global symbol table by all functions defined in the module.
Thus, the author of a module can use global variables in the
module without worrying about accidental clashes with a user’s
global variables. On the other hand, if you know what you are
doing you can touch a module’s global variables with the same notation
used to refer to its functions, modname.itemname.
"""

# Fibonacci numbers module

def fib(n):  # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()


def fib2(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result
