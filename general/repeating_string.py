#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):

    if len(s) == 1 and s == 'a':
        return n

    char_list = [char for char in s]
    length = len(char_list) - 1
    index = 0
    a_count = 0
    for i in range(n):
        if char_list[index] == 'a':
            a_count += 1



        print("{0} - {1} - {2} ".format(i, index, char_list[index]))


        if index == length:
            index = 0
        else:
            index += 1

    return a_count


s, n = input().strip(), int(input().strip())
print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))









if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = 'kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm'

    n = 736778906400

    result = repeatedString(s, n)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()


