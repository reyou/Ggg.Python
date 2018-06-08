from random import *

print("random()", random())
print("uniform(2.5, 10.0)", uniform(2.5, 10.0))
print("expovariate(1 / 5)", expovariate(1 / 5))
print("randrange(10)", randrange(10))
print("randrange(0, 101, 2)", randrange(0, 101, 2))
print("choice(['win', 'lose', 'draw'])", choice(['win', 'lose', 'draw']))
deck = 'ace two three four'.split()
print("deck", deck)
print("shuffle(deck) ", shuffle(deck))
print("deck", deck)
print("sample([10, 20, 30, 40, 50], k=4) ", sample([10, 20, 30, 40, 50], k=4))
