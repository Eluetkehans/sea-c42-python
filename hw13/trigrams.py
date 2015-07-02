# Import random
import random

# Create empty dictionary for our trigrams
tridic = {}

# Get our text file
f = open("sherlock-small.txt", "r")

# Store the text in a variable
text = f.readlines()

# Close the file, we have what we need
f.close()

# Get the text into a single string
single_line = " ".join(text)

# Take out the white space
words = single_line.split()


# Create dictionary of trigrams
def filldic(words):
    """Fills the trigram dictionary with trigrams"""
    # Loops as long as there are more the two words left.
    key = tuple()
    for i in range(len(words) - 2):
        key = tuple(words[i:i + 2])
        third = words[i + 2]
        tridic.setdefault(key, []).append(third)


def build_story(dict):
    """Returns a brand new story generated from the input"""
    for i in range(100):
        
filldic(words)
print(tridic)
