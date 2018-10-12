import weakref
"""
You can unregister a finalizer using its detach() method. 
This kills the finalizer and returns the arguments passed to 
the constructor when it was created.
"""


class Object:
    def __init__(self):
        print("obj initialized.")

# http://book.pythontips.com/en/latest/args_and_kwargs.html


def callback(*argv, **kwargs):
    print("callback called!")
    return 6


obj = Object()
"""
Class for finalization of weakrefable objects
finalize(obj, func, *args, **kwargs) returns a callable finalizer 
object which will be called when obj is garbage collected. The first 
time the finalizer is called it evaluates func(*arg, **kwargs) and 
returns the result. After this the finalizer is dead, and calling it 
just returns None.
"""
f = weakref.finalize(obj, callback, 1, 2, z=3)
res = f.detach()

newobj, func, args, kwargs = res
assert not f.alive
assert newobj is obj
assert func(*args, **kwargs) == 6
