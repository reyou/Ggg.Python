# https://stackoverflow.com/questions/4906977/access-environment-variables-from-python
import os

for param in os.environ.keys():
    print("%s: %s " % (param, os.environ[param]))
