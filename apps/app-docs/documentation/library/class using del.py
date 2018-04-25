"""
Temporary files.
This module provides generic, low- and high-level interfaces 
for creating temporary files and directories. All of the 
interfaces provided by this module can be used without 
fear of race conditions except for 'mktemp'. 'mktemp' is subject 
to race conditions and should not be used; it is provided for 
backward compatibility only.
"""
import tempfile
"""
Utility functions for copying and archiving files and directory trees.
XXX The functions here don't copy the resource fork or other metadata on Mac.
"""
import shutil


class TempDir:
    def __init__(self):
        """
        User-callable function to create and return a unique 
        temporary directory. The return value is the pathname 
        of the directory.
        """
        self.name = tempfile.mkdtemp()

    def remove(self):
        """
        Recursively delete a directory tree.
        """
        if self.name is not None:
            shutil.rmtree(self.name)
            self.name = None
    """
    property(fget=None, fset=None, fdel=None, doc=None) -> property attribute
    fget is a function to be used for getting an attribute value, and likewise 
    fset is a function for setting, and fdel a function for del'ing, an attribute. 
    Typical use is to define a managed attribute x:
    """
    @property
    def removed(self):
        return self.name is None

    def __del__(self):
        self.remove()
