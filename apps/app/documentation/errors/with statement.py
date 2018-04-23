# Predefined Clean-up Actions
"""The with statement allows objects like files to be used in
a way that ensures they are always cleaned up promptly and correctly.
"""
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
