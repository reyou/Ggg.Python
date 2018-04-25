"""This imports all names except those beginning with an
underscore (_). In most cases Python programmers do not use
this facility since it introduces an unknown set of names
into the interpreter, possibly hiding some things you have
already defined."""
from fibo import *

print(fib(1000))
print("===================")
print(fib2(1000))
