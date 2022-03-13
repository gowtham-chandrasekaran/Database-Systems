#!/usr/bin/python

import sys

# Iterating through each line
for line in sys.stdin:

    line = line.strip() # Stripping extra space from left and right

    words = line.split() # Split each word of line by spaces and store in a list

    # Iterate through each word in words
    for word in words:
        # Print each word along with number 1 with a tab space in between
        print('{}\t1'.format(word))