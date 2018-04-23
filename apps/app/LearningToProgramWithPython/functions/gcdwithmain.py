# Computes the greatest common divisor of m and n
def gdc(m, n):
    # Determine the smaller of m and n
    min = m if m < n else n
    # 1 is definetly a common factor to all ints
    largestFactor = 1
    for i in range(1, min + 1):
        if m % i == 0 and n % i == 0:
            # Found larger factor
            largestFactor = i
    return largestFactor

# Get an integer from the user
def get_int():
    return int(input("Please enter an integer: "))

# main code to execute
def main():
    n1 = get_int()
    n2 = get_int()
    print("gdc(", n1, ",", n2, ") = ", gdc(n1, n2), sep="")


# run the program
main()
