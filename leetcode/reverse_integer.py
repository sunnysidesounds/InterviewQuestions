import unittest

def reverse_integer(x):
    is_negative = False
    reversed_int = 0
    x = abs(x)

    if x < 0:
        is_negative = True
        x *= -1  # make the negative number positive by multipling by -1


    while x > 0:
        reversed_int = reversed_int * 10 + (x % 10)  # This accounts the 1's, 10's 100's place
        x /= 10

    if reversed_int > 1 << 31: # if we have overflow, return 0
        return 0

    if is_negative:
        reversed_int *= -1

    return reversed_int


class TestReverseInteger(unittest.TestCase):

    def test_1(self):
        output = reverse_integer(123)
        self.assertEqual(output, 321, 'Should be reversed')

    def test_2(self):
        output = reverse_integer(-123)
        self.assertEqual(output, -321, 'Should be reversed')

    def test_3(self):
        output = reverse_integer(1534236469)
        self.assertEqual(output, 0, 'Should be reversed')



if __name__ == '__main__':
    unittest.main()
