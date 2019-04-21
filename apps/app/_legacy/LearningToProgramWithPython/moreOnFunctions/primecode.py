# Contains the definition of the is_prime function
from math import sqrt


# Returns True if non-negative integer n is prime;
# otherwise, returns false
def is_prime(n):
    trial_factor = 2
    root = sqrt(n)
    while trial_factor <= root:
        if n % trial_factor == 0:
            return False
        trial_factor += 1
    return True

# print(is_prime(14))