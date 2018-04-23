"""“If something is ugly, hide it inside an object.” 
This is basically what Façade accomplishes."""
"""Façade is often implemented as singleton abstract factory. 
Of course, you can easily get this effect by creating a class 
containing static factory methods:"""


class A:
    def __init__(self, x):
        print("created A")


class B:
    def __init__(self, x):
        print("created B")


class C:
    def __init__(self, x):
        print("created C")


# Other classes that aren't exposed by the
# facade go here ...


class Facade:
    def makeA(x):
        return A(x)
    makeA = staticmethod(makeA)

    def makeB(x):
        return B(x)
    makeB = staticmethod(makeB)

    def makeC(x):
        return C(x)
    makeC = staticmethod(makeC)


# The client programmer gets the objects
# by calling the static methods:
a = Facade.makeA(1)
b = Facade.makeB(1)
c = Facade.makeC(1.0)
