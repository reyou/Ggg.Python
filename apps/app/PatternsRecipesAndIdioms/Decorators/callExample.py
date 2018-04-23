# The first is used to initialise newly created object,
# and receives arguments used to do that:
class Foo:
    def __init__(self, a, b, c):
        print("Foo.init", a, b, c)


x = Foo(1, 2, 3)

# The second implements function call operator.
class FooCall:
    def __call__(self, a, b, c):
        print("Foo.call", a, b, c)


y = FooCall()
y(1, 2, 3)
