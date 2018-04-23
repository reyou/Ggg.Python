# https://blog.rmotr.com/python-magic-methods-and-getattr-75cf896b3f88
"""If you ever need to use __getattribute__ to simulate something
similar to __getattr__ you’ll have to do some more advanced Python handling:
"""


class Dummy(object):
    def __getattribute__(self, attr):
        __dict__ = super(Dummy, self).__getattribute__('__dict__')
        if attr in __dict__:
            return super(Dummy, self).__getattribute__(attr)
        return attr.upper()


d = Dummy()
d.value = "Python"
print(d.value)  # "Python"
print(d.does_not_exist)  # "DOES_NOT_EXIST"
