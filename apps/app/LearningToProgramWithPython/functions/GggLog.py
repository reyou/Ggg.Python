# ==============================================================================
def printStarsFun():
    print("printStarsFun")
    print("          *")
    print("         ***")
    print("        *****")
    print("          *")
    print("          *")
    print("          *")


#
printStarsFun()


# ==============================================================================
def printFun():
    print("printFun")
    print("Please enter an integer value: ", end='')
    print("")
    print(end='Please enter an integer value 2: ')
    print("")
    print("Please enter an integer value 3: ", end='\n')
    print("New line added above.")
    print("")
    print('A', end='')
    print('B', end='')
    print('C', end='')
    print()
    print('X')
    print('Y')
    print('Z')


printFun()


# ==============================================================================
def printSepFun():
    print("printsepFun", end='\n')
    w, x, y, z = 10, 15, 20, 25
    print("print(w, x, y, z)")
    print(w, x, y, z)
    print("print(w, x, y, z, sep=',')")
    print(w, x, y, z, sep=',', end='\n')
    print("print(w, x, y, z, sep='')")
    print(w, x, y, z, sep='', end='\n')
    print("print(w, x, y, z, sep=':')")
    print(w, x, y, z, sep=':', end='\n')
    print("print(w, x, y, z, sep='-----')")
    print(w, x, y, z, sep='-----', end='\n')


printSepFun()

# ==============================================================================
