# ==============================================================================
def boolvarsFun():
    print("boolvarsFun")
    # Assign some Boolean variables
    a = True
    b = False
    print('a =', a, ' b =', b)
    # Reassign a
    a = False;
    print('a =', a, ' b =', b)
    print("")


boolvarsFun()


# ==============================================================================
def betterdivisionFun():
    print("betterdivisionFun")
    # File betterdivision.py
    # Get two integers from the user
    # dividend, divisor = eval(input('Please enter two numbers to divide: '))
    dividend, divisor = 1, 5
    print("Entered two numbers to divide: ", dividend, ",", divisor)
    # If possible, divide them and report the result
    if divisor != 0:
        print(dividend, '/', divisor, "=", dividend / divisor)
    if divisor != 0:
        print("Thanks for not putting divisor as 0(zero)!")
    print("")


betterdivisionFun()


# ==============================================================================
def alternatedivisionFun():
    print("alternatedivisionFun")
    # Get two integers from the user
    # dividend, divisor = eval(input('Please enter two numbers to divide: '))
    dividend, divisor = 1, 5
    print("Entered two numbers to divide: ", dividend, ",", divisor)
    # If possible, divide them and report the result
    if divisor != 0:
        quotient = dividend / divisor
    print(dividend, '/', divisor, "=", quotient)
    if quotient == 0.2:
        print("quotient equals to 0.2!")
    print('Program finished')
    print("")


alternatedivisionFun()


# ==============================================================================
def oneZeroFun():
    print("oneZeroFun")
    if 1:
        print('one')
    if 0:
        print('zero')
    print("")


oneZeroFun()


# ==============================================================================
def leadingzerosFun():
    print("leadingzerosFun")
    # Request input from the user
    # num = eval(input("Please enter an integer in the range 0...9999: "))
    num = 100
    print("Entered an integer in the range 0...9999:", 157)
    # Attenuate the number if necessary
    if num < 0:  # Make sure number is not too small
        num = 0
    if num > 9999:  # Make sure number is not too big
        num = 9999
    print(end="[")  # Print left brace
    # Extract and print thousands-place digit
    digit = num // 1000  # Determine the thousands-place digit
    print(digit, end="")  # Print the thousands-place digit
    num %= 1000  # Discard thousands-place digit
    # Extract and print hundreds-place digit
    digit = num // 100  # Determine the hundreds-place digit
    print(digit, end="")  # Print the hundreds-place digit
    num %= 100  # Discard hundreds-place digit
    # Extract and print tens-place digit
    digit = num // 10  # Determine the tens-place digit
    print(digit, end="")  # Print the tens-place digit
    num %= 10  # Discard tens-place digit
    # Remainder is the one-place digit
    print(num, end="")  # Print the ones-place digit
    print("]")  # Print right brace
    print("")


leadingzerosFun()


# ==============================================================================
def betterfeedbackFun():
    print("betterfeedbackFun")
    # Get two integers from the user
    # dividend, divisor = eval(input('Please enter two numbers to divide: '))
    dividend, divisor = 5, 0
    print("Entered two numbers:", end=" ")
    print(dividend, divisor, sep=",")
    # If possible, divide them and report the result
    if divisor != 0:
        print(dividend, '/', divisor, "=", dividend / divisor)
    else:
        print('Division by zero is not allowed')
    print()


betterfeedbackFun()


# ==============================================================================
def samedifferentFun():
    print("samedifferentFun")
    print("d1 = 1.11 - 1.10")
    d1 = 1.11 - 1.10
    print("d2 = 2.11 - 2.10")
    d2 = 2.11 - 2.10
    print('d1 =', d1, ' d2 =', d2)
    if d1 == d2:
        print('Same')
    else:
        print('Different')
    print("")


samedifferentFun()


# ==============================================================================
# nested if statement
def checkrangeFun():
    print("checkrangeFun")
    # value = eval(input("Please enter an integer value in the range 0...10: ")
    value = 5
    print("Entered an integer value in the range 0...10:", value)
    if value >= 0:  # First check
        if value <= 10:
            print("In range")
    print("Done")
    print("")


checkrangeFun()


# ==============================================================================
def newcheckrangeFun():
    print("newcheckrangeFun")
    # value = eval(input("Please enter an integer value in the range 0...10: ")
    value = 5
    print("Entered an integer value in the range 0...10:", value)
    if value >= 0 and value <= 10:  # Only one, more complicated check
        print("In range")
    print("Done")
    print("")


newcheckrangeFun()


# ==============================================================================
def enhancedcheckrangeFun():
    print("enhancedcheckrangeFun")
    # value = eval(input("Please enter an integer value in the range 0...10: ")
    value = 50
    print("Entered an integer value in the range 0...10:", value)
    if value >= 0:  # First check
        if value <= 10:  # Second check
            print(value, "is in range")
        else:
            print(value, "is too large")
    else:
        print(value, "is too small")
        print("Done")

    print("")


enhancedcheckrangeFun()


# ==============================================================================
def elifFun():
    print("elifFun")
    # value = eval(input("Please enter an integer in the range 0...5: "))
    value = 3
    print("Entered integer in the range 0...5: ", value)
    if value < 0:
        print("Too small")
    elif value == 0:
        print("zero")
    elif value == 1:
        print("one")
    elif value == 2:
        print("two")
    elif value == 3:
        print("three")
    elif value == 4:
        print("four")
    elif value == 5:
        print("five")
    else:
        print("Too large")
    print("Done")
    print("")


elifFun()


# ==============================================================================
def conditionalExpressionFun():
    print("conditionalExpressionFun")
    # Get the dividend and divisor from the user
    divident, divisor = 10, 3
    print("Entered divident and divisor: ", divident, divisor)
    # We want to divide only if divisor is not zero; otherwise,
    # we will print an error message
    msg = divident / divisor if divisor != 0 else "Error, cannot divide by zero"
    print("Result: ", msg)
    print("")


conditionalExpressionFun()
# ==============================================================================
