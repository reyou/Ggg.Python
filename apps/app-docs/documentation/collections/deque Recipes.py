from collections import deque


def tail(filename, n=5):
    'Return the last n lines of a file'
    with open(filename) as f:
        return deque(f, n)


res = tail(
    "C:\\Github\\Ggg\\Ggg.Python\\apps\\app\\documentation\\collections\\hamlet.txt")
print(type(res))
for item in res:
    print(item)
