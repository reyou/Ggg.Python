class Dog:
    kind = 'canine'  # class variable shared by all instances

    def __init__(self, name):
        self.name = name  # instance variable unique to each instance


d = Dog('Fido')
e = Dog('Buddy')
# shared by all dogs
print(d.kind)
# shared by all dogs
print(e.kind)
# unique to d
print(d.name)
# unique to e
print(e.name)
# static variable
print(Dog.kind)