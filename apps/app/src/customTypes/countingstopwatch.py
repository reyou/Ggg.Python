from sys import stdin

from stopwatch import Stopwatch


# This single line means that the CountingStopwatch
# class inherits everything from the Stopwatch class.
# CountingStopwatch objects automatically will have
# start, stop, reset, and elapsed methods.
class CountingStopwatch(Stopwatch):
    def __init__(self):
        # Allow superclass to do its initialization of the
        # inherited fields
        # in the __init__ method definition calls the constructor
        # of the superclass.
        super(CountingStopwatch, self).__init__()
        # Set number of starts to zero
        self.__count = 0

    def start(self):
        # Let superclass do its start code
        super(CountingStopwatch, self).start()
        # Count this start message
        self.__count += 1
        print("Started")

    def reset(self):
        # Let superclass reset the inherited fields
        super(CountingStopwatch, self).reset()
        # Reset new field
        self.__count = 0

    def count(self):
        return self.__count


countingStopwatch = CountingStopwatch()
countingStopwatch.start()
stdin.read(1)
