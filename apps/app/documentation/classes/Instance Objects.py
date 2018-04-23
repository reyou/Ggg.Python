class XClass:
    def __init__(self, x):
        self.counter = x


x = XClass(15)
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
