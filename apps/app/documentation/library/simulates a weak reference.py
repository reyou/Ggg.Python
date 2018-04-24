"""
A custom ref subclass which simulates a weak reference to a bound method 
(i.e., a method defined on a class and looked up on an instance). 
Since a bound method is ephemeral, a standard weak reference cannot 
keep hold of it. WeakMethod has special code to recreate the bound 
method until either the object or the original function dies:
"""
"""
Weak reference support for Python.
This module is an implementation of PEP 205:
"""
import weakref
# This module provides access to the garbage collector for reference cycles.
import gc


class C:
    def method(self):
        print("method called!")


c = C()
"""
Return a weak reference to object. The original object can be retrieved by 
calling the reference object if the referent is still alive; if the referent is 
no longer alive, calling the reference object will cause None to be returned. 
If callback is provided and not None, and the returned weakref object is still 
alive, the callback will be called when the object is about to be finalized; 
the weak reference object will be passed as the only parameter to the callback; 
the referent will no longer be available.
"""
r = weakref.ref(c.method)
r()
"""
A custom weakref.ref subclass which simulates a weak reference to a 
bound method, working around the lifetime problem of bound methods.
"""
r = weakref.WeakMethod(c.method)
r()
# method called here
r()()

del c
"""
With no arguments, run a full collection. The optional argument may 
be an integer specifying which generation to collect. A ValueError 
is raised if the generation number is invalid.
"""
gc.collect()
r()
