
"""
Read two integers from STDIN and print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.

"""

def arithemtic(a, b):

    first_line = (a + b)
    second_line = (a - b)
    third_line = (a * b)

    print(first_line)
    print(second_line)
    print(third_line)

    return [first_line, second_line, third_line]






if __name__ == "__main__":

    tests = [
        {"paramters": [3, 2], "expected": [5, 1, 6]}
    ]

    counter = 1
    for test in tests:
        results = arithemtic(test['paramters'][0], test['paramters'][1])
        print("Test {0} n={1}".format(counter, test['paramters']), test['expected'] == results, results )

        counter += 1







