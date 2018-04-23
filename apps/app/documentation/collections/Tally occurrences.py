import collections
# Tally occurrences of words in a list
# A counter tool is provided to support convenient and rapid tallies. For example:
cnt = collections.Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
print("cnt:")
print(cnt)
# Find the ten most common words in Hamlet
import re
path_file = "C:\\Github\\Ggg\\Ggg.Python\\apps\\app\\documentation\\collections\\hamlet.txt"
words = re.findall(r'\w+', open(path_file).read().lower())
# Dict subclass for counting hashable items. Sometimes
# called a bag or multiset. Elements are stored as
# dictionary keys and their counts are stored as dictionary
# values.
most_common = collections.Counter(words).most_common(10)
print("most_common:")
print(most_common)
