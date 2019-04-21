# Metaprogramming/SimpleMeta3.py
# A function for __metaclass__ in Python 2.x
"""As you’ll see, Python 3 doesn’t allow the syntax of these last two examples.
Even so, the above example
makes it quite clear what’s happening: the class object is created,
then modified, then returned."""
class Simple4(object):
    def __metaclass__(name, bases, nmspc):
        cls = type(name, bases, nmspc)
        cls.uses_metaclass = lambda self: "Yes!"
        return cls


simple = Simple4()
print(simple.uses_metaclass())
