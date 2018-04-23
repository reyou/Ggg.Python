class my_decorator(object):

    def __init__(self, f):
        print("inside my_decorator.__init__()")
        f()

    def __call__(self):
        print("inside my_decorator.__call__()")

# This is the reason why people argued against decorators,
# because the @ is just a little syntax sugar meaning
# “pass a function object through another function and assign
# the result to the original function.”
@my_decorator
def aFunction():
    print("inside aFunction()")


print("Finished decorating aFunction()")

aFunction()
