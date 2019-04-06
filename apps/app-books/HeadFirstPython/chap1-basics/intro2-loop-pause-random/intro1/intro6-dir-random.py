
import random
for item in dir(random):
    print(item, ":", type(item))
print(help(random.randint))