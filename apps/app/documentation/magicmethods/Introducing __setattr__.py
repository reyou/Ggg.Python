"""Although implementing __setattr__ is not that common of a practice, 
we thought we'd include a discussion of it for the sake of completeness. 
Basically, __setattr__ allows you to override Python's default mechanism 
for member assignment."""
"""Implementing __setattr__ can lead to some really nasty-looking code. 
Because you end up writing the following statement an awful lot: 
object.__setattr__(self, name, value). If you fine-grained control of member 
assignment, you are almost always better off using properties instead."""


class Test(object):
    def __init__(self):
        self.a = 'a'
        self.b = 'b'

    def __setattr__(self, name, value):
        print('set %s to %s' % (name, repr(value)))

        if name in ('a', 'b'):
            print("setting", 'a or b')
            object.__setattr__(self, name, value)


t = Test()
t.c = 'z'
setattr(t, 'd', '888')
print("\n getattr")
print(getattr(t, "a"))
