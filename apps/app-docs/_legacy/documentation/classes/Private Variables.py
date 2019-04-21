class Mapping:
    def __init__(self, iterable):
        print("__init__ called.")
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        print("Mapping.update called.")
        for item in iterable:
            self.items_list.append(item)
        print(self.items_list)

    __update = update  # private copy of original update() method


class MappingSubclass(Mapping):

    def update(self, keys, values):
        print("MappingSubclass.update called.")
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
        print(self.items_list)


items = ['qqq', 'www', 'eee']
values = ['aaa', 'sss', 'ddd']
qqq = MappingSubclass(items)
qqq.update(items, values)
