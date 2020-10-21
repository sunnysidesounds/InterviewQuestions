"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


"""

import unittest


def str_str(haystack, needle):
    if needle == "":
        return 0

    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            sub_haystack = haystack[i: len(needle) + i]
            if sub_haystack == needle:
                return i

    return -1


class TestStrStr(unittest.TestCase):

    def test_1(self):
        output = str_str("hello", 'll')
        self.assertEqual(output, 2, 'Should return an index of 2')

    def test_2(self):
        output = str_str("aaaaa", 'bba')
        self.assertEqual(output, -1, 'Should return an index of -1')

    def test_3(self):
        output = str_str("", "")
        self.assertEqual(output, 0, 'Should return an index of 0')

    def test_4(self):
        output = str_str("jasonalexander", 'alex')
        self.assertEqual(output, 5, 'Should return an index of 5')

    def test_5(self):
        output = str_str("a", "")
        self.assertEqual(output, 0, 'Should return an index of -1')

if __name__ == '__main__':
    unittest.main()
