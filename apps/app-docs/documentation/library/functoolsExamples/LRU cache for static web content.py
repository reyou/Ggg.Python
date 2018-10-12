# https://docs.python.org/3/library/functools.html
# https://stackoverflow.com/questions/22278993/attributeerror-module-object-has-no-attribute-request
import urllib.request


def get_pep(num):
    'Retrieve text of a Python Enhancement Proposal'
    resource = 'http://www.python.org/dev/peps/pep-%04d/' % num
    try:
        with urllib.request.urlopen(resource) as s:
            assert isinstance(s.read, object)
            return s.read()
    except urllib.error.HTTPError:
        return 'Not Found'


res = get_pep(5)
print("\n", "res", "(" + str(type(res)) + ") =>")
print(res)
print("\n")
