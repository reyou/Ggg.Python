class Tuple(tuple):
    def __getattr__(self, name):
        def _int(val):
            try:
                return int(val)
            except ValueError:
                return False

        if not name.startswith('_') or not _int(name[1:]):
            raise AttributeError("'tuple' object has no attribute '%s'" % name)
        index = _int(name[1:]) - 1
        return self[index]


t = Tuple(['z', 3, 'Python', -1])
print(t._1)  # 'z'
print(t._2)  # 3
print(t._3)  # 'Python'
