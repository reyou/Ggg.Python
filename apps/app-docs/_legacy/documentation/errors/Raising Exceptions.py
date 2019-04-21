# https://docs.python.org/3/tutorial/errors.html
# https://docs.python.org/2/library/exceptions.html
"""raise: If no expressions are present, raise re-raises the last
exception that was active in the current scope. If no exception is
active in the current scope, a RuntimeError exception is raised
indicating that this is an error."""
"""Raised when a local or global name is not found.
This applies only to unqualified names. The associated value
is an error message that includes the name that could
not be found."""
raise NameError('HiThere')