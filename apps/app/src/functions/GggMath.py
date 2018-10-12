# ==============================================================================
def integerFun():
    print("integerFun")
    print("type(4)", type(4))
    print("type('4')", type('4'))
    print("str(4)", str(4))
    print("int(’5’)", int('5'))
    print("type(int(’3’) + int(4))", type(int('3') + int(4)))


integerFun()


# ==============================================================================
# 6.022×10 23 is written 6.022e23
def floatingPointFun():
    print("floatingPointFun")
    x = 5.62
    print("x", x)
    pi = 3.14159;
    print("Pi =", pi)
    print("or", 3.14, "for short")
    x = 23.3123400654033989
    print("x again", x)
    print("controlCodesFun")
    avogadros_number = 6.022e23
    c = 2.998e8
    print("Avogadro's number =", avogadros_number)
    print("Speed of light =", c)
    print()


floatingPointFun()


# ==============================================================================
def divideFun():
    print("divideFun")
    print("The // operator produces an integer result when used with integers")
    print("print(10 / 3, 3 / 10, 10 // 3, 3 // 10)")
    print(10 / 3, 3 / 10, 10 // 3, 3 // 10)
    print("")


divideFun()


# ==============================================================================
def modulusFun():
    print("modulusFun")
    print("print(10 % 3, 3 % 10)")
    print(10 % 3, 3 % 10)
    print("")
    print("Floating-point arithmetic always produces a floating-point result.")
    print("print(10.0 / 3.0, 3.0 / 10.0, 10.0 // 3.0, 3 // 10.0)")
    print(10.0 / 3.0, 3.0 / 10.0, 10.0 // 3.0, 3 // 10.0)
    print("")


modulusFun()


# ==============================================================================
def impreciseFun():
    print("impreciseFun")
    one = 1.0
    one_third = 1.0 / 3.0
    zero = one - one_third - one_third - one_third
    print("one = ", one, "one_third = ", one_third, "zero = ", zero)
    print("")


impreciseFun()


# ==============================================================================
def imprecise10Fun():
    print("imprecise10Fun")
    one = 1.0
    one_tenth = 1.0 / 10.0
    zero = one - one_tenth - one_tenth - one_tenth \
           - one_tenth - one_tenth - one_tenth \
           - one_tenth - one_tenth - one_tenth \
           - one_tenth
    print('one =', one, ' one_tenth =', one_tenth, ' zero =', zero)
    print("")


imprecise10Fun()


# ==============================================================================
def adderFun():
    print("adderFun")
    value1 = eval(input("Please enter a number: "))
    value2 = eval(input("Please enter another number: "))
    sum = value1 + value2
    print(value1, '+', value2, '=', sum)
    print("")


# adderFun()
# ==============================================================================
def dividedangerFun():
    print("dividedangerFun")
    # Get two integers from the user
    # a,b = map(int, input("Enter some stuff").split(","))
    dividend, divisor = eval(input('Please enter two numbers to divide: '))
    # Divide them and report the result
    print(dividend, '/', divisor, "=", dividend / divisor)
    print("")


# dividedangerFun()
# ==============================================================================
# "aozdemir"
# TypeError: unsupported operand type(s) for /: 'str' and 'int'
def halveFun():
    print("halveFun")
    # Get a number from the user
    value = eval(input('Please enter a number to cut in half: '))
    # Report the result
    print(value / 2)
    print("")


# halveFun()

# ==============================================================================
def tempconvFun():
    print("tempconvFun")
    # degreesF = input("Enter the temperature in degrees F: ")
    degreesF = 80
    degreesC = 5 / 9 * (degreesF - 32);
    print(degreesF, "degrees F = ", degreesC, "degrees C")
    print("")


tempconvFun()


# ==============================================================================
def swapFun():
    print("swapFun")
    x = 3
    y = 9
    print("Original x,y:", end=" ")
    print(x, y, sep=",")
    x, y = y, x
    print("Swapped x,y:", end=" ")
    print(x, y, sep=",")
    print("")


swapFun()
# ==============================================================================
