from math import sqrt


# Determines the primality of a given value
# n an integer to test primality
# Returns true if n is prime, else returns false
def is_prime(n):
    result = True
    nSqrt = sqrt(n)
    dividor = 2
    # 1,2,3,4.....sqrt.....n
    while result == True and dividor <= nSqrt:
        remaining = n % dividor
        if (remaining == 0):
            result = False
        dividor = dividor + 1

    return result


# tests the primality for each int
def main():
    userInput = int(input("Until what value would you like to see the primes? "))
    for value in range(2, userInput):
        isPrime = is_prime(value)
        if (isPrime):
            print(value, end=", ")

main()
