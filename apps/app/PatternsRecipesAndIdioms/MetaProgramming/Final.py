# Emulating Java's 'final' (sealed)
class final(type):
    def __init__(cls, name, bases, namespace):
        super(final, cls).__init__(name, bases, namespace)
        for klass in bases:
            if isinstance(klass, final):
                """If no expressions are present, raise re-raises the last 
                exception that was active in the current scope. 
                If no exception is active in the current scope, a RuntimeError 
                exception is raised indicating that this is an error.
                Otherwise, raise evaluates the first expression as the exception object. 
                It must be either a subclass or an instance of BaseException. 
                If it is a class, the exception instance will be obtained when needed by 
                instantiating the class with no arguments. The type of the exception is the 
                exception instance’s class, the value is the instance itself."""
                raise TypeError(str(klass.__name__) + " is final")


class A(object):
    pass


class B(A):
    __metaclass__ = final


print(B.__bases__)
print("isinstance(B, final): ", isinstance(B, final))

# Produces compile-time error:
try:
    class C(B):
        pass
except Exception as ex:
    print("Exception: ", ex)
