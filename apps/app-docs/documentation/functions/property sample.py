# https://docs.python.org/3/library/functions.html#property
"""class property(fget=None, fset=None, fdel=None, doc=None)¶
Return a property attribute.
fget is a function for getting an attribute value. fset is a
function for setting an attribute value. fdel is a function for
deleting an attribute value.
And doc creates a docstring for the attribute.
A typical use is to define a managed attribute x:"""


class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")


cInstance = C()
x_get = cInstance.getx()
x_prop = cInstance.x;
print("x_get:")
print(x_get)
print("x_prop:")
print(x_prop)
