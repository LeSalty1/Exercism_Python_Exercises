# Takes a string and outputs its acronym with the convention that hyphenated words (e.g., metal-oxide) count as two separte words. 
import string

def abbreviate(words):
    acronym = ""
    for word in words.split(): 
        if word[0] in string.punctuation:
            if len(word) == 1: 
                continue
            acronym += word[1].upper # Handles words that are emphasized with punctuation (e.g., _not_). 
        else: 
            if "-" in word: # Handles the hyphenated case. 
                acronym += word[0].upper() + word[word.index("-") + 1].upper()
            else: 
                acronym += word[0].upper()
    return acronym
