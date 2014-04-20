#!/usr/local/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys


def mimic_dict(filename):
    """Returns mimic dict mapping each word to list of words which follow it."""
    text_file = open(filename, 'rU')
    full_text = text_file.read().replace('\n', ' ')
    words_list = full_text.split()
    words_dict = {}
    words_dict[''] = words_list[:]

    for word in words_list:
        word_index = words_list.index(word)
        words_dict[word] = words_list[word_index+1:]

    return words_dict


def print_mimic(mimic_dict, word):
    """Given mimic dict and start word, prints 200 random words."""

    counter = 0
    col_number = 0
    new_word = word
    while counter < 200:
        list_from_word = mimic_dict[new_word]
        new_word = random.choice(list_from_word)
        col_number += len(new_word)
        print new_word,
        if abs(col_number - 70) < len(new_word):
            print
            col_number = 0
        counter += 1


# Provided main(), calls mimic_dict() and mimic()
def main():
    """This is the main function"""

    if len(sys.argv) != 2:
        print 'usage: ./mimic.py file-to-read'
        sys.exit(1)

    the_dict = mimic_dict(sys.argv[1])
    print_mimic(the_dict, '')


if __name__ == '__main__':
    main()
