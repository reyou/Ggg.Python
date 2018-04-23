from multiprocessing import Pool
import threading


def f(x):
    thread_id = threading.get_ident()
    print("\n thread_id")
    print(thread_id)
    return x*x


def get_thread_id(item):
    thread_id = threading.get_ident()
    return thread_id


if __name__ == '__main__':
    p = Pool(5)
    print(p.map(f, [1, 2, 3]))
    print(p.map(get_thread_id, [1, 2, 3, 4, 5, 6, 7]))
