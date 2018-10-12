# https://docs.python.org/3/library/itertools.html#itertool-functions
from itertools import *
import operator

def accumulate(iterable, func=operator.add):
    'Return running totals'
    # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
    # accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
    it = iter(iterable)
    try:
        total = next(it)
    except StopIteration:
        return
    yield total
    for element in it:
        total = func(total, element)
        yield total


data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
print("qqq:")
print(list(accumulate(data, operator.mul)))    # running product

print("www:")
print(list(accumulate(data, max)))              # running maximum

cashflows = [1000, -90, -90, -90, -90]
print("eee:")
print(list(accumulate(cashflows, lambda bal, pmt: bal*1.05 + pmt)))

logistic_map = lambda x, _:  r * x * (1 - x)
r = 3.8
x0 = 0.4
inputs = repeat(x0, 36)     # only the initial value is used
print("rrr:")
print([format(x, '.2f') for x in accumulate(inputs, logistic_map)])

