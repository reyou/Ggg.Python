"""Generators are a simple and powerful tool for creating iterators.
They are written like regular functions but use the yield statement
whenever they want to return data"""


def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


reversed = reverse('abracadabra')
print(reversed)
print(type(reversed))
for char in reversed:
    print(char)
