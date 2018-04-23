
# http://www.bogotobogo.com/python/Multithread/python_multithreading_Synchronization_Lock_Objects_Acquire_Release.php
import threading
import time
"""module logging
Logging package for Python. Based on PEP 282 
and comments thereto in comp.lang.python."""
import logging
import random
"""Do basic configuration for the logging system.
This function does nothing if the root logger already has handlers configured. 
It is a convenience method intended for use by simple scripts to do one-shot 
configuration of the logging package."""
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)


class Counter(object):
    def __init__(self, start=0):
        """Create a new lock object. See help(type(threading.Lock())) 
        for information about locks."""
        logging.debug("Creating new log object.")
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        logging.debug('Waiting for a lock')
        self.lock.acquire()
        try:
            """Log a message with severity 'DEBUG' on the root logger. 
            If the logger has no handlers, call basicConfig() 
            to add a console handler with a pre-defined format"""
            logging.debug('Acquired a lock')
            self.value = self.value + 1
        finally:
            logging.debug('Released a lock')
            self.lock.release()


def worker(c):
    for i in range(2):
        r = random.random()
        logging.debug('Sleeping %0.02f', r)
        time.sleep(r)
        c.increment()
    logging.debug('Done')


if __name__ == '__main__':
    counter = Counter()
    for i in range(2):
        """A class that represents a thread of control.
        This class can be safely subclassed in a limited fashion. 
        There are two ways to specify the activity: by passing a callable 
        object to the constructor, or by overriding the run() method 
        in a subclass."""
        t = threading.Thread(target=worker, args=(counter,))
        """Start the thread's activity.
        It must be called at most once per thread object. 
        It arranges for the object's run() method to be invoked 
        in a separate thread of control."""
        t.start()

    logging.debug('Waiting for worker threads')
    """Return the current Thread object, corresponding 
    to the caller's thread of control. If the caller's thread of control 
    was not created through the threading module, a dummy thread object with 
    limited functionality is returned."""
    main_thread = threading.currentThread()
    """Return a list of all Thread objects currently alive.
The list includes daemonic threads, dummy thread objects created by 
current_thread(), and the main thread. It excludes terminated threads 
and threads that have not yet been started."""
    for t in threading.enumerate():
        if t is not main_thread:
            t.join()
    logging.debug('Counter: %d', counter.value)
