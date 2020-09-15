

# How do you find the missing number in a given integer array of 1 to 100?
# Formula: (n + 1) * (n + 2) / 2 (n being length of array
def find_missing_number_in_array(array):
    n = len(array)
    total_needs = (n + 1) * (n + 2) // 2
    total_is = sum(array)
    return total_needs - total_is


# How do you find the duplicate number on a given integer array?
def find_duplicate_number_in_array(array):
    original_length = len(array)
    new_length = len(list(set(array)))
    return True if new_length != original_length else False


# How do you find the largest and smallest number in an unsorted integer array?
def find_largest_and_smallest_numbers(array):
    return max(array), min(array)


# How do you find all pairs of an integer array whose sum is equal to a given number?
def find_all_sum_pairs_in_array(array, sum):
    array = sorted(array)
    low = 0
    high = len(array) - 1
    pairs = []

    while low < high:
        sub_sum = array[low] + array[high]
        if sub_sum == sum:
            pairs.append((array[low], array[high]))
        if sub_sum > sum:
            high -= 1
        else:
            low += 1

    return pairs


# How do you find duplicate numbers in an array if it contains multiple duplicates?
def find_multiple_duplicate_numbers_in_array(array):
    dups_arr = []
    dups_dict = {}
    for a in array:
        if a in dups_dict:
            dups_dict[a] += 1
            if dups_dict[a] == 2:
                dups_arr.append(dups_dict[a])
        else:
            dups_dict[a] = 1
    return dups_arr


# How to remove duplicates from a given array?
def remove_duplicates_from_array(array):
    counter_dict = []
    for i in range(len(array)):
        if i <= len(array):
            if array[i] not in counter_dict:
                counter_dict.append(array[i])
            else:
                del array[i]

    return array


# How do you search a target value in a rotated array?
def find_target_in_rotated_array(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left + right) // 2
        if target == array[middle]:
            return middle
        # check if left to mid is sorted
        if array[left] <= array[middle]:
            if target > array[middle] or target < array[left]:
                left = middle + 1
            else:
                right = middle - 1

        # check if mid to right is sorted
        else:
            if target < array[middle] or target > array[right]:
                right = middle - 1
            else:
                left = middle + 1

    return -1


# Given an unsorted array of integers, find the length of the longest consecutive elements sequence?
def find_longest_consecutive_elements_sequence(array):
    number_set = set(array)  # make a set of all numbers
    best_length = 0  # tracking the longest consecutive
    while number_set:
        number = number_set.pop()  # pick out an arbitrary number
        current_length = 1  # initialize current consecutive length
        number_copy = number
        while number_copy + 1 in number_set:
            number_set.remove(number_copy + 1)
            current_length += 1
        number_copy = number
        while number_copy - 1 in number_set:
            number_set.remove(number_copy - 1)
            current_length += 1
            current_length -= 1
        best_length = max(best_length, current_length)
        return best_length


# How to rotate an array left and right by a given number K?
def left_rotate_array(array, k):
    for i in range(k):
        temp = array[0]
        for i in range(len(array) - 1):
            array[i] = array[i + 1]
        array[len(array) - 1] = temp
    return array


def right_rotate_array(array, k):
    for i in range(k):
        temp = array[- 1]
        for i in reversed(range(len(array) - 1)):
            array[i + 1] = array[i]
        array[0] = temp
    return array













# How is an integer array sorted in place using the quicksort algorithm?
# The key process to quicksort is partitioning
# QuickSort is a Divide and Conquer algorithm


# How do you remove duplicates from an array in place?
# How do you reverse an array in place
# How are duplicates removed from an array without using any library?
# How to convert a byte array to String?
# What is the difference between an array and a linked list?
# How do you perform a binary search in a given array?
# How to find a median of two sorts arrays?

# How do you find duplicates from an unsorted array?
# Given an array of integers sorted in ascending order, find the starting and ending position of a given value?
# Given an integer array, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum?








if __name__ == '__main__':

    #r1 = find_missing_number_in_array([1, 2, 4, 6, 3, 7, 8])
    #print(r1)

    #r2 = find_duplicate_number_in_array([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
    #print(r2)

    #r3 = find_all_sum_pairs_in_array([2, 3, 4, -2, 6, 8, 9, 11], 6)
    #print(r3)

    #r4 = remove_duplicates_from_array([2, 3, 2, 4, 5, 6, 7, 7, 8, 9, 9])
    #print(r4)

    #r5 = find_target_in_rotated_array([4,5,6,7,0,1,2], 0)
    #print(r5)

    r6 = right_rotate_array([1, 2, 3, 4, 5, 6, 7], 2)
    print(r6)

