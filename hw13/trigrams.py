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
    for word in range(len(words) - 2):
        if(tridic[words[word], words[word + 1]] in tridic):
            tridic[(words[word], words[word + 1])].append(words[word + 3])
        else:
            tridic[(words[word], words[word + 1])] = [words[word + 3]]


filldic(words)
print(tridic)
