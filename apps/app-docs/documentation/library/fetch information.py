"""
JSON (JavaScript Object Notation) http://json.org is a subset of 
JavaScript syntax (ECMA-262 3rd edition) used as a lightweight 
data interchange format.
"""
import json
"""
module pprint
Support to pretty-print lists, tuples, & dictionaries recursively.
Very simple, but useful, especially in debugging data structures.
"""
import pprint
"""
request
An extensible library for opening URLs using a variety of protocols
The simplest way to use this module is to call the urlopen function, 
which accepts a string containing a URL or a Request object (described below). 
It opens the URL and returns the results as file-like object; the 
returned object has some extra methods described below.
"""
"""
Open the URL url, which can be either a string or a Request object.
"""
from urllib.request import urlopen
with urlopen('http://pypi.python.org/pypi/Twisted/json') as url:
    http_info = url.info()
    url_read = url.read()
    content_charset = http_info.get_content_charset()
    if content_charset is None:
        content_charset = "utf-8"
    raw_data = url_read.decode(content_charset)
project_info = json.loads(raw_data)
pprint.pprint(project_info)
