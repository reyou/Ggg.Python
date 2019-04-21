# factorial(n)
# Computes n!
# Returns the factorial of n.
def factorial(n):
    product = 1
    while n:
        print("qqq product *= n")
        print("qqq " + str(product) + " *= " + str(n) + "")
        print("qqq \n")
        product *= n
        n -= 1
        print("www n -= 1")
        print("www " + str(n) + " -= 1")
        print("www \n")
    return product


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
