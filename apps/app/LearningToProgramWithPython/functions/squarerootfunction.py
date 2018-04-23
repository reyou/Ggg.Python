# Computes the approximate square root of val
# val is an number
def square_root(val):
    # Compute a provisional square root
    root = 1.0
    # How far off is our provisional root?
    diff = root * root - val
    # Loop until the provisional root
    # is close enough to the actual root
    while diff > 0.00000001 or diff < -0.00000001:
        print("qqq while diff > 0.00000001 or diff < -0.00000001:")
        print("qqq while " + str(diff) + " > 0.00000001 or " + str(diff) + " < -0.00000001:")
        print("\n")

        print("www Compute new provisional root")
        print("www root = (root + val / root) / 2")
        print("www " + str(root) + " = (" + str(root) + " + " + str(val) + " / " + str(root) + ") / 2")
        root = (root + val / root) / 2
        print("www root", root)
        print("\n")
        print("eee How bad is our current approximation?")
        print("eee diff = root * root - val")
        print("eee " + str(diff) + " = " + str(root) + " * " + str(root) + " - " + str(val) + "")
        diff = root * root - val
        print("eee diff", diff)
        print("\n")
    return root


def main():
    # Get value from the user
    num = float(input("Enter number: "))
    # Report square root
    print("Square root of", num, "=", square_root(num))


main()
