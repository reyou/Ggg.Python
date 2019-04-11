def search4vowels(word):
    """Display any vowels found in an asked-for word."""
    vowels = set("aeiou")    
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)
    return bool(found)

word = input("Provide a word to search for vowels: ")
isfound = search4vowels(word)
print(isfound)