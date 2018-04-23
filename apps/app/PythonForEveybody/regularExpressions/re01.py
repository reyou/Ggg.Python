# Search for lines that contain 'From'
import re

hand = open('mbox-short.txt')
counter = 0
for line in hand:
    line = line.strip()
    if re.search('From: ', line):
        counter = counter + 1
        print(line)
print(counter, "results found.")
