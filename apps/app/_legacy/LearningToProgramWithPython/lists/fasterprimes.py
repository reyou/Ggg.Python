# Display the prime numbers between 2 and 500
# Largest potential prime considered

MAX = 500


def main():
    # Each position in the Boolean list indicates
    # if the number of that position is not prime:
    # false means "prime," and true means "composite."
    # Initially all numbers are prime until proven otherwise
    nonPrimes = MAX * [False]

    # First prime number is 2; 0 and 1 are not prime
    nonPrimes[0] = nonPrimes[1] = True

    for i in range(2, MAX):
        # print(str(i) + " - " + str(nonPrimes[i]))
        for j in range(i * 2, MAX, i):
            nonPrimes[j] = True

    for i in range(0, MAX):
        if (nonPrimes[i] == False):
            print(i)
            # It is prime, so eliminate all of its
            # multiples that cannot be prime
            for j in range(2 * i, MAX + 1, i):
                nonPrimes[j] = True
    print()  # Move cursor down to next line


main()
