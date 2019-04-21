class Counter(dict):
    def __missing__(self, key):
        print(key, "is missing")
        return 0


c = Counter()
print('first access:')
print(c['red'])
print('second assignment:')
c['red'] += 1
print('third access:')
print(c['red'])
