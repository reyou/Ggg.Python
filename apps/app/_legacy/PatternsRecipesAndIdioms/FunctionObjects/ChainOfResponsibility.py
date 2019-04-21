# http://python-3-patterns-idioms-test.readthedocs.io/en/latest/FunctionObjects.html
# FunctionObjects/ChainOfResponsibility.py

# Carry the information into the strategy:


class Messenger:
    pass

# The Result object carries the result data and
# whether the strategy was successful:


class Result:
    def __init__(self):
        self.succeeded = 0

    def isSuccessful(self):
        return self.succeeded

    def setSuccessful(self, succeeded):
        self.succeeded = succeeded


class Strategy:
    def __call__(self, messenger):
        pass

    def __str__(self):
        return "Trying " + self.__class__.__name__ \
            + " algorithm"

# Manage the movement through the chain and
# find a successful result:


class ChainLink:
    def __init__(self, chain, strategy):
        self.strategy = strategy
        self.chain = chain
        self.chain.append(self)

    def next(self):
        # Where this link is in the chain:
        location = self.chain.index(self)
        if not self.end():
            return self.chain[location + 1]

    def end(self):
        return (self.chain.index(self) + 1 >=
                len(self.chain))

    def __call__(self, messenger):
        r = self.strategy(messenger)
        if r.isSuccessful() or self.end():
            return r
        return self.next()(messenger)

# For this example, the Messenger
# and Result can be the same type:


class LineData(Result, Messenger):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data


class LeastSquares(Strategy):
    # http://farmdev.com/src/secrets/magicmethod/index.html#introducing-call
    """Implementing the __call__ magic method in a class causes its 
    instances to become callables -- in other words, those instances now behave 
    like functions. You can use the built-in function callable to test if a 
    particular object is a callable (callable returns True for functions, 
    methods, and objects that have __call__)."""

    def __call__(self, messenger):
        print(self)
        linedata = messenger
        print("LeastSquares.linedata:")
        print(linedata)
        # [ Actual test/calculation here ]
        result = LineData([1.1, 2.2])  # Dummy data
        result.setSuccessful(0)
        return result


class NewtonsMethod(Strategy):
    def __call__(self, messenger):
        print(self)
        linedata = messenger
        print("NewtonsMethod.linedata:")
        print(linedata)
        # [ Actual test/calculation here ]
        result = LineData([3.3, 4.4])  # Dummy data
        result.setSuccessful(0)
        return result


class Bisection(Strategy):
    def __call__(self, messenger):
        print(self)
        linedata = messenger
        print("Bisection.linedata:")
        print(linedata)
        # [ Actual test/calculation here ]
        result = LineData([5.5, 6.6])  # Dummy data
        result.setSuccessful(1)
        return result


class ConjugateGradient(Strategy):
    def __call__(self, messenger):
        print(self)
        linedata = messenger
        print("ConjugateGradient.linedata:")
        print(linedata)
        # [ Actual test/calculation here ]
        result = LineData([7.7, 8.8])  # Dummy data
        result.setSuccessful(1)
        return result


solutions = []
ls = LeastSquares()
ChainLink(solutions, ls)
nm = NewtonsMethod()
ChainLink(solutions, nm)
bs = Bisection()
ChainLink(solutions, bs),
cg = ConjugateGradient()
ChainLink(solutions, cg)

line = LineData([
    1.0, 2.0, 1.0, 2.0, -1.0,
    3.0, 4.0, 5.0, 4.0
])

res = solutions[0](line)
print(res)
