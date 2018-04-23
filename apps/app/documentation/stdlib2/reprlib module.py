import reprlib

# reprlib: Redo the builtin repr() (representation)
# but with limits on most sizes.

qqq = reprlib.repr(set('supercalifragilisticexpialidocious'))
print(qqq)
