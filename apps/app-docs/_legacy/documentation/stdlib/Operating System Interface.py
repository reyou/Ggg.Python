# https://docs.python.org/3/tutorial/stdlib.html
"""The os module provides dozens of functions for interacting
with the operating system:"""
"""Be sure to use the import os style instead of from os import *. 
This will keep os.open() from shadowing the built-in open() 
function which operates much differently."""
import os
# Return the current working directory
# Return a string representing the current working directory.
print(os.getcwd())
# Change current working directory
"""Change the current working directory to path.
This function can support specifying a file descriptor. 
The descriptor must refer to an opened directory, not an open file.
New in version 3.3: Added support for specifying path as a 
file descriptor on some platforms.
Changed in version 3.6: Accepts a path-like object."""
os.chdir('server/accesslogs')
# Run the command mkdir in the system shell
"""Execute the command (a string) in a subshell. 
This is implemented by calling the Standard C function system(), 
and has the same limitations. Changes to sys.stdin, etc. are not 
reflected in the environment of the executed command. If command 
generates any output, it will be sent to the interpreter 
standard output stream."""
os.system('mkdir today')
