# The timeit module quickly demonstrates a modest performance advantage:

from timeit import Timer

print('timeit', Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())

print('timeit', Timer('a,b = b,a', 'a=1; b=2').timeit())
