'''
Contains the definition of the is_prime function
'''
from math import sqrt


def is_prime(n):
    '''
    Returns True if non-negative integer n is prime;
    otherwise, returns false
    '''
    trial_factor = 2
    root = sqrt(n)
    while trial_factor <= root:
        if n % trial_factor == 0:  # Is trialFactor a factor?
            return False;  # Yes, return right away
        trial_factor += 1
    return True;  # Tried them all, must be prime


print(is_prime(12))
