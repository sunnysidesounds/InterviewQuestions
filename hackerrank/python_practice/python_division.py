
"""
Task
Read two integers and print two lines. The first line should contain integer division,  a//b .
The second line should contain float division,  a/b .

You don't need to perform any rounding or formatting operations.

Input Format

The first line contains the first integer, . The second line contains the second integer, .

Output Format

Print the two lines as described above.

"""

def division(a, b):
    integer_division = a // b
    float_division = a / b

    print(integer_division)
    print(float_division)

    return [integer_division, float_division]

    pass









if __name__ == "__main__":

    tests = [
        {"paramters": [4, 3], "expected": [1, 1.33333333333]}
    ]

    counter = 1
    for test in tests:
        results = division(test['paramters'][0], test['paramters'][1])
        print("Test {0} n={1}".format(counter, test['paramters']), test['expected'] == results, results)

        counter += 1







