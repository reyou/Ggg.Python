import weakref, gc


class A:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


a = A(10)  # create a reference
""" WeakValueDictionary: Mapping class that references values weakly. 
Entries in the dictionary will be discarded when no strong reference 
to the value exists any more."""
d = weakref.WeakValueDictionary()
d['primary'] = a  # does not create a reference
d['primary']  # fetch the object if it is still alive

del a  # remove the one reference
gc.collect()  # run garbage collection right away

try:
    d['primary']  # entry was automatically removed
except Exception as ex:
    print("Exception:", ex)

d['primary']  # entry was automatically removed
