# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# Functional tools for creating and using iterators.
import itertools


def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    chars = {"2": ['a', 'b', 'c'],
             "3": ['d', 'e', 'f'],
             "4": ['g', 'h', 'i'],
             "5": ['j', 'k', 'l'],
             "6": ['m', 'n', 'o'],
             "7": ['p', 'q', 'r', 's'],
             "8": ['t', 'u', 'v'],
             "9": ['w', 'x', 'y', 'z']}
    print("chars:", type(chars))
    cumulativeList = chars[digits[0]]
    print("cumulativeList:", cumulativeList)
    for c in digits[1:]:
        # Functional tools for creating and using iterators.
        """Cartesian product of input iterables. Roughly equivalent to nested for-loops 
        in a generator expression. For example, product(A, B) returns the same as ((x,y) 
        for x in A for y in B)."""
        print("chars[c]:", chars[c])
        tempList = list(itertools.product(cumulativeList, chars[c]))
        print("tempList:", tempList)
        cumulativeList = [''.join(item) for item in tempList]
        print("cumulativeList:", cumulativeList)

    return cumulativeList


result = letterCombinations("23")
print("result:", result)
