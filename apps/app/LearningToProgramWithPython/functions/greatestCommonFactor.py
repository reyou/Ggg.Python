# the following code defines a function that computes the greatest
# common divisor of two integers. It determines largest factor (divisor)
# common to its paraneters
def gdc(num1, num2):
    # determine the smaller of num1 and num2
    min = num1 if num1 < num2 else num2
    # 1 is definetly a common factor to all ints
    largestFactor = 1
    for i in range(1, min + 1):
        if num1 % i == 0 and num2 % i == 0:
            # Found larger factor
            largestFactor = i
    return largestFactor

# test function here
gdcResult = gdc(200, 16)
print(gdcResult)
