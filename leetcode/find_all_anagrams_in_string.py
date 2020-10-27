"""

    Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

    Strings consists of lowercase English letters only and the length of both strings s and p will
    not be larger than 20,100.

    The order of output does not matter.

    Example 1:

    Input:
    s: "cbaebabacd" p: "abc"

    Output:
    [0, 6]

    Explanation:
    The substring with start index = 0 is "cba", which is an anagram of "abc".
    The substring with start index = 6 is "bac", which is an anagram of "abc".
    Example 2:

    Input:
    s: "abab" p: "ab"

    Output:
    [0, 1, 2]

    Explanation:
    The substring with start index = 0 is "ab", which is an anagram of "ab".
    The substring with start index = 1 is "ba", which is an anagram of "ab".
    The substring with start index = 2 is "ab", which is an anagram of "ab".
"""


import unittest





def find_all_anagram_indexes(s, p):

    p_sorted = "".join(sorted(p))
    results = []
    for i in range(0, len(s) - len(p) + 1):
        char_set = "".join(sorted(s[i:i+len(p)]))
        if p_sorted == char_set:
            results.append(i)

    return results





class TestFinaAllAnagramIndexes(unittest.TestCase):

    def test_1(self):
        output = find_all_anagram_indexes("cbaebabacd", "abc")
        self.assertEqual(output, [0, 6])

    def test_2(self):
        output = find_all_anagram_indexes("abab", "ab")
        self.assertEqual(output, [0, 1, 2])


if __name__ == '__main__':
    unittest.main()
