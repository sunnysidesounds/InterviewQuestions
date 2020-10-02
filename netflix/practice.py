

# Given a two-dimensional array, if any element within is zero, make its whole row and column zero.
def make_zero(matrix):
    """
    Naive Approach
    :param matrix:
    :return:
    """
    zero_indexes = []
    for x in range(len(matrix)): # O(x * y) or O(n)
        for y in range(len(matrix[0])):
            value = matrix[x][y]
            if value == 0:
                if (x, y) not in zero_indexes:
                    zero_indexes.append((x, y))

    for (row_index, column_index) in zero_indexes:

        # change row: row 1, column 2
        for i in range(len(matrix)):
            matrix[row_index][i] = 0

        for j in range(len(matrix[0])):
            matrix[j][column_index] = 0

    return matrix

def make_zero_2(matrix):
    """
    Naive Approach
    :param matrix:
    :return:
    """
    for x in range(len(matrix)): # O(x * y) or O(n)
        for y in range(len(matrix[0])):
            value = matrix[x][y]
            if value == 0:
                for i in range(len(matrix)):
                    matrix[x][i] = 0

                for j in range(len(matrix[0])):
                    matrix[j][y] = 0

    return matrix


# Given an array of integers and a value, determine if there are any three integers in the array whose sum equals the given value.
# Input: array = {12, 3, 4, 1, 6, 9}, sum = 24;
# Output: 12, 3, 9

def find_sum_triplet(nums, num_sum):
    results = []
    sorted_nums = sorted(nums)

    for i in range(len(sorted_nums) - 2):
        current_value = sorted_nums[i]
        left = i + 1
        right = len(sorted_nums) - 1
        while left < right:
            left_value = sorted_nums[left]
            right_value = sorted_nums[right]
            value_sum = (current_value + left_value + right_value)
            if value_sum == num_sum:
                if (current_value, left_value, right_value) not in results:
                    results.append((current_value, left_value, right_value))
                    left += 1
                    right -= 1
            elif value_sum > num_sum:
                right -= 1
            else:
                left += 1

    return results


# Remove Even Integers from Array
def remove_even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            numbers.remove(number)
    return numbers

# Merge Two Sorted Arrays
def merge_two_sorted_array(num1, num2):
    merged_array = []
    for n1, n2 in zip(num1, num2):
        if n1 < n2:
            merged_array.extend([n1, n2])  # append single value, extend multiple values
        else:
            merged_array.extend([n2, n1])
    return merged_array


# First Non-Repeating Integer in an Array
#Input : -1 2 -1 3 2
#Output : 3
def find_non_repeating(numbers):
    dmap = {}
    results = []
    for number in numbers:
        if number not in dmap:
            dmap[number] = 1
        else:
            dmap[number] += 1

    for key, value in dmap.items():
        if value == 1:
            results.append(key)

    return results

# Find the k largest and smallest Values in an Array
# [1, 23, 12, 9, 30, 2, 50]
# k = 3
# 50, 30 and 23.
def find_largest_smallest_values(nums, k):
    results = {"smallest": [], "largest": []}
    sorted_numbers = sorted(nums)
    for i in range(k):
        results['smallest'].append(sorted_numbers[i])
    for j in range(len(sorted_numbers) - 1, 0, -1):
        if j == k:
            break
        results['largest'].append(sorted_numbers[j])
    return results

# Use temporary array
#K largest elements from arr[0..n-1]

#1) Store the first k elements in a temporary array temp[0..k-1].
#2) Find the smallest element in temp[], let the smallest element be min.
#3-a) For each element x in arr[k] to arr[n-1]. O(n-k)
#If x is greater than the min then remove min from temp[] and insert x.
#3-b)Then, determine the new min from temp[]. O(k)
#4) Print final k elements of temp[]

#Time Complexity: O((n-k)*k). If we want the output sorted then O((n-k)*k + klogk)
def find_k_largest_elements(arr, k):
    temp = []
    for i in range(0, k):
        temp.append(arr[i])

    smallest_element = min(temp)
    for x in range(k, len(arr)):
        if arr[x] > smallest_element:
            temp.remove(smallest_element)
            temp.append(arr[x])
        smallest_element = min(temp)

    return temp

def find_k_smallest_elements(arr, k):
    temp = []
    for i in range(0, k):
        temp.append(arr[i])

    largest_element = max(temp)
    for x in range(k, len(arr)):
        if arr[x] < largest_element:
            temp.remove(largest_element)
            temp.append(arr[x])
        largest_element = max(temp)
    return temp

















if __name__ == '__main__':


    #results = find_sum_triplet([12, 3, 4, 1, 6, 9, 2, 5, 7], 24)
    #print(results)

    results = find_largest_smallest_values([1, 23, 12, 9, 30, 2, 50], 3)
    print(results)