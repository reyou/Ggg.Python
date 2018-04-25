# When looping through dictionaries, the key and corresponding
# value can be retrieved at the same time using the items() method.
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

print("===================")
# When looping through a sequence, the position
# index and corresponding value can be retrieved at the same
# time using the enumerate() function.
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
print("===================")
# To loop over two or more sequences at the same time,
# the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
"""Return a zip object whose .__next__() method returns a 
tuple where the i-th element comes from the i-th iterable argument. 
The .__next__() method continues until the shortest iterable 
in the argument sequence is exhausted and then it 
raises StopIteration."""
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))
print("===================")
# To loop over a sequence in reverse, first specify the
# sequence in a forward direction and then call the
# reversed() function.
for i in reversed(range(1, 10, 2)):
    print(i)
print("===================")
# To loop over a sequence in sorted order,
# use the sorted() function which returns a new
# sorted list while leaving the source unaltered.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
print("===================")
# It is sometimes tempting to change a list while you are
# looping over it; however, it is often simpler and
# safer to create a new list instead.
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)
print("===================")