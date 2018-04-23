# https://regex101.com/r/i4lKqD/2/
import re

s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
# \S+ matches any non-whitespace character (equal to [^\r\n\t\f ])
lst = re.findall('\S+@\S+', s)
print(lst)
