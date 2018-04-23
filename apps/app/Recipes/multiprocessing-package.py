# https://stackoverflow.com/questions/3310049/proper-use-of-mutexes-in-python/49453199#49453199
"""An alternative, for Python 2.6 and later, is to
use Python's multiprocessing package. It mirrors the threading
package, but will create entirely new processes which can run
simultaneously. It's trivial to update your example:"""
from multiprocessing import Process, Lock
import threading
mutex = Lock()


def processData(data, thread_safe):
    thread_id = threading.get_ident()
    if thread_safe:
        with mutex:
            print('\nProcessing data:', data, "ThreadId:", thread_id)
    else:
        print('\nProcessing data:', data, "ThreadId:", thread_id)


if __name__ == '__main__':
    counter = 0
    max_run = 10
    thread_safe = False
    while True:
        some_data = counter
        p = Process(target=processData, args=(some_data, thread_safe))
        """Start the process’s activity. This must be called at most
        once per process object. It arranges for the object’s
        run() method to be invoked in a separate process."""
        p.start()
        print("\n process started:", p.ident)
        counter = counter + 1
        if counter >= max_run:
            break
