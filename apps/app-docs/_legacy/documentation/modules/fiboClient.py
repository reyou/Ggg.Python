"""Each module has its own private symbol table, which is used as
the global symbol table by all functions defined in the module.
Thus, the author of a module can use global variables in the
module without worrying about accidental clashes with a user’s
global variables. On the other hand, if you know what you are
doing you can touch a module’s global variables with the same notation
used to refer to its functions, modname.itemname.
"""
import fibo

print(fibo.fib(1000))
print("===================")
print(fibo.fib2(100))
print("===================")
print(fibo.__name__)
print("===================")
fiboClient = fibo.fib
fiboClient(2000)
print("===================")