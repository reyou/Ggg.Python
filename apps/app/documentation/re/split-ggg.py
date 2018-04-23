import re
# Split string by the occurrences of pattern. If capturing parentheses are used
# in pattern, then the text of all groups in the pattern are also returned as
# part of the resulting list. If maxsplit is nonzero, at most maxsplit splits
# occur, and the remainder of the string is returned as the final element
# of the list.
res1 = re.split(r'\W+', 'Words, words, words.')

res2 = re.split(r'(\W+)', 'Words, words, words.')

res3 = re.split(r'\W+', 'Words, words, words.', 1)

res4 = re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)

print(res1)
print(res2)
print(res3)
print(res4)

try:
    res5 = re.split("^$", "foo\n\nbar\n", flags=re.M)
    print(res5)
except Exception as ex:
    print(ex)


text = """Ross McFluff: 834.345.1254 155 Elm Street

Ronald Heathmore: 892.345.3428 436 Finley Avenue
Frank Burger: 925.541.7625 662 South Dogwood Way


Heather Albrecht: 548.326.4584 919 Park Place"""

entries = re.split("\n+", text)

print("\nentries:")
print(entries)

print("\nitems:")
for item in entries:
    print(item)
