fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    # use the rstrip method which strips whitespace from
    # the right side of a string as follows:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
