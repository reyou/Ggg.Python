from random import randrange

'''
    Produce a list of pseudorandom integers.
    The list's length is chosen pseudorandomly in the
    range 3-20.
    The integers in the list range from -50 to 50.
    :return:
    '''


def rand_list():
    result = []
    count = randrange(3, 20)
    for i in range(count):
        result += [randrange(-50, 50)]
    return result


def selection_sort(lst):
    pivCounter = 0
    for q in range(0, len(lst)):
        pivCounter = pivCounter + 1
        minIndex = q
        for w in range(pivCounter, len(lst)):
            current = lst[w]
            if (current < lst[minIndex]):
                minIndex = w
        swap(lst, minIndex, q)


def selection_sort2(lst):
    '''
    Arranges the elements of list lst in ascending order.
    The contents of lst are physically rearranged.
    '''
    n = len(lst)
    for i in range(n - 1):
        # Note: i, small, and j represent positions within lst
        # lst[i], lst[small], and lst[j] represent the elements at
        # those positions.
        # small is the position of the smallest value we've seen
        # so far; we use it to find the smallest value less
        # than lst[i]
        small = i
        # See if a smaller value can be found later in the list
        # Consider all the elements at position j, where i < j < n
        for j in range(i + 1, n):
            if lst[j] < lst[small]:
                small = j  # Found a smaller value
        # Swap lst[i] and lst[small], if a smaller value was found
        if i != small:
            lst[i], lst[small] = lst[small], lst[i]


def swap(array, index1, index2):
    if (index1 == index2):
        return
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp


randList1 = rand_list()
print("randList1", randList1)
selection_sort(randList1)
print("selection_sort", randList1)
randList2 = rand_list()
print("//============================")
print("randList2", randList2)
selection_sort2(randList2)
print("selection_sort2", randList2)
