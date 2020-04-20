#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    note_dict = {}
    mag_dict = {}
    for word in note.split(" "):
        if word in note_dict:
            note_dict[word] =  note_dict[word] + 1
        else:
            note_dict[word] = 1

    for mword in magazine.split(" "):
        if mword in note_dict:
            if mword in mag_dict:
                mag_dict[mword] += 1
            else:
                mag_dict[mword] = 1

    print("note: {0}".format(note_dict))
    print("mag: {0}".format(mag_dict))

    if note_dict == mag_dict:
        return 'Yes'

    is_yes = 'No'
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