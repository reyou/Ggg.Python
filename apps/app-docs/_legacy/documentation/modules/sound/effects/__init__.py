# Importing * From a Package
# https://docs.python.org/3/tutorial/modules.html
"""The import statement uses the following convention: if a package’s
__init__.py code defines a list named __all__, it is taken to be
the list of module names that should be imported when from package
import * is encountered. It is up to the package author to keep
this list up-to-date when a new version of the package is released.
Package authors may also decide not to support it, if they don’t see
a use for importing * from their package.
For example, the file sound/effects/__init__.py could
contain the following code:"""
"""This would mean that from sound.effects import * would 
import the three named submodules of the sound package.
"""
__all__ = ["echo", "surround", "reverse"]
"""If __all__ is not defined, the statement from sound.effects 
import * does not import all submodules from the package sound.effects 
into the current namespace; it only ensures that the package 
sound.effects has been imported (possibly running any initialization 
code in __init__.py) and then imports whatever names 
are defined in the package. """