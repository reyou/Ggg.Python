# Fronting/ProxyDemo2.py
# Simple demonstration of the ProxyPattern pattern.
class Implementation2:
    def f(self):
        print("Implementation.f()")

    def g(self):
        print("Implementation.g()")

    def h(self):
        print("Implementation.h()")


class Proxy2:
    def __init__(self):
        self.__implementation = Implementation2()

    # https://blog.rmotr.com/python-magic-methods-and-getattr-75cf896b3f88
    def __getattr__(self, name):
        print("__getattr__.name:", name)
        return getattr(self.__implementation, name)


p = Proxy2()
p.f();
p.g();
p.h();
