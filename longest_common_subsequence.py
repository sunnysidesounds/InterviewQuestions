"""

Implement a function that returns the longest subsequence common to two given strings.
A subsequence is defined as a group of characters that appear sequentially, with no importance given to their
actual position in a string. In other words, characters do not need to appear consecutively in order to form a
subsequence. Assume that there will only be one longest common subsequence.

Sample input: "ZXVVYZW", "XKYKZPW"

Sample output: ["X", "Y", "Z", "W"]

- dynamic programming

"""

def longest_common_subsequence(str1, str2):

    pass



if __name__ == '__main__':

    str1 = 'ZXVVYZW'
    str2 = 'XKYKZPW'
    results = longest_common_subsequence(str1, str2)
    print(results)

