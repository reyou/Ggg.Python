# https://stackoverflow.com/a/5748583/929902
import os
"""Get useful information from live Python objects.
This module encapsulates the interface provided by the internal 
special attributes (co_*, im_*, tb_*, etc.) in a friendlier fashion. 
It also provides some help for examining source code and class layout."""
import inspect


def module_path(local_function):
    ''' returns the module path without the use of __file__.  Requires a function defined
    locally in the module.
    from http://stackoverflow.com/questions/729583/getting-file-path-of-imported-module'''
    return os.path.abspath(inspect.getsourcefile(local_function))


if (__name__ == "__main__"):
    print("Yo!")
