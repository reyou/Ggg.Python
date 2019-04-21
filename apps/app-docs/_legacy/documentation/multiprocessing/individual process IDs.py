# To show the individual process IDs involved, here is an expanded example:

from multiprocessing import Process
import os


def info(title):
    print("info:", title)
    print('module name:', __name__)
    """Return the parent's process id.
If the parent process has already exited, Windows machines 
will still return its id; others systems will return 
the id of the 'init' process (1)."""
    print('parent process:', os.getppid())
    # Return the current process id.
    print('process id:', os.getpid())


def f(name):
    info('function f')
    print('hello', name)


if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
