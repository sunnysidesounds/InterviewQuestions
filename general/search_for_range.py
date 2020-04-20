"""
Write a function that takes in a sorted array of integers as well as a target integer.
The function should use a variation of the Binary Search algorithm to find a range of indices in between
which the target number is contained in the array and should return this range in the form of an array.
The first number in the output array should represent the first index at which the target number is located
while the second number should represent the last index at which the target number is located.
The function should return [-1, -1] if the number is not contained in the array.

Sample input: [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45

Sample output: [4, 9]

def binary_search(input_array, value):
    low = 0
    high = len(input_array) - 1
    while (low <= high):
        mid = (low + high) // 2
        if (input_array[mid] == value):
            return value
        elif (input_array[mid] < value):
            low = mid +1
        else:
            high = mid -1

    return -1



"""


def search_for_range(array, target):
    low = 0
    high = len(array) - 1
    output_indexes = []
    has_left_index = False
    has_right_index = False

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            left_mid = mid - 1
            right_mid = mid + 1

            while left_mid <= right_mid and len(output_indexes) < 2:
                if array[left_mid] != target and not has_left_index:
                    output_indexes.append(left_mid + 1)
                    has_left_index = True
                else:
                    left_mid = left_mid - 1

                if array[right_mid] != target and not has_right_index:
                    output_indexes.append(right_mid - 1)
                    has_right_index = True
                else:
                    right_mid = right_mid + 1
            break

        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return sorted(output_indexes) if len(output_indexes) == 2 else [-1, -1]

    pass





if __name__ == '__main__':

    # middle find
   #results = search_for_range([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45)
   #if results[0] == 4 and results[1] == 9:
   #    print("PASSED middle find test: ", results)
   #else:
   #    print("FAILED middle find test: ", results)

   ## left find
   #results = search_for_range([0, 1, 21, 33, 33, 33, 45, 55, 55, 56, 56, 60, 61, 71, 73], 33)
   #if results[0] == 3 and results[1] == 5:
   #    print("PASSED left find test: ", results)
   #else:
   #    print("FAILED left find test: ", results)

   ## no find
   #results = search_for_range([0, 1, 21, 33, 33, 33, 45, 55, 55, 56, 56, 60, 61, 71, 73], 2)
   #if results[0] == -1 and results[1] == -1:
   #    print("PASSED no find test: ", results)
   #else:
   #    print("FAILED no find test: ", results)

   ## find one
   #results = search_for_range([0, 1, 21, 33, 33, 33, 45, 55, 55, 56, 56, 60, 61, 71, 73], 21)
   #if results[0] == 2 and results[1] == 2:
   #    print("PASSED one find test: ", results)
   #else:
   #    print("FAILED one find test: ", results)

    # find at end
    results = search_for_range([0, 1, 21, 33, 33, 33, 45, 55, 55, 56, 56, 60, 61, 71, 73], 73)
    if results[0] == 14 and results[1] == 14:
        print("PASSED one find test: ", results)
    else:
        print("FAILED one find test: ", results)

    results = search_for_range([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 45, 45, 45], 45)
    if results[0] == 4 and results[1] == 12:
        print("PASSED one find test: ", results)
    else:
        print("FAILED one find test: ", results)