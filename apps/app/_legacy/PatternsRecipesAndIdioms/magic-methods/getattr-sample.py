# https://blog.rmotr.com/python-magic-methods-and-getattr-75cf896b3f88
"""__getattr__
Let’s start with __getattr__. This method will allow you to “catch”
references to attributes that don’t exist in your object.
Let’s see a simple example to understand how it works:"""

"""__getattribute__
__getattribute__ is similar to __getattr__, with the important 
difference that __getattribute__ will intercept EVERY attribute 
lookup, doesn’t matter if the attribute exists or not. 
Let me show you a simple example:"""


class Dummy(object):
    def __getattr__(self, item):
        print("__getattr__ invoked: ", item)
        return item.upper()

    def __getattribute__(self, item):
        print('__getattribute__ invoked: ', item)
        return 'YOU SEE ME?' + " " + item


d = Dummy()
"""But using the __getattr__ magic method, we can intercept that 
inexistent attribute lookup and do something so it doesn’t fail:"""
d.does_not_exists
d.what_about_this_one

# But if the attribute does exist, __getattr__ won’t be invoked:
d.value = "Python"
print(d.va)
