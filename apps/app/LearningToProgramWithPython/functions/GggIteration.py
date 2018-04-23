# ==============================================================================
def iterativecounttofiveFun():
    print("iterativecounttofiveFun")
    count = 1
    while count <= 5:
        print("count: ", count)
        count += 1
    print("")


iterativecounttofiveFun()


# ==============================================================================
def addnonnegativesFun():
    print("addnonnegativesFun")
    # Allow the user to enter a sequence of non-negative
    # numbers. The user ends the list with a negative
    # number. At the end the sum of the non-negative
    # numbers entered is displayed. The program prints
    # zero if the user provides no non-negative numbers.
    entry = 0  # Ensure the loop is entered
    sum = 0  # Initialize sum
    # Request input from the user
    print("Enter numbers to sum, negative number ends list:")
    while entry >= 0:  # A negative number exits the loop
        entry = eval(input())  # Get the value
        if entry >= 0:  # Is number non-negative?
            sum += entry  # Only add it if it is non-negative
    print("Sum =", sum)  # Display the sum
    print()


# addnonnegativesFun()
# ==============================================================================
def troubleshootloopFun():
    print("troubleshootloopFun")
    print("Help! My computer doesn't work!")
    done = False  # Not done initially
    while not done:
        print("Does the computer make any sounds (fans, etc.) ")
        choice = input("or show any lights? (y/n):")
        # The troubleshooting control logic
        if choice == 'n':  # The computer does not have power
            choice = input("Is it plugged in? (y/n):")
            if choice == 'n':  # It is not plugged in, plug it in
                print("Plug it in.")
            else:
                choice = input("Is the switch in the \"on\" position? (y/n):")
                if choice == 'n':  # The switch is off, turn it on!
                    print("Turn it on.")
                else:  # The switch is on
                    choice = input("Does the computer have a fuse? (y/n):")
                    if choice == 'n':  # No fuse
                        choice = input("Is the outlet OK? (y/n):")
                        if choice == 'n':  # Fix outlet
                            print("Check the outlet's circuit ")
                            print("breaker or fuse. Move to a")
                            print("new outlet, if necessary. ")
                        else:  # Beats me!
                            print("Please consult a service technician.")
                        done = True  # Nothing else I can do
                    else:  # Check fuse
                        print("Check the fuse. Replace if ")
                        print("necessary.")

        else:  # The computer has power
            print("Please consult a service technician.")
        done = True  # Nothing else I can do
    print("")


# troubleshootloopFun()


# ==============================================================================
def whileFun():
    print("whileFun")
    counter = 5
    while counter > 0:
        print("counter:", counter)
        counter = counter - 1;
    print("")


whileFun()


# ==============================================================================
def whileNotFun():
    print("whileNotFun")
    counter = 15
    while not (counter < 10):
        print("counter:", counter)
        counter -= 1
    print("")


whileNotFun()


# ==============================================================================
def forFun():
    print("forFun")
    # range(begin,end,step)
    for n in range(1, 5):
        print("n", n)
    print()


forFun()


# ==============================================================================
def rangeFun():
    print("rangeFun")
    # range(begin,end,step)
    for n in range(20, 1, -3):
        print(n, end=' ')
    print("\n")


rangeFun()


# ==============================================================================
def increaseFun():
    print("increaseFun")
    sum = 0
    for n in range(1, 5):
        print(n, end=' ')
        n += 1
    print("\n")


increaseFun()


# ==============================================================================
def timestableFun():
    print("timestableFun")
    # Print a multiplication table to 10 x 10
    # Print column heading
    print(" 1 2 3 4 5 6 7 8 9 10")
    print(" +----------------------------------------")
    for row in range(1, 11):
        if row < 10:
            print(" ", end="")
        print(row, "| ", end="")
        for column in range(1, 11):
            product = row * column;
            if (product < 100):
                print(end=" ")
            if (product < 10):
                print(end=" ")
            print(product, end=" ")
        print()
    print("")


timestableFun()


# ==============================================================================
def flexibletimestableFun():
    print("flexibletimestableFun")
    # Print a MAX x MAX multiplication table
    MAX = 18
    # first, print heading
    print(end="       ")
    # Print column heading numbers
    for column in range(1, MAX + 1):
        print(end=" %2i " % column)
    print()  # Go down to the next line

    # Print line separator; a portion for each column
    print(end=" +")
    for column in range(1, MAX + 1):
        print(end="----")  # Print portion of line
    print()  # Go down to the next line

    # Print table contents
    for row in range(1, MAX + 1):  # 1 <= row <= MAX, table has MAX rows
        print(end="%2i | " % row)  # Print heading for this row.
    for column in range(1, MAX + 1):  # Table has 10 columns.
        product = row * column;  # Compute product
    print(end="%3i " % product)  # Display product
    print()  # Move cursor to next row

    print("")


flexibletimestableFun()


# ==============================================================================
def permuteabcFun():
    # this takes n^3 time
    # recursive should be much lower!
    print("permuteabcFun")
    # The first letter varies from A to C
    for first in 'ABC':
        for second in 'ABC':  # The second varies from A to C
            if second != first:  # No duplicate letters allowed
                for third in 'ABC':  # The third varies from A to C
                    # Don't duplicate first or second letter
                    if third != first and third != second:
                        print(first + second + third)

    print("")


permuteabcFun()


# ==============================================================================
# break statement
def addmiddleexitFun():
    print("addmiddleexitFun")
    start = 13
    while True:
        print(start)
        start = start - 1
        if start == 7:
            break
    print()


addmiddleexitFun()


# ==============================================================================
def continueFun():
    print("continueFun")
    sum = 0
    done = False;
    val = 995
    print("Positive int entered: ", val)
    while not done:
        if (val < 0):
            print("Negavtive value", val, "ignored")
            continue;
        if (val != 999):
            print("Tallying", val)
            val += 1
        else:
            done = (val == 999);
    print("")


continueFun()


# ==============================================================================
def computesquarerootFun():
    print("computesquarerootFun")
    # Get the value from the user
    val = 81
    # Compute a provosional square root
    root = 1.0

    # How far off is our provosional root?
    diff = (root * root) - val

    # Loop until the provisional root
    # is close enough to the actual root
    while diff > 0.0000001 or diff < -0.0000001:
        # Compute the new provosional root
        root = (root + (val / root)) / 2
        # Report how we are doing
        print(root, "square is", root * root)
        # How bad is our current approximation?
        diff = root * root - val
        print("Current diff:", diff, end="\n\n")
    # Report approximate square root
    print("Square root of", val, "=", root)
    print()


computesquarerootFun()


# ==============================================================================
def startreeFun():
    print("startreeFun")
    # Get tree height from user
    height = 10
    print("Height of tree:", height)
    # Draw one row for every unit of height
    row = 0
    while row < height:
        # Print leading spaces; as row gets bigger, the number of
        # leading spaces gets smaller
        count = 0
        while count < height - row:
            print(end=" ")
            count += 1
        # Print out stars, twice the current row plus one:
        # 1. number of stars on left side of tree
        # = current row value
        # 2. exactly one star in the center of tree
        # 3. number of stars on right side of tree
        # = current row value
        count = 0
        while count < 2 * row + 1:
            print(end=" * ")
            count += 1
        # Move cursor down to next line
        print()
        row += 1  # Consider next row

    print()


startreeFun()


# ==============================================================================
def printprimesFun():
    print("printprimesFun")
    max_value = 50
    value = 2
    while value <= max_value:
        # see if value is prime
        # Provisionally, value is prime
        is_prime = True
        # try all possible factors from 2 to value -1
        trial_factor = 2
        while trial_factor < value:
            if value % trial_factor == 0:
                is_prime = False  # found a factor
                break  # no need to continue; it is NOT prime
            trial_factor += 1  # try the next potential prime factor
        if is_prime:
            print(value, end=' ')  # display the prime number
        value += 1 # try the next potential prime number
    print() # move cursor down  to next line

    print()


printprimesFun()
# ==============================================================================
