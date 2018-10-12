"""
The bisect() function can be useful for numeric table lookups. 
This example uses bisect() to look up a letter grade for an exam 
score (say) based on a set of ordered numeric breakpoints: 90 and 
up is an ‘A’, 80 to 89 is a ‘B’, and so on:
"""
import bisect


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    """
    Return the index where to insert item x in list a, assuming a is sorted.
    The return value i is such that all e in a[:i] have e <= x, and all 
    e in a[i:] have e > x. So if x already appears in the list, a.insert(x) 
    will insert just after the rightmost x already there.
    Optional args lo (default 0) and hi (default len(a)) bound the slice 
    of a to be searched.
    """
    # looking up for score in breakpoints table, and returns closest index.
    i = bisect.bisect(breakpoints, score)
    return grades[i]


res = [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
print("\n", "res", "(" + str(type(res)) + ") =>")
print(res)
print("\n")
