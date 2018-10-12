# ==============================================================================
from time import *
from math import *


# ==============================================================================
def timeconvFun():
    print("timeconvFun")
    # Get the number of seconds
    # seconds = eval(input("Please enter the number of seconds:"))
    seconds = 38500
    print("Entered the number of seconds:", seconds)
    # First, compute the number of hours in the given number of seconds
    # Note: integer division with possible truncation
    #  3600 seconds = 1 hours+
    hours = seconds // 3600
    # Compute the remaining seconds after the hours are accounted for
    seconds = seconds % 3600
    # Next, compute the number of minutes in the remaining number of seconds
    # 60 seconds = 1 minute
    minutes = seconds // 60
    # Compute the remaining seconds after the minutes are accounted for
    seconds = seconds % 60
    # Report the results
    print(hours, "hr,", minutes, "min,", seconds, "sec")
    print("")


timeconvFun()


# ==============================================================================
def enhancedtimeconvFun():
    print("enhancedtimeconvFun")
    # File enhancedtimeconv.py
    # Get the number of seconds
    # seconds = eval(input("Please enter the number of seconds:"))
    seconds = 38500
    print("Entered number of seconds:", seconds)
    # First, compute the number of hours in the given number of seconds
    # Note: integer division with possible truncation
    hours = seconds // 3600  # 3600 seconds = 1 hours
    # Compute the remaining seconds after the hours are accounted for
    seconds = seconds % 3600
    # Next, compute the number of minutes in the remaining number of seconds
    minutes = seconds // 60  # 60 seconds = 1 minute
    # Compute the remaining seconds after the minutes are accounted for
    seconds = seconds % 60
    # Report the results
    print(hours, ":", sep="", end="")
    # Compute tens digit of minutes
    tens = minutes // 10
    # Compute ones digit of minutes
    ones = minutes % 10
    print(tens, ones, ":", sep="", end="")
    # Compute tens digit of seconds
    tens = seconds // 10
    # Compute ones digit of seconds
    ones = seconds % 10
    print(tens, ones, sep="")
    print("")


enhancedtimeconvFun()


# ==============================================================================
def datetransformerFun():
    print("datetransformerFun")
    # month = eval(input("Please enter the month as a number (1-12): "))
    month = 9
    print("Entered the month as a number (1-12): ", month)
    # day = eval(input("Please enter the day of the month: "))
    day = 25
    print("Entered the day of the month: ", day, end="\n\n")
    # Translate month into English
    if month == 1:
        print("January ", end='')
    elif month == 2:
        print("February ", end='')
    elif month == 3:
        print("March ", end='')
    elif month == 4:
        print("April ", end='')
    elif month == 5:
        print("May ", end='')
    elif month == 6:
        print("June ", end='')
    elif month == 7:
        print("July ", end='')
    elif month == 8:
        print("August ", end='')
    elif month == 9:
        print("September ", end='')
    elif month == 10:
        print("October ", end='')
    elif month == 11:
        print("November ", end='')
    else:
        print("December ", end='')
    # Add the day
    print(day, 'or', day, end='')
    # Translate month into Spanish
    if month == 1:
        print(" enero")
    elif month == 2:
        print(" febrero")
    elif month == 3:
        print(" marzo")
    elif month == 4:
        print(" abril")
    elif month == 5:
        print(" mayo")
    elif month == 6:
        print(" junio")
    elif month == 7:
        print(" julio")
    elif month == 8:
        print(" agosto")
    elif month == 9:
        print(" septiembre")
    elif month == 10:
        print(" octubre")
    elif month == 11:
        print(" noviembre")
    else:
        print(" diciembre")
    print("")


datetransformerFun()


# ==============================================================================
def timeitFun():
    print("timeitFun")
    print("Enter your name: ", end="")
    start_time = clock()
    # name = input()
    name = "Aozdemir"
    elapsed = clock() - start_time
    print(name, "it took you", elapsed, "seconds to respond")
    print("\n")


timeitFun()


# ==============================================================================
def timeadditionFun():
    print("timeadditionFun")
    sum = 0
    start = clock()
    for n in range(1, 1000001):
        sum += n
        # stop the stopwatch
    elapsed = clock() - start
    # report results
    print("sum: ", sum, "time:", elapsed)
    print("\n")


timeadditionFun()


# ==============================================================================
def measureprimespeedFun():
    print("measureprimespeedFun")
    max_value = 10000
    count = 0
    start_time = clock()  # Start timer
    # Try values from 2 (smallest prime number) to max_value
    for value in range(2, max_value + 1):
        # See if value is prime
        is_prime = True  # Provisionally, value is prime
        # Try all possible factors from 2 to value - 1
        for trial_factor in range(2, value):
            if value % trial_factor == 0:
                is_prime = False  # Found a factor
        break  # No need to continue; it is NOT prime
        if is_prime:
            count += 1  # Count the prime number
    print()  # Move cursor down to next line
    elapsed = clock() - start_time  # Stop the timer
    print("Count:", count, " Elapsed time:", elapsed, "sec")

    print("\n")


measureprimespeedFun()


# ==============================================================================
#  using the square root optimization runs over 10 times faster.
def timemoreefficientprimesFun():
    print("timemoreefficientprimesDef")
    print("using the square root optimization runs over 10 times faster.")
    max_value = 10000
    count = 0
    value = 2  # Smallest prime number
    start = clock()  # Start the stopwatch
    while value <= max_value:
        # See if value is prime
        is_prime = True  # Provisionally, value is prime
        # Try all possible factors from 2 to value - 1
        trial_factor = 2
        root = sqrt(value)
        while trial_factor <= root:
            if value % trial_factor == 0:
                is_prime = False;  # Found a factor
                break  # No need to continue; it is NOT prime
            trial_factor += 1  # Try the next potential factor
        if is_prime:
            count += 1  # Count the prime number
        value += 1  # Try the next potential prime number
    elapsed = clock() - start  # Stop the stopwatch
    print("Count:", count, " Elapsed time:", elapsed, "sec")
    print("")


timemoreefficientprimesFun()
# ==============================================================================
