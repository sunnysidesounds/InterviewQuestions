"""

Alice is taking a cryptography class and finding anagrams to be very useful.
We consider two strings to be anagrams of each other if the first string's letters
can be rearranged to form the second string. In other words, both strings must
contain the same exact letters in the same exact frequency For example, bacdc
and dcbac are anagrams, but bacdc and dcbad are not.

Alice decides on an encryption scheme involving two large strings where encryption
is dependent on the minimum number of character deletions required to make the two
strings anagrams. Can you help her find this number?

Given two strings,  and , that may or may not be of the same length, determine the
minimum number of character deletions required to make  and  anagrams. Any characters
can be deleted from either of the strings.

For example, if  and , we can delete  from string  and  from string  so that both
remaining strings are  and  which are anagrams.

Function Description

Complete the makeAnagram function in the editor below. It must return an integer
representing the minimum total characters that must be deleted to make the strings anagrams.

makeAnagram has the following parameter(s):

a: a string
b: a string
Input Format

The first line contains a single string, .
The second line contains a single string, .

Constraints

The strings  and  consist of lowercase English alphabetic letters ascii[a-z].
Output Format

Print a single integer denoting the number of characters you must delete to make the two strings anagrams of each other.

Sample Input

cde
abc
Sample Output

4
Explanation

We delete the following characters from our two strings to turn them into anagrams of each other:

Remove d and e from cde to get c.
Remove a and b from abc to get c.
We must delete  characters to make both strings anagrams, so we print  on a new line.



{'f': 1,
'c': 2,
'r': 1,
'x': 2,
'z': 1,
'w': 1,
's': 1,
'a': 1,
'n': 1,
'm': 2,
'l': 1,
'i': 1,
'g': 1,
'y': 3,
'v': 1}



{'j': 2,
'x': 1,
'w': 2,
't': 1,
'r': 2,
'h': 2,
'v': 1,
'u': 1,
'l': 1,
'm': 3,
'p': 2,
'd': 1,
'o': 2,
'q': 1,
'b': 2,
'i': 1,
's': 1,
'g': 1,
'e': 2,
'k': 1}



"""


def make_anagram(a, b):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    for i in range(len(alphabet)):
        letter = alphabet[i]
        count_a = a.count(letter)
        count_b = b.count(letter)
        count += abs(count_a - count_b)
    return count
























if __name__ == '__main__':

    tests = [#{"a": "cde", "b": "abc", "expected": 4},
             {"a": "fcrxzwscanmligyxyvym", "b": "jxwtrhvujlmrpdoqbisbwhmgpmeoke", "expected": 30}
             ]

    counter = 1
    for test in tests:
        results = make_anagram(test['a'], test['b'])
        print(results)

        counter += 1

