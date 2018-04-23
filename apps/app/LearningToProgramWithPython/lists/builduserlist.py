# Build a custom list of non-negative integers specified by the user
def make_list():
    '''
    Builds a list from input provided by the user.
    '''
    result = []  # List to return is initially empty
    in_val = 0  # Ensure loop is entered at least once
    while in_val >= 0:
        in_val = int(input("Enter integer (-1 quits): "))
        if in_val >= 0:
            # Add item to list
            result = result + [in_val]
    return result


def main():
    col = make_list()
    print(col)


main()
