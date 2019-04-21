# https://regex101.com/r/i4lKqD/2/
# Search for lines that have an at sign between characters
import re

hand = open('mbox-short.txt')
counter = 0
for line in hand:
    line = line.rstrip()
    x = re.findall('\S+@\S+', line)
    if len(x) > 0:
        counter = counter + 1
        print(x)
print(counter, "results found.")

