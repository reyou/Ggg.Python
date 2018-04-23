def random_list():
    from random import randrange
    result = []
    count = randrange(3, 20)
    for i in range(count):
        result += [randrange(-50, 50)]
    return result


def less_than(m, n):
    return m < n;


def greater_than(m, n):
    return m > n;


def selection_sort(lst, cmp):
    n = len(lst)
    for i in range(n - 1):
        small = i
        # See if a smaller value can be found later in the list
        # Consider all the elements at position j, where i < j < n.
        for j in range(i + 1, n):
            if cmp(lst[j], lst[small]):
                # Found a smaller value
                small = j
        # Swap lst[i] and lst[small], if a smaller value was found
        if i != small:
            lst[i], lst[small] = lst[small], lst[i]


def main():
    '''
    Tests the selection_sort function
    :return:
    '''
    # Make a random list
    original = random_list()
    # Make a working copy of the list
    working = original[:]
    print("Original: ", working)
    # Sort ascending
    selection_sort(working, less_than)
    print("Ascending: ", working)
    # Make a working copy of the list
    working = original[:]
    print("Original: ", working)
    # Sort descending
    selection_sort(working, greater_than)
    print("Descending: ", working)


main()
