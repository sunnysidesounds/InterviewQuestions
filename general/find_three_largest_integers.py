







def findThreeLargestNumbers(array):
    array.sort()
    return array[len(array)-3:]

if __name__ == '__main__':

    results = findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7])
    print(results)