print("""A workaround for apostrophes can be constructed 
using regular expressions:""")
import re


def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?", lambda mo: mo.group(0)[0].upper() + mo.group(0)[1:].lower(), s)


print("\ntitlecase('they're bill's friends.'):")
print(titlecase("they're bill's friends."))
