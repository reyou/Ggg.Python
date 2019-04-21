import re
import string
"""Escape all the characters in pattern except ASCII letters, 
numbers and '_'. This is useful if you want to match an arbitrary 
literal string that may have regular expression metacharacters in 
it. For example:"""
print()
print(re.escape('python.exe'))


legal_chars = string.ascii_lowercase + string.digits + "!#$%&'*+-.^_`|~:"
print()
print('[%s]+' % re.escape(legal_chars))


operators = ['+', '-', '*', '/', '**']
sortedVal = sorted(operators, reverse=True)
print()
print("sortedVal:")
print(sortedVal)
mappedVal = map(re.escape, sortedVal)
print()
print("mappedVal:")
print(mappedVal)
print()
joinedVal = '|'.join(mappedVal)
print("joinedVal:")
print(joinedVal)
"""This functions must not be used for the replacement string in 
sub() and subn(), only backslashes should be escaped. For example:"""

digits_re = r'\d+'
sample = '/usr/sbin/sendmail - 0 errors, 12 warnings'
print()
print(re.sub(digits_re, digits_re.replace('\\', r'\\'), sample))
