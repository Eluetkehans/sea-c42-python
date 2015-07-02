# Import random
import random

# Create empty dictionary for our trigrams
tridic = {}

# Get our text file
f = file.open("sherlock-small.txt", "r")

# Store the text in a variable
text = f.getlines()

# Split the text into individual words
text.split()


# Create dictionary of trigrams
def filldic(text):
    """Fills the trigram dictionary with trigrams"""
    for word in range(len(text) - 2):
        if(tridic[word, word + 1] in tridic):
            tridic[(word, word + 1)].append(word + 3)
        else:
            tridic[(word, word + 1)] = [word + 3]
