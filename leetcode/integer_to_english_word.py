# Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
#
# Example 1:
#
# Input: 123
# Output: "One Hundred Twenty Three"
# Example 2:
#
# Input: 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# Example 3:
#
# Input: 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# Example 4:
#
# Input: 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
#
# Hide Hint #1
# Did you see a pattern in dividing the number into chunk of words? For example, 123 and 123000.
# Hide Hint #2
# Group the number by thousands (3 digits). You can write a helper function that takes a number less than
# 1000 and convert just that chunk to words.
# Hide Hint #3
# There are many edge cases. What are some good test cases? Does your code work with input such as 0? Or
# 1000010? (middle chunk is zero and should not be printed out)

# 123 = hundred
#
# thousand - hundred - ones
#
# million - hundred - thousand - hundred
#
# billion - hundred - million - hundred - thousand - hundred
#
#

#
#
# [2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
# [2, 1, 1,
# 2, 3, 4,
# 5, 6, 7,
# 8, 9, 1]

#
#
# - backwards
# 1 = ones = one						- one
# 9 = tens = ninety					- ninety
# 8 = hundred (ones + "hundred") = eight hundred		- eight hundred
#
# 7 = thousands (ones + "thousand") seven thousand
# 6 = thousands (tens) sixty				- sixty seven thousand
# if middle digit > 1: use tens else: use teens
# 5 = hundred (ones + "hundred") five hundred		- five hundred
#
# 4 = million (ones + "million") four million
# 3 = million (tens) thirty				- thirty four million
# if middle digit > 1: use tens else: use teens
#
# 2 = hundred (ones + "hundred") two hundred		- two hundred
#
# 1 = billion (ones + "billion")
# 1 = billion (tens)					- eleven billion
# if middle digit > 1: use tens else: use teens
#
# 2 = hundred (ones + "hundred")				- two hundred
# ones = [one, two, three, four, five, size, seven, eight, nine, ten]
# teens = [eleven, twevle, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen]
# tens = [twenty, thirty, fourty, fifty, sixty, seventy, eighty, ninety]
#
# hundred, thousand, million, billion

import unittest

def integer_to_word_helper(number_tuple, section):
    ones = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten'}
    teens = {1: 'Eleven', 2: 'Twelve', 3: 'Thirteen', 4: 'Fourteen', 5: 'Fifteen', 6: 'Sixteen', 7: 'Seventeen', 8: 'Eighteen', 9: 'Nineteen'}
    tens = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}
    bigger = {100: 'Hundred', 1000: 'Thousand', 1000000: 'Million', 100000000000: 'Billion'}

    digit_substr_1 = ""
    digit_substr_2 = ""
    digit_substr_3 = ""

    if section == 1:

        if len(number_tuple) == 3:
            if number_tuple[0] == 0 and number_tuple[1] == 0 and number_tuple[2] == 0:
                digit_substr_1 = bigger[100] + " " + bigger[1000]
            elif number_tuple[1] == 0 and number_tuple[2] == 0:
                digit_substr_1 = ones[number_tuple[0]] + " " + bigger[100]
            elif number_tuple[1] == 0:
                digit_substr_1 = tens[number_tuple[0]]
            else:
                if number_tuple[0] == 0:
                    digit_substr_1 = " " + bigger[100] + " " + bigger[1000]
                else:
                    digit_substr_1 = ones[number_tuple[0]] + " " + bigger[100]

                if number_tuple[1] == 1:
                    digit_substr_2 = teens[number_tuple[2]]
                else:
                    digit_substr_2 = tens[number_tuple[1]]
                    digit_substr_3 = ones[number_tuple[2]]
        elif len(number_tuple) == 2:
            if number_tuple[1] == 0:
                digit_substr_1 = tens[number_tuple[0]]
            else:
                digit_substr_1 = teens[number_tuple[1]]
        else:
            digit_substr_1 = ones[number_tuple[0]]

    elif section == 2:

        if len(number_tuple) == 3:
            if number_tuple[1] == 0 and number_tuple[2] == 0:
                if number_tuple[0] == 1:
                    digit_substr_1 = ones[number_tuple[0]]
                else:
                    digit_substr_1 = ones[number_tuple[0]] + " " + bigger[1000]
            elif number_tuple[1] == 0:
                digit_substr_1 = tens[number_tuple[0]]
            else:
                digit_substr_1 = ones[number_tuple[0]] + " " + bigger[100]
                digit_substr_2 = tens[number_tuple[1]]
                digit_substr_3 = ones[number_tuple[2]] + " " + bigger[1000]
        elif len(number_tuple) == 2:
            digit_substr_1 = teens[number_tuple[1]] + " " + bigger[1000]

    elif section == 3:

        digit_substr_1 = ones[number_tuple[0]] + " " + bigger[100]
        digit_substr_2 = tens[number_tuple[1]]
        digit_substr_3 = ones[number_tuple[2]] + " " + bigger[1000000]

    elif section == 4:
        digit_substr_1 = ones[number_tuple[0]] + " " + bigger[100]
        digit_substr_2 = tens[number_tuple[1]]
        digit_substr_3 = ones[number_tuple[2]] + " " + bigger[100000000000]

    return " ".join((digit_substr_1, digit_substr_2, digit_substr_3))


def groups_of_three(l):
    start = 0
    for end in range(len(l)%3, len(l)+1, 3):
        yield l[start:end]
        start = end


def convert_integer_to_english_word(number):

    group_by_digits = list(groups_of_three([int(i) for i in str(number)]))
    section = 1
    string_output = ""
    for i in range(len(group_by_digits)-1, -1, -1):
        group = group_by_digits[i]

        if len(group) > 0:
            string_value = integer_to_word_helper(group, section).strip()
            string_output = string_value + " " + string_output

        section += 1

    return string_output.strip()



class TestIntegerToEnglishWord(unittest.TestCase):
     def test_1(self):
         output_value = convert_integer_to_english_word(123)
         expected_value = "One Hundred Twenty Three"
         self.assertEqual(output_value, expected_value, 'Should equal {0}'.format(expected_value))

     def test_2(self):
         output_value = convert_integer_to_english_word(12345)
         expected_value = "Twelve Thousand Three Hundred Forty Five"
         self.assertEqual(output_value, expected_value, 'Should equal {0}'.format(expected_value))

     def test_3(self):
         output_value = convert_integer_to_english_word(11)
         expected_value = "Eleven"
         self.assertEqual(output_value, expected_value, 'Should equal {0}'.format(expected_value))

     def test_4(self):
         output_value = convert_integer_to_english_word(15)
         expected_value = "Fifteen"
         self.assertEqual(output_value, expected_value, 'Should equal {0}'.format(expected_value))

     def test_5(self):
         output_value = convert_integer_to_english_word(20)
         expected_value = "Twenty"
         self.assertEqual(output_value, expected_value, 'Should equal {0}'.format(expected_value))

     def test_6(self):
         output_value = convert_integer_to_english_word(100)
         expected_value = "One Hundred"
         self.assertEqual(output_value, expected_value, 'Should equal {0}'.format(expected_value))

     def test_7(self):
         output_value = convert_integer_to_english_word(111)
         expected_value = "One Hundred Eleven"
         self.assertEqual(output_value, expected_value, 'Should equal {0}'.format(expected_value))

     def test_8(self):
        output_value = convert_integer_to_english_word(115)
        expected_value = "One Hundred Fifteen"
        self.assertEqual(output_value, expected_value, 'Should equal {0}'.format(expected_value))

     def test_9(self):
         output_value = convert_integer_to_english_word(1)
         expected_value = "One"
         self.assertEqual(output_value, expected_value, 'Should equal {0}'.format(expected_value))

     def test_10(self):
         output_value = convert_integer_to_english_word(100000)
         expected_value = "One Hundred Thousand"
         self.assertEqual(output_value, expected_value, 'Should equal {0}'.format(expected_value))

     def test_11(self):
         output_value = convert_integer_to_english_word(100011)
         expected_value = "One Hundred Thousand Eleven"
         self.assertEqual(output_value, expected_value, 'Should equal {0}'.format(expected_value))

     def test_12(self):
         output_value = convert_integer_to_english_word(100015)
         expected_value = "One Hundred Thousand Fifteen"
         self.assertEqual(output_value, expected_value, 'Should equal {0}'.format(expected_value))

     def test_13(self):
         output_value = convert_integer_to_english_word(100115)
         expected_value = "One Hundred Thousand One Hundred Fifteen"
         self.assertEqual(output_value, expected_value, 'Should equal {0}'.format(expected_value))


if __name__ == '__main__':
    unittest.main()
