
"""
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird


"""

def so_weird(n):
    text = None
    if n % 2 != 0:
        text = "Weird"
    else:
        if n in range(2, 5):
            text = "Not Weird"
        elif n in range(6, 20):
            text = "Weird"
        elif n > 20:
            text = "Not Weird"
    return text









if __name__ == "__main__":

    tests = [
        {"n": 3, "expected": "Weird"},
        {"n": 2, "expected": "Not Weird"},
        {"n": 4, "expected": "Not Weird"},
        {"n": 18, "expected": "Weird"}


    ]

    counter = 1
    for test in tests:
        results = so_weird(test['n'])
        print("Test {0} n={1}".format(counter, test['n']), test['expected'] == results, results )

        counter += 1







