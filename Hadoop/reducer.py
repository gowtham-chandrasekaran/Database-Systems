#!/usr/bin/python

import sys

count = 0

word2count = {} # Dictionary to store word as key and count as value

# Iterating through each line
for line in sys.stdin:

    line = line.strip() # Remove spaces from left and right

    word, count = line.split('\t', 1) # Split word and count from input file

    try:
        count = int(count) # Convert into integer
    except ValueError:

        continue

    if word in word2count: # If word available in dictionary
        word2count[word] += count # Add count to the existing count
    else:
        word2count[word] = count # else add a fresh count by adding the word to the dictionary

# Iterate through the dictionary
for word in word2count.keys():
    # Display each word with its count
    print("{}\t{}".format(word,word2count[word]))