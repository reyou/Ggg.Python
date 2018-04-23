import struct

print("\nshow the names in the module namespace")
print(dir())  # show the names in the module namespace

print("\nshow the names in the struct module")
print(dir(struct))  # show the names in the struct module


class Shape:
    def __dir__(self):
        return ['area', 'perimeter', 'location']


s = Shape()
print("\nprint(dir(s))")
print(dir(s))
