#!/bin/python3

import math
import os
import random
import re
import sys

"""
Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through 
his handwriting. He found a magazine and wants to know if he can cut out whole words from it and use them 
to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must 
use only whole words available in the magazine. He cannot use substrings or concatenation to create the 
words he needs.

Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom 
note exactly using whole words from the magazine; otherwise, print No.

For example, the note is "Attack at dawn". The magazine contains only "attack at dawn". The magazine has 
all the right words, but there's a case mismatch. The answer is .

Function Description

Complete the checkMagazine function in the editor below. It must print  if the note can be formed using 
the magazine, or .

checkMagazine has the following parameters:

magazine: an array of strings, each a word in the magazine
note: an array of strings, each a word in the ransom note

"""

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    note_dict = {}
    mag_dict = {}
    # Split the words into a list from the ransom note, counting these words in the note
    for word in note.split(" "):
        if word in note_dict:
            note_dict[word] =  note_dict[word] + 1
        else:
            note_dict[word] = 1

    # Split the words into a list from the magazine, also counting the words in the magazine
    for mword in magazine.split(" "):
        if mword in note_dict:
            if mword in mag_dict:
                mag_dict[mword] += 1
            else:
                mag_dict[mword] = 1

    print("note: {0}".format(note_dict))
    print("mag: {0}".format(mag_dict))

    # If both dicts match, then yes we can construct a ransom note from the magazine words.
    if note_dict == mag_dict:
        return 'Yes'

    is_yes = 'No'
    # Otherwise we iterate over both dictionaries compaing value counts with each other.
    for (note_key, note_value), (mag_key, mag_value) in zip(note_dict.items(), mag_dict.items()):
        if mag_value >= note_value:
            is_yes = 'Yes'
            continue
        else:
            is_yes = 'No'

    return is_yes




if __name__ == '__main__':
    #mn = input().split()

    #m = int(mn[0])

    #n = int(mn[1])

    #magazine = 'h ghq g xxy wdnr anjst xxy wdnr h h anjst wdnr'
    #magazine = 'give me one grand today night'

    #note = 'h ghq'
    #note = 'give one grand today'

    result = checkMagazine(magazine, note)
    print(result)