# We require the set: { 'Bob', 'John', 'Alice' }
names = ['Bob', 'JOHN', 'alice', 'bob', 'ALICE', 'J', 'Bob']

updatedNames = [name[0].upper() + name[1:].lower() for name in names if len(name) > 0]
print(updatedNames)
