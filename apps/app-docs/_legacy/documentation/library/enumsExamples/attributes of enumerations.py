"""
Enumerations are Python classes, and can have methods 
and special methods as usual. If we have this enumeration:
"""
from enum import Enum


class Mood(Enum):
    FUNKY = 1
    HAPPY = 3

    def describe(self):
        # self is the member here
        return self.name, self.value

    def __str__(self):
        return 'my custom str! {0}'.format(self.value)
    """
    It can be called either on the class (e.g. C.f()) or on an instance 
    (e.g. C().f()). The instance is ignored except for its class. If a class 
    method is called for a derived class, the derived class object is passed 
    as the implied first argument.
    Class methods are different than C++ or Java static methods. 
    If you want those, see the staticmethod builtin.   
    """
    @classmethod
    def favorite_mood(cls):
        # cls here is the enumeration
        return cls.HAPPY


res = Mood.favorite_mood()
print("\n", "Mood.favorite_mood", "(" + str(type(res)) + ") =>")
print(res)
print("\n")
res = Mood.HAPPY.describe()
print("\n", "Mood.HAPPY.describe", "(" + str(type(res)) + ") =>")
print(res)
print("\n")
res = str(Mood.FUNKY)
print("\n", "Mood.FUNKY", "(" + str(type(res)) + ") =>")
print(res)
print("\n")
