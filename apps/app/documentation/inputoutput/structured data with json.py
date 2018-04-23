# https://docs.python.org/3/tutorial/inputoutput.html
# https://docs.python.org/3/library/pickle.html#module-pickle
import json

dump = json.dumps([1, 'simple', 'list'])
print(dump)
x = [1, 2, 3],
f = open('json.dump.txt', 'w')
json.dump(x, f)
print("file written.")
f = open('json.dump.txt', 'r')
x = json.load(f)
print(x)