import re
"""Return the string obtained by replacing the leftmost non-overlapping 
occurrences of pattern in string by the replacement repl. If the 
pattern isn’t found, string is returned unchanged. repl can be a string 
or a function; if it is a string, any backslash escapes in it are processed. 
That is, \n is converted to a single newline character, \r is converted 
to a carriage return, and so forth. Unknown escapes such as \& are left 
alone. Backreferences, such as \6, are replaced with the substring matched 
by group 6 in the pattern. For example:"""
res = re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
             r'static PyObject*\npy_\1(void)\n{', 'def myfunc():')
print(res)
