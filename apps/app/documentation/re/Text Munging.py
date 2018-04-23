"""sub() replaces every occurrence of a pattern with a string 
or the result of a function. This example demonstrates using sub() 
with a function to “munge” text, or randomize the order of all the 
characters in each word of a sentence except for the first and last characters:"""
import random
import re


def repl(m):
    inner_word = list(m.group(2))
    # Shuffle list x in place, and return None.
    random.shuffle(inner_word)
    return m.group(1) + "".join(inner_word) + m.group(3)


text = "Professor Abdolmalek, please report your absences promptly."
# def sub(pattern, repl, string, count=0, flags=0)
"""Return the string obtained by replacing the leftmost non-overlapping 
occurrences of the pattern in string by the replacement repl. repl can 
be either a string or a callable; if a string, backslash escapes in it 
are processed. If it is a callable, it's passed the match object and 
must return a replacement string to be used."""
sub1 = re.sub(r"(\w)(\w+)(\w)", repl, text)

sub2 = re.sub(r"(\w)(\w+)(\w)", repl, text)

print("\ntext:")
print(text)
print("\nsub1:")
print(sub1)
print("\nsub2:")
print(sub2)
