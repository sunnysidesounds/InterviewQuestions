
# O(n^2)
def insert_2(arr, index, value):
    arr = arr + [0]
    for i in range(len(arr)):
        if i == index:
            temp_value = arr[i]
            arr[i] = value
            for j in range(i + 1, len(arr), 1):
                temp2 = arr[j]
                arr[j] = temp_value
                temp_value = temp2
            break

    return arr


# O(n)
def insert(arr, index, value):
    arr = arr + [0]
    temp_value = arr[index]
    arr[index] = value
    for j in range(index + 1, len(arr), 1):
        temp2 = arr[j]
        arr[j] = temp_value
        temp_value = temp2

    return arr


# O(n ^2)
def delete_2(arr, index):
    for i in range(len(arr)):
        if i == index:
            arr[i] = arr[i + 1]
            for j in range(i + 1, len(arr), 1):
                if j < len(arr) - 1:
                    arr[j] = arr[j + 1]
                else:
                    del arr[j]

            break

    return arr


# O(n)
def delete(arr, index):
    arr[index] = arr[index + 1]
    for j in range(index + 1, len(arr), 1):
        if j < len(arr) - 1:
            arr[j] = arr[j + 1]
        else:
            del arr[j]

    return arr


def remove_all_elements_2(arr, val):
    for i in range(len(arr)):
        if i < len(arr) - 1:
            if val == arr[i]:
                arr[i] = arr[i + 1]
                for j in range(i + 1, len(arr), 1):
                    if j < len(arr) - 1:
                        arr[j] = arr[j + 1]
                    else:
                        del arr[j]
    return arr


def remove_all_elements(arr, val):
    length = len(arr) - 1
    for i in range(length):
        if arr[i] == val:
            del arr[i]
            length -= 1
    return len(arr)


def remove_duplicate_in_sorted_array(nums):
    for i in range(len(nums) -1 , 0, -1):
        if nums[i] == nums[i - 1]:
            del nums[i]

    return nums


def check_if_exist(arr):

    for i in range(len(arr)):
        if (2 * arr[i]) in arr:
            return True
        if (arr[i] / 2) in arr and arr[i] % 2 == 0:
            return True

    return False


# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
# [17,18,5,4,6,1] --> [18,6,6,6,1,-1]

# greatest_element = 1
# [17,18,5,4,6,-1]
# -1, 1

def replace_elements(arr):

    greatest_element = arr[len(arr) - 1]
    arr[len(arr) - 1] = -1

    for i in range(len(arr) - 2, -1, -1):

        current_element = arr[i]
        arr[i] = greatest_element

        if greatest_element < current_element:
            greatest_element = current_element


    return arr


def sort_array_by_parity(A):
    evens = [even for even in A if even % 2 == 0]
    odds = [odd for odd in A if odd % 2 == 1]
    return (evens + odds)


# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# Find all the elements of [1, n] inclusive that do not appear in this array.
# [4,3,2,7,8,2,3,1]
# [5,6]
# [value for value in the_list if value != val]

def find_disappeared_numbers(nums):

    for i in range(len(nums)):

        index = abs(nums[i]) - 1

        if nums[index] > 0:
            nums[index] *= -1

    result = []

    for i in range(1, len(nums) + 1):
        if nums[i - 1] > 0:
            result.append(i)

    return result

    #counter = 1
    #size = len(nums)
    #nums = list(set(nums))
    #for i in range(size):
    #    if counter in nums:
    #        nums.remove(counter)
    #    else:
    #        nums.append(counter)

    #    counter += 1

    #return nums



def find_max_consecutive_ones(nums):
    contiansZero = False
    ret = 0
    prevOnes = 0
    oneCount = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            if not contiansZero:
                contiansZero = True
            if i == 0 or nums[i-1] == 0:
                prevOnes = 0
            else:
                prevOnes = oneCount
            oneCount = 0 # reset one counting

        if nums[i] == 1:
            oneCount += 1
            ret = max(ret, prevOnes+oneCount)
    if contiansZero:
        return ret + 1
    else:
        return ret


def height_checker(heights):
    sorted_heights = sorted(heights)

    positions_changed = 0
    for position_old, position_new in zip(heights, sorted_heights):
        if position_old != position_new:
            positions_changed += 1

    return positions_changed






if __name__ == '__main__':

    arr = [1, 2, 2, 3, 5, 5, 6]
    arr2 = [1, 2, 2, 3, 5, 6]
    arr3 = [0, 1, 2, 2, 3, 0, 4, 2]

    arr5 = [0,0,1,1,1,2,2,3,3,4]

    arr6 = [17,18,5,4,6,1]

    results = height_checker([1,1,4,2,1,3])
    print(results)

    # [1,1,1,2,3,4]

    #results123 = find_max_consecutive_ones([1,1,0,1,1,1])
    #print(results123)

    #results99 = replace_elements(arr6)
    #print(results99)

    #results111 = sort_array_by_parity([3,1,2,4])

    #results333 = find_disappeared_numbers([4,3,2,7,8,2,3,1])
    #print(results333)


    #results = insert(arr, 2, 4)
    #print(results)

    #results4 = insert_2(arr2, 2, 4)
    #print(results4)


    #results7 = remove_all_elements(arr3, 2)
    #print(results7)

    #results10 = remove_duplicate_in_sorted_array(arr5)
    #print(results10)

    #results10 = check_if_exist([-2,0,10,-19,4,6,-8])
    #print(results10)

    #results2 = delete(arr, 0)
    #print(results2)
    #results3 = delete_2(arr2, 0)
    #print(results3)


#    value 4
#    index 2
#
#    input:
#    - [1, 2, 2, 3, 5, 6]
#    - iterate over until index match
#    - temp = 2, index = i
#    - place new value at index i , arr[i] == value
#    - [1, 2, 4, 3, 5, 6]
#    - i + 1 == temp 2
#    - temp = 3
#    - [1, 2, 4, 2, 5, 6]
#    - i + 1 == temp 3
#    - temp = 5
#    - [1, 2, 4, 2, 3, 6]
#    - i + 1 == temp 5
#    - temp = 6
#    - [1, 2, 4, 2, 3, 5]
#    - i + 1 == temp 6
#    - [1, 2, 4, 2, 3, 5, 6]
#
#
#
#
#    output:
#    [1, 2, 4, 2, 3, 5, 6]

