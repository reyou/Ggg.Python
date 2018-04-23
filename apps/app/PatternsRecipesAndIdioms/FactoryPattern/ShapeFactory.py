# Factory/shapefact2/ShapeFactory2.py
# Polymorphic factory methods.
"""__future__ is a real module, and serves three purposes:
To avoid confusing existing tools that analyze import statements and expect to find the modules they’re importing.
To ensure that future statements run under releases prior to 2.1 at least yield runtime exceptions 
(the import of __future__ will fail, because there was no module of that name prior to 2.1).
To document when incompatible changes were introduced, and when they will be — or were — made mandatory. 
This is a form of executable documentation, and can be inspected programmatically via 
importing __future__ and examining its contents."""
from __future__ import generators
import random


class ShapeFactory:
    factories = {}

    def addFactory(id, shapeFactory):
        """Put item into the queue. If optional args block is true and timeout 
        is None (the default), block if necessary until a free slot is available. 
        If timeout is a positive number, it blocks at most timeout seconds and raises 
        the Full exception if no free slot was available within that time. 
        Otherwise (block is false), put an item on the queue if a free slot is 
        immediately available, else raise the Full exception 
        (timeout is ignored in that case)."""
        ShapeFactory.factories.put[id] = shapeFactory
    """Transform a method into a static method.
    A static method does not receive an implicit first argument. 
    To declare a static method, use this idiom"""
    addFactory = staticmethod(addFactory)
    # A Template Method:

    def createShape(id):
        # https://stackoverflow.com/questions/1323410/has-key-or-in
        if not id in ShapeFactory.factories:
            """The expression argument is parsed and evaluated as a Python 
            expression (technically speaking, a condition list) 
            using the globals and locals dictionaries as global and 
            local namespace"""
            ShapeFactory.factories[id] = eval(id + '.Factory()')
        created_factory = ShapeFactory.factories[id].create()
        return created_factory
    createShape = staticmethod(createShape)


class Shape(object):
    pass


class Square(Shape):
    def draw(self):
        print("\nSquare.draw")

    def erase(self):
        print("\nSquare.erase")

    class Factory:
        def create(self):
            return Square()


def shapeNameGen(n):
    types = Shape.__subclasses__()
    for i in range(n):
        yield random.choice(types).__name__


shape_names = shapeNameGen(3)
print("\nshape_names:")
print(shape_names)
shape_name_list = []
counter = 1
for item in shape_names:
    print("\nitem", counter, ":")
    print(item)
    shape_name_list.append(item)
    counter = counter+1

shapes = [ShapeFactory.createShape(i) for i in shape_name_list]
for shape in shapes:
    shape.draw()
    shape.erase()
