def search4vowels(word:str) -> set:
    """Display any vowels found in an asked-for word."""
    vowels = set("aeiou")    
    return vowels.intersection(set(word))

word = input("Provide a word to search for vowels: ")
intersection = search4vowels(word)
print(intersection)