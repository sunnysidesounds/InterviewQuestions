#!/bin/python3

"""
def perform_bubble_sort(blist):
    cmpcount, swapcount = 0, 0
    for j in range(len(blist)):
        for i in range(1, len(blist)-j):
            cmpcount += 1
            if blist[i-1] > blist[i]:
                swapcount += 1
                blist[i-1], blist[i] = blist[i], blist[i-1]
    return cmpcount, swapcount
"""

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swap_count = 0
    for j in range(len(arr) - 1):
        for i in range(1, len(arr) - 1):
            if arr[i - 1] > arr[i]:
                swap_count += 1
                arr[i-1], arr[i] = arr[i], arr[i-1]
    return swap_count

def minimumSwaps2(arr):
    maximum = arr[0]
    count = 0
    for i in range(1, len(arr)):
        if arr[i] > maximum:
            count += 1
            maximum = arr[i]

    print(count)
    return maximum


def minimumSwaps3(arr):
    temp = [0] * (len(arr) + 1)
    for pos, val in enumerate(arr):
        temp[val] = pos
        pos += 1
    swaps = 0
    for i in range(len(arr)):
        if arr[i] != i+1:
            swaps += 1
            t = arr[i]
            arr[i] = i+1
            arr[temp[i+1]] = t
            temp[t] = temp[i+1]
    return swaps


if __name__ == '__main__':


    arr = [ 3, 7, 6, 9, 1, 8, 10, 4, 2, 5 ]
    res = minimumSwaps3(arr)
    print(res)



