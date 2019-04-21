"""
Functional tools for creating and using iterators.
Infinite iterators: count(start=0, step=1) --> start, start+step, 
start+2*step, ... cycle(p) --> p0, p1, ... plast, p0, p1, ... 
repeat(elem [,n]) --> elem, elem, elem, ... endlessly or up to n times
"""
import itertools
from heapq import heappush
from heapq import heappop
pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count


def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    """
    Retrieve the next item from the iterator by calling its next() 
    method. If default is given, it is returned if the iterator is 
    exhausted, otherwise StopIteration is raised.
    """
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heappush(pq, entry)


def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED


def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heappop(pq)
        print("\n", "priority", "(" + str(type(priority)) + ") =>")
        print(priority)
        print("\n")
        print("\n", "count", "(" + str(type(count)) + ") =>")
        print(count)
        print("\n")
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')


class Task:
    def __init__(self, title):
        self.title = title


task_create = Task("create")
add_task(task_create, 3)
task_read = Task("read")
add_task(task_read, 1)
task_update = Task("update")
add_task(task_update, 2)
task_delete = Task("delete")
add_task(task_delete, 4)
# popping task title: read (and deletes from queue)
task = pop_task()
print("\n", "task", "(" + str(type(task)) + ") =>")
print(task.title)
print("\n")
# removes task title: update
remove_task(task_update)
# popping task title: create
task = pop_task()
print("\n", "task", "(" + str(type(task)) + ") =>")
print(task.title)
print("\n")
