"""In multiprocessing, processes are spawned by creating 
a Process object and then calling its start() method. 
Process follows the API of threading.Thread. 
A trivial example of a multiprocess program is"""
from multiprocessing import Process


def f(name):
    print('hello', name)


if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    print("\n begin start processs")
    p.start()
    print("\n end start processs")
    p.join()
    print("\n end join")
