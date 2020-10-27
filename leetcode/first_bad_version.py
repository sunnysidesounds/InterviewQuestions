
import unittest

def isBadVersion(version):
    return False

def first_bad_version(n):
    start = 1
    end = n
    middle = 0
    position = 0

    while start <= end:

        middle = (end - start) // 2
        version = isBadVersion(middle)
        if version:
            position = middle
            end = middle - 1
        else:
            start = middle + 1

    return position




    pass


class TesFirstBadVersion(unittest.TestCase):

    def test_1(self):
        output = first_bad_version(5)
        self.assertEqual(output, 4)



if __name__ == '__main__':
    unittest.main()