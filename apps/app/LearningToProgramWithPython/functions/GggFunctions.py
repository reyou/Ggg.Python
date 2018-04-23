from math import *
from random import random


# ==============================================================================
def sqrtFun():
    print("sqrtFun")
    # get value from the user
    num = 128
    print("Number entered:", num)
    # compute the square root
    root = sqrt(num)
    # report result
    print("Square root of", num, "=", root)
    print()


sqrtFun()


# ==============================================================================
def usingsqrtFun():
    print("usingsqrtFun")
    x = 16
    # Pass a literal value and display the result
    print(sqrt(16.0))
    # Pass a variable and display the result
    print(sqrt(x))
    # Pass an expression
    print(sqrt(2 * x - 5))
    # Assign result to variable
    y = sqrt(x)
    print(y)
    # Use result in an expression
    y = 2 * sqrt(x + 16) - 4
    print(y)
    # Use result as argument to a function call
    y = sqrt(sqrt(256.0))
    print(y)
    print(sqrt(int('45')))
    print()


usingsqrtFun()


# ==============================================================================
def randomFun():
    print("randomFun")
    print("random()", random())
    print("int(random() * 100)", int(random() * 100))
    print()


randomFun()


# ==============================================================================
def mathfunctionsFun():
    print("mathfunctionsFun")
    # Computes the square root of a number: sqrt(x)= √ x
    print("sqrt(64)", sqrt(64))
    # Computes e raised a power: exp(x)= e x
    print("exp(8)", exp(8))
    # Computes the natural logarithm of a number: log(x)= log e x = lnx
    print("log(8)", log(8))
    # Computes the common logarithm of a number: log(x)= log 10 x
    print("log10(100)", log10(100))
    # Computes the cosine of a value specified in radians: cos(x) = cosx;
    # other trigonometric functions include sine, tangent, arc cosine, arc
    # sine, arc tangent, hyperbolic cosine, hyperbolic sine, and hyperbolic
    # tangent
    print("cos(0)", cos(0))
    print("cos(1)", cos(1))
    print("cos(90)", cos(90))
    print("cos(180)", cos(180))
    print("cos(360)", cos(360))
    print("cos(720)", cos(720))
    # Raises one number to a power of another: pow(x,y)= x y
    print("pow(8, 2)", pow(8, 2))
    # Converts a value in radians to degrees: degrees(x)=π180x
    print("degrees(8)", degrees(8))
    # Converts a value in degrees to radians: radians(x)=180πx
    print("radians(8)", radians(8))
    # Computes the absolute value of a number: fabs(x)= |x|
    print("fabs(-8)", fabs(-8))
    print()


mathfunctionsFun()


# ==============================================================================
def orbitdistFun():
    print("orbitdistFun")
    # Use some functions and values from the math package
    # Location of orbiting point is (x,y)
    # Location of fixed point is always (100, 0),
    # AKA (p_x, p_y). Change these as necessary.
    p_x = 100
    p_y = 0
    # Radians in 10 degrees
    radians = 10 * pi / 180
    # Precompute the cosine and sine of 10 degrees
    COS10 = cos(radians)
    SIN10 = sin(radians)
    # Get starting point from user
    # x, y = eval(input("Enter initial satellite coordinates (x,y):"))
    x, y = 10, 20
    # Compute the initial distance
    d1 = sqrt((p_x - x) * (p_x - x) + (p_y - y) * (p_y - y))
    # Let the satellite orbit 10 degrees
    x_old = x;  # Remember x's original value
    x = x * COS10 - y * SIN10  # Compute new x value
    # x's value has changed, but y's calculate depends on
    # x's original value, so use x_old instead of x.
    y = x_old * SIN10 + y * COS10
    # Compute the new distance
    d2 = sqrt((p_x - x) * (p_x - x) + (p_y - y) * (p_y - y))
    # Print the difference in the distances
    print("Difference in distances: %.3f" % (d2 - d1))
    print("")


orbitdistFun()


# ==============================================================================
def moreefficientprimes():
    print("moreefficientprimesFun")
    # max_value = eval(input('Display primes up to what value? '))
    max_value = 128
    value = 2  # Smallest prime number
    while value <= max_value:
        # See if value is prime
        is_prime = True  # Provisionally, value is prime
        # Try all possible factors from 2 to value - 1
        trial_factor = 2
        root = sqrt(value)
        while trial_factor <= root:
            if value % trial_factor == 0:
                # Found a factor
                is_prime = False;
                # No need to continue; it is NOT prime
                break
                # Try the next potential factor
            trial_factor += 1
        if is_prime:
            # Display the prime number
            print(value, end=' ')
            # Try the next potential prime number
        value += 1
        # Move cursor down to next line
    print()
    print("\n")


moreefficientprimes()


# ==============================================================================
def is_prime(n):
    print("is_prime_fun")
    trial_factor = 2
    root = sqrt(n)

    while trial_factor <= root:
        if n % trial_factor == 0:
            print(n, "is not a prime number.", "Can be divided by", trial_factor, ".")
            return False
        trial_factor += 1
    print(n, "is a prime number.")
    return True
    print("")


is_prime(53)
# ==============================================================================
