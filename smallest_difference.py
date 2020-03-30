"""

Write a function that takes in two non-empty arrays of integers.
The function should find the pair of numbers (one from the first array, one from the second array)
whose absolute difference is closest to zero. The function should return an array containing these
two numbers, with the number from the first array in the first position. Assume that there will
only be one pair of numbers with the smallest difference.

Input: [-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]
Output: [28, 26]

"""


def smallest_difference(array_one, array_two):

    array_one.sort()
    array_two.sort()

    index_one = 0
    index_two = 0
    abs_map = {}
    closet_to_zero = None
    while index_one < len(array_one) and index_two < len(array_two):
        abs_value = abs(array_one[index_one] - array_two[index_two])
        if closet_to_zero is None:
            closet_to_zero = abs_value
        if closet_to_zero and abs_value < closet_to_zero:
            closet_to_zero = abs_value
            abs_map[closet_to_zero] = [array_one[index_one], array_two[index_two]]

        if array_one[index_one] < array_two[index_two]:
            index_one += 1
        else:
            index_two += 1

    print(closet_to_zero, abs_map)
    return abs_map[closet_to_zero]








if __name__ == '__main__':
    #arr1 = [-1, 5, 10, 20, 28, 3]
    #arr2 = [26, 134, 135, 15, 17]

    arr1 = [-1, 5, 10, 20, 3]
    arr2 = [26, 134, 135, 15, 17]

    # [-1, 5, 10, 20, 3], [26, 134, 135, 15, 17]), [20, 17]

    results = smallest_difference(arr1, arr2)
    print(results)