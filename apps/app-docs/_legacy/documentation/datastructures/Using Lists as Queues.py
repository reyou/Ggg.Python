from collections import deque
# Returns a new deque object initialized left-to-right
# (using append()) with data from iterable. If iterable is not specified,
# the new deque is empty.
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print(queue.popleft())                 # The first to arrive now leaves
print(queue.popleft())                 # The second to arrive now leaves
print(queue)                           # Remaining queue in order of arrival

