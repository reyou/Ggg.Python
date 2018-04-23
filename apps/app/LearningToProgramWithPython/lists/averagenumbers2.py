def main():
    numberOfEntries = 5
    print("Enter " + str(numberOfEntries) + "below:")
    total = 0
    for i in range(0, numberOfEntries + 1):
        enteredValue = input("Enter number " + str(i) + ": ")
        total += int(enteredValue)
    average = total / numberOfEntries
    print("Total is " + str(total))
    print("Average is " + str(average))


main()
