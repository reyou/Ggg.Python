from collections import deque
import itertools
"""Another approach to using deques is to maintain a sequence 
of recently added elements by appending to the right and popping 
to the left:"""


def moving_average(iterable, n=3):
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # http://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable)
    print("\n it")
    print(it)
    d = deque(itertools.islice(it, n-1))
    d.appendleft(0)
    print("\n d")
    print(d)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        print("\n s / n")
        print(s / n)
        yield s / n


iterable = [40, 30, 50, 46, 39, 44]
res = moving_average(iterable)
print("\n res")
print(res)
