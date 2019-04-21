import random
#==============================================================================
print("Set 1: random.random()")
for i in range(10):
    x = random.random()
    print(x)
# ==============================================================================
print()
print("Set 2: random.randint(5, 10)")
for i in range(10):
    x = random.randint(5, 10)
    print(x)
# ==============================================================================
print()
print("Set 3: random.choice(t)")
t = range(1, 100)
for i in range(10):
    x = random.choice(t)
    print(x)
