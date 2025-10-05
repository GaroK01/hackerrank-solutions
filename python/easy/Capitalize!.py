#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    # Split the string into a list with spaces
    words = s.split(" ")
    capitalized_words = []
    # Loop over the list and capitalize each word
    for word in words:
      capitalized_words.append(word.capitalize())
    # Join the capitalized words back into a string with spaces
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
