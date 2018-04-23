from time import clock


class Stopwatch:
    def __init__(self):
        self.__running = False
        self.__elapsed = 0
        self.reset()

    # Start the timer
    def start(self):
        if not self.__running:
            self.__start_time = clock()
            # Clock now running
            self.__running = True
        else:
            print("Stopwatch already running")

    # Stop the timer
    def stop(self):
        if self.__running:
            self.__elapsed += clock() - self.__start_time
            self.__running = False
            print("Elapsed:", self.__elapsed)
        else:
            print("Stopwatch not running")
    def elapsed(self):
        return self.__elapsed
    # Reveal the elapsed time
    def reset(self):
        if not self.__running:
            return self.__elapsed
        else:
            print("Stopwatch must be stopped")
            return None

"""
def main():
    stopWatch = Stopwatch()
    stopWatch.start()
    stopWatch.stop()
    stopWatch.stop()
    stopWatch.start()
    stopWatch.reset()


main()
"""

