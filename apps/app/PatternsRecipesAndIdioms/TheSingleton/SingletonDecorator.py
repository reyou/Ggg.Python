class SingletonDecorator:
    def __init__(self, klass):
        self.klass = klass
        self.instance = None
    """Called when the instance is “called” as a function; 
    if this method is defined, x(arg1, arg2, ...) is a shorthand for 
    x.__call__(arg1, arg2, ...).
    """
    def __call__(self, *args, **kwds):
        if self.instance == None:
            self.instance = self.klass(*args, **kwds)
        return self.instance


class foo: pass


foo = SingletonDecorator(foo)
x = foo()
y = foo()
z = foo()
x.val = 'sausage'
y.val = 'eggs'
z.val = 'spam'
print(x.val)
print(y.val)
print(z.val)
print(x is y is z)
