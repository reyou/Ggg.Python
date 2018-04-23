import random

print("\nqqq")
print(random.choice(['apple', 'pear', 'banana']))

print("\nwww")
# sampling without replacement
print(random.sample(range(100), 10) )

print("\neee")
# random float
print(random.random())

print("\nrrr")
# random integer chosen from range(6)
print(random.randrange(6))
