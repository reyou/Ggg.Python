import difflib

# class SequenceMatcher(isjunk=None, a='', b='', autojunk=True)
s = difflib.SequenceMatcher(None, " abcd", "abcd abcd")
# def find_longest_match(alo, ahi, blo, bhi)
lm = s.find_longest_match(0, 5, 0, 9)
print("\n s:")
print(s)
print("\n lm:")
print(lm)
