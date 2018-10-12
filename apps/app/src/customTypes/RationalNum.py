class RationalNum:
    def __init__(self, num, den):
        self.numerator = num
        if den != 0:
            self.denominator = den
        else:
            print("Attempt to make an illegal rational number")
            from sys import exit
            exit(1)  # Terminate program with an error code

ratNum = RationalNum(1,-1)
print(ratNum)
