# If the file already exists, opening it in write
# mode clears out the old data and starts fresh, so
# be careful! If the file doesn’t exist, a new one
# is created.
fout = open("output.txt", "w")
print("fout", fout)
line1 = "This here's the wattle,\n"
fout.write(line1)
line2 = 'the emblem of our land.\n'
fout.write(line2)
# When you are done writing, you have to close the file
# to make sure that the last bit of data is physically
# written to the disk so it will not be lost if the
# power goes off.
fout.close()
fread = open("output.txt")
for line in fread:
    print("for line in fread:", line)

fread.close()
