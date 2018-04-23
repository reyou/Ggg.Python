# http://www.bogotobogo.com/python/Multithread/python_multithreading_Synchronization_Lock_Objects_Acquire_Release.php
import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

logging.debug("program started.")


def locker(lock, max):
    logging.debug('Starting')
    while True:
        max = max-1
        logging.debug("max: " + str(max))
        if(max <= 0):
            return
        lock.acquire()
        try:
            logging.debug('Locking')
            time.sleep(1.0)
        finally:
            logging.debug('Not locking')
            lock.release()
        time.sleep(1.0)
    return


def worker(lock):
    logging.debug('Starting')
    num_tries = 0
    num_acquires = 0
    while num_acquires < 3:
        time.sleep(0.5)
        logging.debug('Trying to acquire')
        acquired = lock.acquire(0)
        try:
            num_tries += 1
            if acquired:
                logging.debug('Try #%d : Acquired',  num_tries)
                num_acquires += 1
            else:
                logging.debug('Try #%d : Not acquired', num_tries)
        finally:
            if acquired:
                lock.release()
    logging.debug('Done after %d tries', num_tries)


if __name__ == '__main__':
    """allocate_lock() -> lock object (allocate() is an 
    obsolete synonym) Create a new lock object. 
    See help(type(threading.Lock())) for information about locks."""
    lock = threading.Lock()

    locker = threading.Thread(target=locker, args=(lock, 10), name='Locker')
    locker.setDaemon(True)
    logging.debug("begin locker.start()")
    locker.start()

    worker = threading.Thread(target=worker, args=(lock,), name='Worker')
    logging.debug("worker locker.start()")
    worker.start()
    worker.join()
    locker.join()
