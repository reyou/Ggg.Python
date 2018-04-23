"""If no expressions are present, raise re-raises the last
exception that was active in the current scope. If no exception is
active in the current scope, a RuntimeError exception is raised
indicating that this is an error."""
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')