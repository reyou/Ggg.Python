# Metaprogramming/SimpleMeta1.py
# Two-step metaclass creation in Python 2.x
class SimpleMeta1(type):
    def __init__(cls, name, bases, nmspc):
        super(SimpleMeta1, cls).__init__(name, bases, nmspc)
        """Lambda expressions (sometimes called lambda forms) are used to create anonymous functions. 
        The expression lambda arguments: expression yields a function object. 
        The unnamed object behaves like a function object defined with"""
        cls.uses_metaclass = lambda self: "Yes!"


class Simple1(object):
    __metaclass__ = SimpleMeta1

    def foo(self): pass

    @staticmethod
    def bar(): pass


simple = Simple1()
print([m for m in dir(simple) if not m.startswith('__')])
