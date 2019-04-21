# Listing 9.13 (badreverse.py) attempts to print the list’s elements in reverse
# order, but it fails to stay inside the bounds of the list.
def make_list():
    '''
    Builds a list from input provided by the user.
    '''
    result = []  # List to return is initially empty
    in_val = 0  # Ensure loop is entered at least once
    while in_val >= 0:
        in_val = int(input("Enter integer (-1 quits): "))
        if in_val >= 0:
            result = result + [in_val]  # Add item to list
    return result


def main():
    col = make_list()
    # Print the list in reverse
    for i in range(len(col) - 1, -1, -1):
        print(col[i], end=" ")
    print()


main()
