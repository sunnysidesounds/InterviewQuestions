#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    print(n)
    print(s)
    if len(s) <= 3:
        return 0

    has_valley = False
    valley_count = 0
    for i in range(0, n-1):
        if s[i] == 'D' and s[i+1] == 'D':
            has_valley = True

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