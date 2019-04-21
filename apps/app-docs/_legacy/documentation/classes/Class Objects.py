class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

    """The instantiation operation (“calling” a class object) 
    creates an empty object. Many classes like to create objects 
    with instances customized to a specific initial state. 
    Therefore a class may define a special method 
    named __init__(), like this:"""

    def __init__(self):
        print("__init__ called.")
        self.data = []


qqq = MyClass()
print(qqq.f())
print(qqq.i)
