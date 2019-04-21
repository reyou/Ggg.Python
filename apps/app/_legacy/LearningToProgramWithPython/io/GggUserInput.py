def inputFun():
    print('Please enter some text:')
    x = input()
    print('Text entered:', x)
    print('Type:', type(x))


# inputFun()
# ==============================================================================
def addintegersFun():
    print('Please enter an integer value:')
    x = input()
    print('Please enter another integer value:')
    y = input()
    num1 = int(x)
    num2 = int(y)
    print(num1, '+', num2, '=', num1 + num2)


# addintegersFun()
# ==============================================================================
def addintegers2Fun():
    x = input('Please enter an integer value: ')
    y = input('Please enter another integer value: ')
    num1 = int(x)
    num2 = int(y)
    print(num1, '+', num2, '=', num1 + num2)


# addintegers2Fun()
# ==============================================================================
# functional composition
def addintegers3Fun():
    num1 = int(input('Please enter an integer value: '))
    num2 = int(input('Please enter another integer value: '))
    print(num1, '+', num2, '=', num1 + num2)

# addintegers3Fun()
# ==============================================================================
#  Python provides the eval function that attempts to evaluate a string in the
# same way that the interactive shell would evaluate it.
def evalfuncFun():
    x1 = eval(input('Entry x1? '))
    print('x1 =', x1, ' type:', type(x1))
    x2 = eval(input('Entry x2? '))
    print('x2 =', x2, ' type:', type(x2))
    x3 = eval(input('Entry x3? '))
    print('x3 =', x3, ' type:', type(x3))
    x4 = eval(input('Entry x4? '))
    print('x4 =', x4, ' type:', type(x4))
    x5 = eval(input('Entry x5? '))
    print('x5 =', x5, ' type:', type(x5))
evalfuncFun()
# ==============================================================================

