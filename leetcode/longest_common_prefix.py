"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


"""


import unittest


def longest_common_prefix(strings):

    if len(strings) == 0:
        return ""

    if len(strings) == 1 and strings[0] != "":
        return strings[0][0]

    final_prefix = ""
    for i in range(0, len(strings) - 1):
        current_prefix = ""
        for v1, v2 in zip(strings[i], strings[i + 1]):
            if v1 == v2:
                current_prefix += v1
            else:
                break

        if final_prefix == "" and i == 0:
            final_prefix = current_prefix
        else:
            if final_prefix != current_prefix:
                final_prefix = "".join([v1 for v1, v2 in zip(final_prefix, current_prefix) if v1 == v2])
            else:
                final_prefix = current_prefix

    return final_prefix







class TestLongestCommonPrefix(unittest.TestCase):

    def test_1(self):
        output = longest_common_prefix(["flower","flow","flight"])
        self.assertEqual(output, 'fl', 'Longest common prefix is: fl')

    def test_2(self):
        output = longest_common_prefix(["dog","racecar","car"])
        self.assertEqual(output, '', 'Longest common prefix is: NONE')

    def test_3(self):
        output = longest_common_prefix(["alexa","alexander","alexz"])
        self.assertEqual(output, 'alex', 'Longest common prefix is: alex')

    def test_4(self):
        output = longest_common_prefix(["dog","doom","dot", 'doth'])
        self.assertEqual(output, 'do', 'Longest common prefix is: do')

    def test_5(self):
        output = longest_common_prefix(["dog","doom","dot", 'di'])
        self.assertEqual(output, 'd', 'Longest common prefix is: d')

    def test_6(self):
        output = longest_common_prefix(["animal","ann","ani", 'di'])
        self.assertEqual(output, '', 'Longest common prefix is: NONE')

    def test_7(self):
        output = longest_common_prefix([])
        self.assertEqual(output, '', 'Longest common prefix is: NONE')

    def test_8(self):
        output = longest_common_prefix(['animal'])
        self.assertEqual(output, 'a', 'Longest common prefix is: NONE')

    def test_9(self):
        output = longest_common_prefix(["reflower","flow","flight"])
        self.assertEqual(output, '', 'Longest common prefix is: NONE')

if __name__ == '__main__':
    unittest.main()
