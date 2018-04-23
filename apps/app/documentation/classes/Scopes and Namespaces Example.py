# https://docs.python.org/3/tutorial/classes.html
"""This is an example demonstrating how to reference
the different scopes and namespaces, and how global and
nonlocal affect variable binding:"""


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        """The nonlocal statement causes the listed identifiers
        to refer to previously bound variables in the nearest enclosing
        scope excluding globals."""
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        """The global statement is a declaration which holds for
        the entire current code block."""
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)
