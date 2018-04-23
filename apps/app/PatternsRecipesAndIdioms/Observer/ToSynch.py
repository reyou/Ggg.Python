# Thread module emulating a subset of Java's threading model.
import threading


class ToSynch:
    def __init__(self):
        """Factory function that returns a new reentrant lock.
        A reentrant lock must be released by the thread that acquired it. 
        Once a thread has acquired a reentrant lock, the same thread may 
        acquire it again without blocking; the thread must release it once for 
        each time it has acquired it."""
        self.mutex = threading.RLock()
        self.val = 1

    def aSynchronizedMethod(self):
        """Lock the lock. blocking indicates whether we should 
        wait for the lock to be available or not. If blocking is 
        False and another thread holds the lock, the method will 
        return False immediately. If blocking is True and another 
        thread holds the lock, the method will wait for the lock to be 
        released, take it and then return True. (note: the blocking 
        operation is interruptible.)"""
        self.mutex.acquire()
        try:
            self.val += 1
            return self.val
        finally:
            self.mutex.release()


sync = ToSynch()
res = sync.aSynchronizedMethod()
print("\n res")
print(res)
