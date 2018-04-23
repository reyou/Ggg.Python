# Factory/Games.py
# An example of the Abstract Factory pattern.


class Obstacle:
    def action(self):
        pass


class Character:
    def interactWith(self, obstacle):
        pass


class Kitty(Character):
    def interactWith(self, obstacle):
        print("Kitty has encountered a",
              obstacle.action())


class KungFuGuy(Character):
    def interactWith(self, obstacle):
        print("KungFuGuy now battles a",
              obstacle.action())


class Puzzle(Obstacle):
    def action(self):
        return "Puzzle"


class NastyWeapon(Obstacle):
    def action(self):
        return "NastyWeapon"
# The Abstract Factory:


class GameElementFactory:
    def makeCharacter(self): pass

    def makeObstacle(self): pass
# Concrete factories:


class KittiesAndPuzzles(GameElementFactory):
    def makeCharacter(self): return Kitty()

    def makeObstacle(self): return Puzzle()


class KillAndDismember(GameElementFactory):
    def makeCharacter(self): return KungFuGuy()

    def makeObstacle(self): return NastyWeapon()


class GameEnvironment:
    """Called after the instance has been created (by __new__()), 
    but before it is returned to the caller. The arguments are those passed 
    to the class constructor expression. If a base class has an __init__() method, 
    the derived class’s __init__() method, if any, must explicitly call it to ensure 
    proper initialization of the base class part of the instance; 
    for example: super().__init__([args...])."""
    """Because __new__() and __init__() work together in constructing objects 
     (__new__() to create it, and __init__() to customize it), no non-None value 
    may be returned by __init__(); doing so will cause a TypeError to be raised 
    at runtime."""

    def __init__(self, factory):
        self.factory = factory
        self.p = factory.makeCharacter()
        self.ob = factory.makeObstacle()

    def play(self):
        self.p.interactWith(self.ob)


g1 = GameEnvironment(KittiesAndPuzzles())
g2 = GameEnvironment(KillAndDismember())
g1.play()
g2.play()
