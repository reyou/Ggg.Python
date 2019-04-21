# Search for lines that start with 'From'
import re

hand = open('mbox-short.txt')
counter = 0
for line in hand:
    line = line.strip()
    #  zero-or-more characters (in the case of the asterisk)
    #  one-or-more of the characters (in the case of the plus sign)
    if re.search('^From:.+@', line):
        counter = counter + 1
        print(line)
print(counter, "results found.")
