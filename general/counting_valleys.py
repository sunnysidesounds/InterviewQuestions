#!/bin/python3

import math
import os
import random
import re
import sys

"""
Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography. 
During his last hike he took exactly  steps. For every step he took, he noted if it was an uphill, , 
or a downhill,  step. Gary's hikes start and end at sea level and each step up or down represents a  
unit change in altitude. We define the following terms:

A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending 
with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending 
with a step up to sea level.
Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked 
through.

For example, if Gary's path is , he first enters a valley  units deep. Then he climbs out an up onto a mountain  
units high. Finally, he returns to sea level and ends his hike.

Function Description

Complete the countingValleys function in the editor below. It must return an integer that denotes the number 
of valleys Gary traversed.

countingValleys has the following parameter(s):

n: the number of steps Gary takes
s: a string describing his path
"""

# Complete the countingValleys function below.
def countingValleys(n, s):
    print(n)
    print(s)
    if len(s) <= 3:
        return 0

    has_valley = False
    valley_count = 0
    # Iterate over the number of steps Gary took by two's ( i & i + 1)
    for i in range(0, n-1):
        # If the string has two DD in a string, set the has_valley flag to true as we found a value.
        if s[i] == 'D' and s[i+1] == 'D':
            has_valley = True

        # If the has_valley is True and the string has two UU's, Count the valley and flip has_valley back to False
        # To start over
        if has_valley and s[i] == 'U' and s[i+1] == 'U':
            valley_count += 1
            has_valley = False

    return valley_count


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(10)

    s = 'DUDDDUUDUU'

    result = countingValleys(n, s)

    print(result)