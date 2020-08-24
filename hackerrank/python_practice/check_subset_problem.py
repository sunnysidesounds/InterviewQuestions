
def check_subset(a, b):

    A = a
    B = b
    print (A.difference(B))
    print (B.difference(A))

    return None




if __name__ == "__main__":

    tests = [
        {"paramters": [set([1, 2, 3, 5, 6]), set([9, 8, 5, 6, 3, 2, 1, 4, 7])], "expected": True},
    ]

    counter = 1
    for test in tests:
        results = check_subset(test['paramters'][0], test['paramters'][1])
        print("Test {0} n={1}".format(counter, test['paramters']), test['expected'] == results, results )

        counter += 1
    
    