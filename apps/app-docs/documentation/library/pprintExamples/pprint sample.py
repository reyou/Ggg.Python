import pprint
stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
# L.insert(index, object) -- insert object before index
stuff.insert(0, stuff[:])
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(stuff)
print("\n================================\n")

pp = pprint.PrettyPrinter(width=41, compact=True)
pp.pprint(stuff)
print("\n================================\n")

tup = ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead',
                                                           ('parrot', ('fresh fruit',))))))))
pp = pprint.PrettyPrinter(depth=6)
pp.pprint(tup)
print("\n================================\n")
