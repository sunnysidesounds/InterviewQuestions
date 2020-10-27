"""
        if x >= 2**31-1 or x <= -2**31: return 0
        else:
            strg = str(x)
            if x >= 0 :
                revst = strg[::-1]
            else:
                temp = strg[1:]
                temp2 = temp[::-1]
                revst = "-" + temp2
            if int(revst) >= 2**31-1 or int(revst) <= -2**31: return 0
            else: return int(revst)
"""


import unittest


def reverse_integer(x):

    if x >= 2**31-1 or x <= -2**21:
        return 0
    else:
        string_integer = str(x)
        if x >= 0:
            rev = string_integer[::-1]
        else:
            temp = string_integer[1:]
            temp2 = temp[::-1]
            rev = "-" + temp2
        if int(rev) >= 2**31-1 or int(rev) <= -2**31:
            return 0
        else:
            return int(rev)



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
