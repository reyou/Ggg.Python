s = "ABCDEFGHIJK"
print(s)
for i in range(len(s)):
    print("[", s[i], "]", sep="", end="")
print()

for ch in s:
    print("<", ch, ">", sep="", end="")
print()
