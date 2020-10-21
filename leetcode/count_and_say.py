

import unittest


"""
 1.     1
 2.     11
 3.     21
 4.     1211
 5.     111221
 6.     312211
 7.     13112221
 8.     1113213211
 9.     31131211131221
10.     13211311123113112211

set s := “1”
if n = 1, then return s
for i := 2 to n + 1
    j := 0, temp := “”, curr = “” and count := 0
    while j < length of s, do
        if curr is “”, then curr := s[j], count := 1 and increase j by 1
        else if curr is s[j], then increase count and j by 1
        otherwise temp := temp + count as string + curr, curr = “”, count := 0
    temp := temp + count as string + curr
return s


"""

def count_and_say_2(n):

    number = "1"
    if n == 1:
        return number

    for i in range(2, n + 1):
        j = 0
        tmp = ""
        current = ""
        count = 0
        while j < len(number):
            if current == "":
                current = number[j]
                count += 1
                j += 1
            elif current == number[j]:
                count += 1
                j += 1
            else:
                tmp += str(count) + current
                current = ""
                count = 0
        tmp += str(count) + current
        number = tmp

    return number













def count_and_say(n):

    str_number = "1"
    for i in range(n - 1):
        str_number = count_and_say_helper(str_number)
    return str_number


def count_and_say_helper(current):
    output = ""
    i = 0
    while i < len(current):
        count = 1
        while i + 1 < len(current) and current[i] == current[i + 1]:
            i += 1
            count += 1
        output += str(count) + current[i]
        i += 1

    return output



class TestCountAndSay(unittest.TestCase):

    def test_1(self):
        output = count_and_say(4)
        self.assertEqual(output, "1211", "Should be 1211")

    def test_22(self):
        output = count_and_say_2(4)
        self.assertEqual(output, "1211", "Should be 1211")


if __name__ == '__main__':
    unittest.main()



