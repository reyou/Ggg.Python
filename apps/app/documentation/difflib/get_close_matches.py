# difflib.get_close_matches GET SCORE
# https://stackoverflow.com/questions/36283391/difflib-get-close-matches-get-score
"""SequenceMatcher is a flexible class for comparing pairs of sequences of any 
type, so long as the sequence elements are hashable. The basic algorithm 
predates, and is a little fancier than, an algorithm published in the 
late 1980's by Ratcliff and Obershelp under the hyperbolic name 
"gestalt pattern matching". The basic idea is to find the longest 
contiguous matching subsequence that contains no "junk" elements 
(R-O doesn't address junk). The same idea is then applied recursively to 
the pieces of the sequences to the left and to the right of the matching subsequence. 
This does not yield minimal edit sequences, but does tend to yield matches that 
"look right" to people."""
import difflib
my_str = 'apple'
str_list = ['ape', 'fjsdf', 'aerewtg', 'dgyow', 'paepd']
print("\n str_list:")
print(str_list)
best_match = difflib.get_close_matches(my_str, str_list, 1)[0]
print("\n best_match:")
print(best_match)
score = difflib.SequenceMatcher(None, my_str, best_match).ratio()
print("\n score:")
print(score)
# You can also loop through the list and compute all the scores to check:
for word in str_list:
    print("\n score for: " + my_str + " vs. " + word + " = " +
          str(difflib.SequenceMatcher(None, my_str, word).ratio()))
