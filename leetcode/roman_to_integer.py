"""
I - 1
V - 5
X - 10
L - 50
C - 100
D - 500
M - 1000

Rules:
* If I comes before V or X, subtract 1 eg: IV = 4 and IX = 9
* If X comes before L or C, subtract 10 eg: XL = 40 and XC = 90
* If C comes before D or M, subtract 100 eg: CD = 400 and CM = 900

M CM XC IV

M = 1000, CM = 900, XC = 90 and IV = 4.

"""


import unittest





def roman_to_integer(roman):

    numerials = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    number_list = []
    i = 0
    while i <= len(roman) - 1:
        if i < len(roman) - 1:
            if roman[i] == 'I' and roman[i + 1] == 'V' or roman[i] == 'I' and roman[i + 1] == 'X':
                number = abs(numerials[roman[i]] - numerials[roman[i + 1]])
                i += 1
            elif roman[i] == 'X' and roman[i + 1] == 'L' or roman[i] == 'X' and roman[i + 1] == 'C':
                number = abs(numerials[roman[i]] - numerials[roman[i + 1]])
                i += 1
            elif roman[i] == 'C' and roman[i + 1] == 'D' or roman[i] == 'C' and roman[i + 1] == 'M':
                number = abs(numerials[roman[i]] - numerials[roman[i + 1]])
                i += 1
            else:
                number = numerials[roman[i]]
        else:
            number = numerials[roman[i]]

        number_list.append(number)

        i += 1

    return sum(number_list)







class TestRomanToInteger(unittest.TestCase):

    def test_1(self):
        output = roman_to_integer('III')
        self.assertEqual(output, 3)

    def test_2(self):
        output = roman_to_integer('MCMXCIV')
        self.assertEqual(output, 1994)

    def test_3(self):
        output = roman_to_integer('IV')
        self.assertEqual(output, 4)

    def test_4(self):
        output = roman_to_integer('MMMDCCXXIV')
        self.assertEqual(output, 3724)

    def test_5(self):
        output = roman_to_integer('LVIII')
        self.assertEqual(output, 58)

    def test_6(self):
        output = roman_to_integer('IX')
        self.assertEqual(output, 9)


if __name__ == '__main__':

    unittest.main()
