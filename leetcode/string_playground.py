
import unittest


def length_of_longest_substring( s: str):
    last_seen_characters = {}
    longest_substr = [0, 1]
    start_index = 0

    for index, character in enumerate(s):
        if character in last_seen_characters:
            start_index = max(start_index, last_seen_characters[character] + 1)  # + 1 because I've seen it already
        if (longest_substr[1] - longest_substr[0]) < (index + 1 - start_index):
            longest_substr = [start_index, index + 1]
        last_seen_characters[character] = index
    return s[longest_substr[0]: longest_substr[1]]


def is_palindrome(s: str):
    s = "".join(i.lower() for i in s if i.isalnum())

    left = 0
    right = len(s) - 1

    while left < right:
        left_char = s[left]
        right_char = s[right]
        if left_char != right_char:
            return False
        left += 1
        right -= 1

    return True

def min_window(s, t):
    pass




class TestStringPlayground(unittest.TestCase):

    def test_min_window(self):
        output = min_window("ADOBECODEBANC", "ABC")
        self.assertEqual(output, 'BANC', 'Should equal BANC')

    #def test_is_palindrome_1(self):
    #    output = is_palindrome("A man, a plan, a canal: Panama")
    #    self.assertEqual(output, True, 'Should equal True')

    #def test_is_palindrome_2(self):
    #    output = is_palindrome("race a car")
    #    self.assertEqual(output, False, 'Should equal False')

    #def test_is_palindrome_3(self):
    #    output = is_palindrome("0P")
    #    self.assertEqual(output, False, 'Should equal False')


   #def test_length_of_longest_substring_1(self):
   #    output = length_of_longest_substring('abcabcbb')
   #    self.assertEqual(output, 'abc', 'Should equal abc')

   #def test_length_of_longest_substring_2(self):
   #    output = length_of_longest_substring('bbbb')
   #    self.assertEqual(output, 'b', 'Should equal b')

   #def test_length_of_longest_substring_3(self):
   #    output = length_of_longest_substring('pwwkew')
   #    self.assertEqual(output, 'wke', 'Should equal wke')

   #def test_length_of_longest_substring_4(self):
   #    output = length_of_longest_substring('')
   #    self.assertEqual(output, '', 'Should equal nothing')

   #def test_length_of_longest_substring_5(self):
   #    output = length_of_longest_substring('tmmzuxt')
   #    self.assertEqual(output, 'mzuxt', 'Should equal nothing')


if __name__ == '__main__':
    unittest.main()