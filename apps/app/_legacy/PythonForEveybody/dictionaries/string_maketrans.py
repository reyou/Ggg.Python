# https://www.tutorialspoint.com/python/string_maketrans.htm

str = "this is string example....wow!!!"
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
print("trantab", trantab)
trans = str.translate(trantab)
print(trans)
