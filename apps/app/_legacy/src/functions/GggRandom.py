from random import *


# ==============================================================================
def simplerandomFun():
    print("simplerandomFun")
    # Set random number seed
    # The seed function establishes the initial value from which the
    # sequence of pseudorandom numbers is generated
    seed(23)
    for i in range(0, 5):
        rand = randrange(1, 10)
        print(rand, end=" ")
    print("\n")


simplerandomFun()


# ==============================================================================
