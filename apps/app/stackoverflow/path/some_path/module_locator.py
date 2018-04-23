"""This module provides access to some objects used or maintained 
by the interpreter and to functions that interact strongly 
with the interpreter."""
import sys
import os


def we_are_frozen():
    # All of the modules are built-in to the interpreter, e.g., by py2exe
    """Return whether the object has an attribute with the given name.
This is done by calling getattr(obj, name) and catching AttributeError."""
    return hasattr(sys, "frozen")


def module_path():
    if we_are_frozen():
        return os.path.dirname(str(sys.executable))
    return os.path.dirname(str(__file__))
