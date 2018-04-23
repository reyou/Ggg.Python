# https://docs.python.org/3/tutorial/errors.html
# A finally clause is always executed before leaving the try statement,
# whether an exception has occurred or not.
"""In real world applications, the finally clause is useful for
releasing external resources (such as files or network connections),
regardless of whether the use of the resource was successful."""
def divide(x, y, message):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!", message)
    else:
        print("result is", result, message)
    finally:
        print("executing finally clause", message)


divide(2, 1, "qqq")

divide(2, 0, "www")

divide("2", "1", "eee")
