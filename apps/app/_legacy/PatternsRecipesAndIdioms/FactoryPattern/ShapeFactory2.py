# Factory/shapefact2/ShapeFactory2.py
# Polymorphic factory methods.
from __future__ import generators
import random


class ShapeFactory:
    factories = {}

    def addFactory(id, shapeFactory):
        ShapeFactory.factories.put[id] = shapeFactory

    addFactory = staticmethod(addFactory)

    # A Template Method:
    def createShape(id):
        if id not in ShapeFactory.factories:
            ShapeFactory.factories[id] = \
                eval(id + '.Factory()')
        return ShapeFactory.factories[id].create()

    createShape = staticmethod(createShape)


class Shape(object):
    pass


class Circle(Shape):
    def draw(self): print("Circle.draw")

    def erase(self): print("Circle.erase")

    class Factory:
        def create(self): return Circle()


class Square(Shape):
    def draw(self):
        print("Square.draw")

    def erase(self):
        print("Square.erase")

    class Factory:
        def create(self): return Square()


def shapeNameGen(n):
    # Each class keeps a list of weak references to its immediate subclasses.
    # This method returns a list of all those references still alive. Example:
    types = Shape.__subclasses__()
    """The arguments to the range constructor must be integers (either built-in 
    int or any object that implements the __index__ special method). If the step 
    argument is omitted, it defaults to 1. If the start argument is omitted, 
    it defaults to 0. If step is zero, ValueError is raised"""
    for i in range(n):
        # Return a random element from the non-empty sequence seq.
        # If seq is empty, raises IndexError
        yield random.choice(types).__name__


shape_names = shapeNameGen(7)
shapes = [ShapeFactory.createShape(i)
          for i in shape_names]

for shape in shapes:
    shape.draw()
    shape.erase()
