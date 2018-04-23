# https://docs.python.org/3/tutorial/inputoutput.html
# Fancier Output Formatting
"""The str() function is meant to return representations of
values which are fairly human-readable, while repr() is meant
to generate representations which can be read by the interpreter
(or will force a SyntaxError if there is no equivalent syntax). """
s = 'Hello, world.'
print(str(s))
print(repr(s))
print(str(1/7))
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
# The argument to repr() may be any Python object:
print(repr((x, y, ('spam', 'eggs'))))