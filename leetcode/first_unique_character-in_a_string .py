
import unittest


def first_unique_character_in_a_string(word):

    words = {}
    for character in word:
        if character not in words:
            words[character] = 1
        else:
            words[character] += 1

    for i in range(len(word)):
        character = word[i]
        if character in words and words[character] == 1:
            return i

    return -1


class TestFirstUniqueCharacter(unittest.TestCase):

    def test_1(self):
        output = first_unique_character_in_a_string("loveleetcode")
        self.assertEqual(output, 2, 'Should equal to index 2')

    def test_2(self):
        output = first_unique_character_in_a_string("leetcode")
        self.assertEqual(output, 0, 'Should equal to index 0')

    def test_3(self):
        output = first_unique_character_in_a_string("")
        self.assertEqual(output, -1, 'Should equal to index -1')

    def test_4(self):
        output = first_unique_character_in_a_string("lleettccoo")
        self.assertEqual(output, -1, 'Should equal to index -1')

    def test_5(self):
        output = first_unique_character_in_a_string("jjaassoonz")
        self.assertEqual(output, 8, 'Should equal to index 8')


if __name__ == '__main__':
    unittest.main()




