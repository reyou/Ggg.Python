def readFile(fileName):
    file = open(fileName)
    for line in file:
        print(line)
    file.close()


readFile("data.dat")
