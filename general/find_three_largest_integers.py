



def third_max(nums):

    if len(nums) < 3:
        return max(nums)
    else:
        results = list(set(sorted(nums)))
        return results[len(results) - 3]





def findThreeLargestNumbers(array):

    array.sort()
    return array[len(array)-3:]

if __name__ == '__main__':

    #results = findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7])
    #print(results)

    results = third_max([2 ,2, 3, 1])
    print(results)