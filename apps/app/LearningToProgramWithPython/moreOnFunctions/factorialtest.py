# factorial(n)
# Computes n!
# Returns the factorial of n.
def factorial(n):
    if n == 0:
        print("www return 1")
        print("www \n")
        return 1
    else:
        print("qqq return n * factorial(n - 1)")
        print("qqq return " + str(n) + " * factorial(" + str(n - 1) + ")")
        print("qqq \n")
        return n * factorial(n - 1)


def main():
    # Try out the factorial function
    print(" 0! = ", factorial(0))
    print("==================================")
    print(" 1! = ", factorial(1))
    print("==================================")
    print(" 6! = ", factorial(6))
    print("==================================")
    print("10! = ", factorial(10))
    print("==================================")


main()
