# Strip leading and trailing whitespace and count substrings
s = " ABCDEFGHBCDIJKLMNOPQRSBCDTUVWXYZ "
print("[", s, "]", sep="")
s = s.strip()
print("[", s, "]", sep="")

# Count occurences of the substring "BCD"
print(s.count("BCD"))

