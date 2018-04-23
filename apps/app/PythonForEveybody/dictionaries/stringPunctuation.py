import string

# noktalama işaretleri
print(string.punctuation)
fname = input('Enter the file name: (romeo-full.txt)')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
counts = dict()
for line in fhand:
    line = line.rstrip()
    trans = line.maketrans('', '', string.punctuation)
    line = line.translate(trans)
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] = counts[word] + 1
for count in counts:
    print(count, counts[count])
