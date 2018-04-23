def binary_search(lst, seek):
    leftP = 0
    rightP = len(lst) - 1
    while (leftP <= rightP):
        # find middle
        midIndex = int((leftP + rightP) / 2)
        current = lst[midIndex]
        if (current == seek):
            return midIndex
        elif (current > seek):
            # check left
            rightP = midIndex - 1
        else:
            # check right
            leftP = midIndex + 1

    return None


def show(lst):
    '''
    Prints the contents of list lst
    '''
    for item in lst:
        print("%4d" % item, end='')  # Print element right justifies in 4 spaces
    print()  # Print newline


def draw_arrow(value, n):
    '''
    Print an arrow to value which is an element in a list.
    n specifies the horizontal offset of the arrow.
    '''
    print(("%" + str(n) + "s") % " ˆ ")
    print(("%" + str(n) + "s") % " | ")
    print(("%" + str(n) + "s%i") % (" +-- ", value))


def display(lst, value):
    '''
    Draws an ASCII art arrow showing where
    the given value is within the list.
    lst is the list.
    value is the element to locate.
    '''
    show(lst)  # Print contents of the list
    position = binary_search(lst, value)
    if position != None:
        position = 4 * position + 7;  # Compute spacing for arrow
        draw_arrow(value, position)
    else:
        print("(", value, " not in list)", sep='')
    print()

def main():
    a = [2, 5, 11, 13, 44, 80, 100, 110]
    display(a, 13)
    display(a, 2)
    display(a, 7)
    display(a, 100)
    display(a, 110)


main()
