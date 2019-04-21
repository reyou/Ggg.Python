# https://docs.python.org/3/library/functions.html#property
class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


c_ins = C()
c_ins.x = "this is a test value"
print("\nc_ins.x:")
print(c_ins.x)
