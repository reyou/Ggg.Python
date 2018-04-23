class Foo(object):
    x = "a"


print(Foo.x);
f = Foo()
print(f.x)
f2 = Foo()
print(f2.x)
f2.x = 'b'
print(f.x)
Foo.x = 'c'
print(f.x)
print(f2.x)
Foo.x = 'd'
print(f2.x)
print(f.x)
f3 = Foo()
print(f3.x)
Foo.x = 'e'
print(f3.x)
print(f2.x)